from deduction import *
from proof import *
class Nodo:
    def __init__(self, info, left = None, right = None):
        self.info = info
        self.right = right
        self.left = left
    def __str__(self):
        return self.root
    def __repr__(self):
        return str(self)

class DeductionTree:
    def __init__(self, deduction):
        self.deduction = deduction
        self.tree = []
    def buidTree(self, deduction):
        try:
            child = self.evaluateDeduction(deduction)
            if(child[0] == RuleType.AXIOM):
                return Nodo(child)
            
        except StopIteration:
            return
    def pipe(self, current, *iterables):
        for n in iterables:
            yield from n(current)

    evaluateDeduction = lambda self, current: self.pipe(
        current,
        AXIOM_RULE.apply,
        AND_LEFT_RULE.apply,
        OR_RIGHT_RULE.apply,
        EQUIV_RULE.apply,
        IFF_RULE.apply,
        NOT_LEFT_RULE.apply,
        NOT_RIGHT_RULE.apply,
        AND_RIGHT_RULE.apply,
        OR_LEFT_RULE.apply,
    )


if __name__ == "__main__":
    print("*** Testing deductionTree ***")
    t = TRUE
    f = FALSE
    p = Atom("p")
    q = Atom("q")
    a = And(p, q)
    na = Not(a)
    b = Or(a, p)
    z = Biconditional(p, a)
    c = Then(p, b)
    ded = Deduction([z, p, c], [q, c])
    DEDUCTION_TREE = DeductionTree(ded)
    prueba_eval = DEDUCTION_TREE.evaluateDeduction(ded)
    print(f"Original: {ded}")
    print(f"Evaluado1: {next(prueba_eval)}")
