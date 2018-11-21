from deduction import *
from proof import *

class DeductionTree:
    def __init__(self):
        pass
    def buildTree(self, deduction):
        try:
            child = next(self.evaluateDeduction(deduction))
            if child[0] == RuleType.AXIOM:
                return '{' + f'"RuleType":"{self.stringRule(child[0])}", "posLeft":{child[1]}, "posRight":{child[2]}, "deduction":"{deduction}"' + '}'
            if child[0] == RuleType.EQUIV or child[0] == RuleType.TWO_THEN:
                return '{' + f'"RuleType":"{self.stringRule(child[0])}", "posLeft":{child[1]}, "posRight":{child[2]}, "deduction":"{deduction}", "children":[{self.buildTree(child[3])}' + ']}'
            string = '{' + f'"RuleType":"{self.stringRule(child[0])}", "pos":{child[1]}, "deduction":"{deduction}", "children":[{self.buildTree(child[2])}'
            if child[0] == RuleType.AND_RIGHT or child[0] == RuleType.OR_LEFT:
                return string + f', {self.buildTree(child[3])}]' + '}'
            return string + ']}'

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
    ded = Deduction([np, qp], [npnq])
    DEDUCTION_TREE = DeductionTree()
    print(DEDUCTION_TREE.stringRule(qp.kind))
    """prueba_eval = DEDUCTION_TREE.evaluateDeduction(ded)
    print(f"Original: {ded}")
    print(f"Evaluado1: {next(prueba_eval)}")"""
    print(DEDUCTION_TREE.buildTree(ded))
