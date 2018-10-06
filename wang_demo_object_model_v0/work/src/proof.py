"""
Prototipo de modelo de objetos para Wang
loriacarlos@gmail.com
@since II-2018
"""

from deduction import *
from formula import *
from enum import Enum, auto

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
    