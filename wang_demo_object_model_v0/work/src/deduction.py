"""
Demo de una deduccion en Wang
Deduccciones
loriacarlos@gmail.com
@since II-2018
"""

from  formula import *
from functools import reduce

class Deduction:
    def __init__(self, left=[], right=[]):
        self.left = left
        self.right = right
    def _stringify(self, view):
        leftded  = ", ".join(map(view, self.left))
        rightded = ", ".join(map(view, self.right))
        return f"{leftded} => {rightded}"
    def __repr__(self):
        return self._stringify(repr)
    def __str__(self):
        return self._stringify(str)
    def to_formula(self):
        left = reduce(lambda a, f: And(a, f), self.left)
        right = reduce(lambda a, f: Or(a, f), self.right)
        return Then(left, right)
    def generadorAtomos(self):
        expresion = self.__str__()
        #filter(lambda x : if x.isalpha(): yield x, expresion)
        for n in expresion:
            if n.isalpha(): yield n
if __name__ == "__main__":
    print("*** Testing Deductions ***")
    t = TRUE
    f = FALSE
    p = Atom("p")
    q = Atom("q")
    a = And(p, q)
    na = Not(a)
    b = Or(a, na)
    c = Then(p, b)
    ded = Deduction([a, b], [na, c])
    generador = ded.generadorAtomos()
    expresion = ded.__str__();
    while True:
        try:
            print(next(generador))
        except StopIteration:
            break;


    print(ded)
    print(ded.to_formula())
    ded2 = Deduction([p, q, p], [q, Not(q)])
    print(ded2, ded2.to_formula())
