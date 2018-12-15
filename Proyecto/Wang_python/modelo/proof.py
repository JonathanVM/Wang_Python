"""
Prototipo de modelo de objetos para Wang
loriacarlos@gmail.com
@since II-2018
coautores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
"""

from deduction import *
from formula import *
from enum import Enum, auto
from abc import ABCMeta, abstractmethod
from deduction import *
from formula import *
import utils

class RuleType(Enum):
    AXIOM = auto()
    NOT_LEFT = auto()
    NOT_RIGHT = auto()
    OR_LEFT = auto()
    OR_RIGHT = auto()
    AND_LEFT = auto()
    AND_RIGHT = auto()
    EQUIV = auto()
    TWO_THEN = auto()

class Just:
    def __init__(self, subject, rule):
        self.subject = subject
        self.rule = rule
        
class Rule(metaclass=ABCMeta):
    def __init__(self, ruletype):
        self.__ruletype = ruletype
    @abstractmethod
    def apply(self, deduction): pass
    @property
    def kind(self):
        return self.__ruletype

class Axiom(Rule):
    def __init__(self):
        super().__init__(RuleType.AXIOM)
    def apply(self, deduction):
        for (pi, p) in enumerate(deduction.left):
            for (pd, q) in enumerate(deduction.right):
                if q == p:
                    yield (self.kind, pi, pd, deduction)

AXIOM_RULE = Axiom()

class NotLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.NOT_LEFT)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.left):
            if isinstance(f, Not):
                newleft = utils.replace(deduction.left, p, [])
                newright = utils.replace(deduction.right, len(deduction.right), [f.left])
                yield (self.kind, p, Deduction(list(newleft), list(newright)))

NOT_LEFT_RULE = NotLeft()

class NotRight(Rule):
    def __init__(self):
        super().__init__(RuleType.NOT_RIGHT)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.right):
            if isinstance(f, Not):
                newleft = utils.replace(deduction.left, len(deduction.left), [f.left])
                newright = utils.replace(deduction.right, p, [])
                yield (self.kind, p, Deduction(list(newleft), list(newright)))

NOT_RIGHT_RULE = NotRight()

class AndLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.AND_LEFT)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.left):
            if isinstance(f, And):
                newleft = utils.replace(deduction.left, p, [f.left, f.right])
                yield (self.kind, p, Deduction(list(newleft), deduction.right))

AND_LEFT_RULE = AndLeft()

class OrRight(Rule):
    def __init__(self):
        super().__init__(RuleType.OR_RIGHT)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.right):
            if isinstance(f, Or):
                newRight = utils.replace(deduction.right, p, [f.left, f.right])
                yield (self.kind, p, Deduction(deduction.left, list(newRight)))

OR_RIGHT_RULE = OrRight()

class OrLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.OR_LEFT)
    def apply(self, deduction):

        for (p, f) in enumerate(deduction.left):
            if isinstance(f, Or):
                deductionA = utils.replace(deduction.left, p, [f.left])
                deductionB = utils.replace(deduction.left, p, [f.right])
                yield (self.kind, p, Deduction(list(deductionA), deduction.right), Deduction(list(deductionB), deduction.right))

OR_LEFT_RULE= OrLeft()

class AndRight(Rule):
    def __init__(self):
        super().__init__(RuleType.AND_RIGHT)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.right):
            if isinstance(f, And):
                deductionA = utils.replace(deduction.right, p, [f.left])
                deductionB = utils.replace(deduction.right, p, [f.right])
                yield (self.kind, p, Deduction(deduction.left, list(deductionA)), Deduction(deduction.left, list(deductionB)))

AND_RIGHT_RULE = AndRight()
            
class Equiv(Rule):
    def __init__(self):
        super().__init__(RuleType.EQUIV)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.left):
            if isinstance(f, Then):
                newleft = utils.replace(deduction.left, p, [Or(Not(f.left), f.right)])
                yield (self.kind, p, -1, Deduction(list(newleft), deduction.right))
        for (p, f) in enumerate(deduction.right):
            if isinstance(f, Then):
                newRight = utils.replace(deduction.right, p, [Or(Not(f.left), f.right)])
                yield (self.kind, -1, p, Deduction(deduction.left, list(newRight)))

EQUIV_RULE = Equiv()

class Iff(Rule):
    def __init__(self):
        super().__init__(RuleType.TWO_THEN)
    def apply(self, deduction):
        for (p, f) in enumerate(deduction.left):
            if isinstance(f, Biconditional):
                newleft = utils.replace(deduction.left, p, [And(Then(f.left, f.right), Then(f.right, f.left))])
                yield (self.kind, p, -1, Deduction(list(newleft), deduction.right))
        for (p, f) in enumerate(deduction.right):
            if isinstance(f, Biconditional):
                newRight = utils.replace(deduction.right, p, [And(Then(f.left, f.right), Then(f.right, f.left))])
                yield (self.kind, -1, p, Deduction(deduction.left, list(newRight)))

IFF_RULE = Iff()

if __name__ == "__main__":
    print("*** Testing Proofs ***")
    t = TRUE
    f = FALSE
    p = Atom("p")
    q = Atom("q")
    a = And(p, q)
    na = Not(a)
    b = Or(a, p)
    z = Biconditional(p, a)
    c = Then(p, b)
    ded = Deduction([z, p, c, na], [q, na])

    print(ded)

    print("1) Axiom test", ded)
    for f in AXIOM_RULE.apply(ded):
        print(f)


    print("2) NotLeft Test", ded)
    for f in NOT_LEFT_RULE.apply(ded):
        print(f)
    print("3) NotRight Test", ded)
    for f in NOT_RIGHT_RULE.apply(ded):
        print(f)

    """
    print("4) AndLeft Test", ded)
    for f in AND_LEFT_RULE.apply(ded):
        print(f)
    print("5) OrRight Test", ded)
    for f in OR_RIGHT_RULE.apply(ded):
       print(f)
    """
    """
    print("6) AndRight Test", ded)
    for f in AND_RIGHT_RULE.apply(ded):
        print(f)   
    print("7) OrLeft Test", ded)
    for f in OR_LEFT_RULE.apply(ded):
       print(f)


    print("8) Equiv Test", ded)
    for f in EQUIV_RULE.apply(ded):
        print(f)

    print("9) Doble Implica Test", ded)
    for f in IFF_RULE.apply(ded):
        print(f)
    """
