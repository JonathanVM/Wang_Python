"""
Prototipo de modelo de objetos para Wang
loriacarlos@gmail.com
@since II-2018
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
    OR_LEFT = auto()
    OR_RIGHT = auto()
    AND_LEFT = auto()
    AND_RIGHT = auto()
    EQUIV = auto()

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
            if p in deduction.right:
                yield (self.kind, pi, deduction)
        

AXIOM_RULE = Axiom()

class AndLeft(Rule):
    def __init__(self):
        super().__init__(RuleType.AND_LEFT)
    def apply(self, deduction):
        ands = (f for f in deduction.left if isinstance(f, And))
        for (p, f) in enumerate(ands):
            newleft = utils.replace(deduction.left, p, [f.left, f.right])
            yield (self.kind, p, Deduction(list(newleft), deduction.right))
            
AND_LEFT_RULE= AndLeft()        
            
        
if __name__ == "__main__":
    print("*** Testing Proofs ***")
    t = TRUE
    f = FALSE
    p = Atom("p")
    q = Atom("q")
    a = And(p, q)
    na = Not(a)
    b = Or(a, na)
    c = Then(p, b)
    ded = Deduction([a, b, p], [na, c, p])
    print("1) Axiom test", ded)
    for f in AXIOM_RULE.apply(ded):
        print(f)
    print("2) AndLeft Test", ded)
    for f in AND_LEFT_RULE.apply(ded):
        print(f)
    
    