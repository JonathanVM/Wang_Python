"""
autores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
"""


from deduction import *
from proof import *

class DeductionTree:
    def __init__(self):
        pass
        
    def toJsonString(self, child):
        return {
            RuleType.AXIOM: self.axiomJsonString,
            RuleType.AND_RIGHT: self.otherRules,
            RuleType.OR_LEFT: self.otherRules,
            RuleType.AND_LEFT: self.otherRules,
            RuleType.OR_RIGHT: self.otherRules,
            RuleType.NOT_RIGHT: self.otherRules,
            RuleType.NOT_LEFT: self.otherRules,
            RuleType.EQUIV: self.equiv_IffJsonString,
            RuleType.TWO_THEN: self.equiv_IffJsonString,
        }[child[0]]
    def twoPositionsRules(self, child, deduction):
        return f'"posLeft":{child[1]}, "posRight":{child[2]}, "deduction":"{deduction}"' + ('}' if child[0] == RuleType.AXIOM else f', "children":[{self.buildTree(child[3])}' + ']}')
    def axiomJsonString(self, child, deduction):
        return '{' + f'"RuleType":"{self.stringRule(child[0])}", "posLeft":{child[1]}, "posRight":{child[2]}, "deduction":"{deduction}"' + '}'

    def equiv_IffJsonString(self, child, deduction):
        return '{' + f'"RuleType":"{self.stringRule(child[0])}", "posLeft":{child[1]}, "posRight":{child[2]}, "deduction":"{deduction}", "children":[{self.buildTree(child[3])}' + ']}'

    def otherRules(self, child, deduction):
        string = '{' + f'"RuleType":"{self.stringRule(child[0])}", "pos":{child[1]}, "deduction":"{deduction}", "children":[{self.buildTree(child[2])}'
        return string + (f', {self.buildTree(child[3])}]' + '}' if child[0] == RuleType.AND_RIGHT or child[0] == RuleType.OR_LEFT else ']}')
    def buildTree(self, deduction):
        try:
            child = next(self.evaluateDeduction(deduction))
            function =  self.toJsonString(child)
            return function(child,deduction)
        except StopIteration:
            return '{' + f'"deduction":"{deduction}", "children":[]' + '}'
            
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
        AND_RIGHT_RULE.apply,
        OR_LEFT_RULE.apply,
        NOT_LEFT_RULE.apply,
        NOT_RIGHT_RULE.apply,
    )
    def stringRule(self, rule):
        return {
            RuleType.AXIOM: "AXIOM",
            RuleType.AND_RIGHT: "AND RIGHT",
            RuleType.AND_LEFT: "AND LEFT",
            RuleType.OR_RIGHT: "OR RIGHT",
            RuleType.OR_LEFT: "OR LEFT",
            RuleType.NOT_RIGHT: "NOT RIGHT",
            RuleType.NOT_LEFT: "NOT LEFT",
            RuleType.EQUIV: "EQUIV",
            RuleType.TWO_THEN: "BICONDITIONAL",
        }[rule]

if __name__ == "__main__":
    print("*** Testing deductionTree ***")
    t = TRUE
    f = FALSE
    p = Atom("p")
    q = Atom("q")
    np = Not(p)
    np2 = Not(p)
    nq = Not(q)
    npnq = And(np, nq)
    a = And(p, q)
    na = Not(a)
    b = Or(a, p)
    z = Biconditional(p, a)
    qp = Then(q, p)
    c = Then(p, z)
    ded = Deduction([np, qp], [np,nq])
    DEDUCTION_TREE = DeductionTree()
    
    print(DEDUCTION_TREE.x(RuleType.AXIOM))
    print(DEDUCTION_TREE.x(RuleType.OR_RIGHT))
    print(DEDUCTION_TREE.x(RuleType.TWO_THEN))
    #print(DEDUCTION_TREE.stringRule(qp.kind))
    print(DEDUCTION_TREE.buildTree(ded))
