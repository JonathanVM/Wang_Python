"""
Demo de modelo de objetos para Wang
Formulas logicas
loriacarlos@gmail.com
@since II-2018
"""
from functools import total_ordering

@total_ordering
class Operator:
    def __init__(self, name, arity=0, preced=128):
        self.name = name
        self.arity = arity
        self.preced = preced
    def __str__(self):
        return self.name
    def __repr__(self):
        #return f"Operator(name={repr(self.name)}, arity={self.arity})"
        return str(self)
    def __eq__(self, other):
        if self is other: return True
        if not isinstance(other, Operator) : return False
        return self.name == other.name
    def __lt__(self, other):
        if self is other: return False
        if not isinstance(other, Operator) : return False
        return self.preced < other.preced
        
        
OR = Operator("|", arity=2, preced=4)
AND = Operator("&", arity=2, preced=8)
THEN = Operator("->", arity=2, preced=2)
NOT = Operator("~", arity=1, preced=16)


    
class Formula:
    def __init__(self, *args):
        self.args = args
    @property
    def left(self):
        if len(self.args) == 0 : return None
        return self.args[0]
    @property
    def right(self):
        if len(self.args) < 2 : return self.left
        return self.args[1]
        
    def stringify(self, oper, met=str):
        assert(isinstance(oper, Operator) and 0 <= oper.arity <= 2)
        if oper.arity == 0:
            return f"{oper}"
        if oper.arity == 1:
            left_str = f"{met(self.left)}"
            if oper > self.left.oper:
                return f"{oper}({left_str})"
            else:
                return f"{oper}{left_str}"
        if oper.arity == 2:
            left_str = f"{met(self.left)}"
            right_str = f"{met(self.right)}"
            #print("**", oper, left_str, right_str)
            left_str = f"({left_str})" if oper > self.left.oper else left_str
            right_str = f"({right_str})" if oper >= self.right.oper else right_str
            return f"{left_str} {oper} {right_str}"
            
    def weak_nf(self):
        return self
    def atoms(self):
        for f in self.args:
            yield from f.atoms()
            
class Atom(Operator, Formula):
    def __init__(self, name):
        Operator.__init__(self, name)
        Formula.__init__(self)
        self.oper = self
    def atoms(self):
        yield self
        
TRUE = Atom("true")
FALSE = Atom("false")

class StrReprMixin:
    def __repr__(self):
        return self.stringify(self.oper)
    def __str__(self):
        return self.stringify(self.oper, str)
        
class BiFormula(Formula, StrReprMixin):
    def __init__(self, oper, left, right):
        super().__init__(left, right)
        self.oper = oper
        
class MonoFormula(Formula, StrReprMixin):
    def __init__(self, oper, left):
        super().__init__(left)
        self.oper = oper

# Implementaciones concretas        
class Not(MonoFormula):
    def __init__(self, left):
        super().__init__(NOT, left)

class Or(BiFormula):
    def __init__(self, left, right):
        super().__init__(OR, left, right)
        
class And(BiFormula):
    def __init__(self, left, right):
        super().__init__(AND, left, right)
        
class Then(BiFormula):
    def __init__(self, left, right):
        super().__init__(THEN, left, right)
    def weak_nf(self):
        return Or(Not(self.left), self.right)
  
if __name__ == "__main__":
    print("*** Testing formulas ***")
    t = TRUE
    f = FALSE
    a = And(t, f)
    print("1", a)
    na = Not(a)
    b = Or(a, na)
    print("2", b)
    c = And(t, Or(t, t))
    print("3", c)
    d = Then(f, b)
    print("4", d)
    print("5", d.weak_nf())
    # Atoms
    p = Atom("p")
    e = Or(p, And(d, Not(p)))
    for a in e.atoms():
        print(a)