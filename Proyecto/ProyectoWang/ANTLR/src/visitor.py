__author__ = 'jszheng'
__coauthor__ = 'loriacarlos@gmail.com'

import sys
sys.path.insert(0, '..\ANTLR\parser\grammar')
from WangVisitor import WangVisitor
from WangParser import WangParser

sys.path.insert(0, '..\modelo')
from formula import *
from deduction import *

"""
    Tests Wang Visitor
    See grammar/Wang.g4
    based on jszheng git https://github.com/jszheng/py3antlr4book
    Example calc
"""
class WangPrintVisitor(WangVisitor):
    def __init__(self):
        pass
        
    def visitAssertion(self, ctx):
        print(f"Total de formula: {len(ctx.formula())}")
        for i in range(len(ctx.formula()) - 1):
            formulaPrint = self.visit(ctx.formula(i))
            yield formulaPrint
        
    def visitPremises(self, ctx):
        list_res = self.visit(ctx.sequence())
        print(f"Premisas: {list_res}")
        return list_res
        
        
    def visitConclusions(self, ctx):
        list_res = self.visit(ctx.sequence())
        print(f"Conclusiones: {list_res}")
        return list_res
        
    def visitFormExpr(self, ctx):
        res_premises = self.visit(ctx.premises())
        res_conclusions = self.visit(ctx.conclusions()) if ctx.conclusions() else []
        return Deduction(res_premises, res_conclusions) if res_premises else Deduction([],res_conclusions)
    
    def visitSeqExpr(self, ctx):
        print(f'Visiting SeqExpr (,) with {len(ctx.expr())} children')
        children = ctx.expr()
        return [self.visit(ch) for ch in children]
    
    def visitId(self, ctx):
        name = ctx.ID().getText()
        print(f'Visiting Id={name}')
        return Atom(name)

    def visitAndExpr(self, ctx):
        print('Visiting AndExpr (&)')
        res_left = self.visit(ctx.expr(0))
        res_right = self.visit(ctx.expr(1))
        return  And(res_left, res_right)

    def visitOrExpr(self, ctx):
        print('Visiting OrExpr (|)')
        res_left = self.visit(ctx.expr(0))
        res_right = self.visit(ctx.expr(1))
        return  Or(res_left, res_right)
     
    def visitImplyExpr(self, ctx):
        print ('Visiting ImplyExpr (->) ')
        res_left = self.visit(ctx.expr(0))
        res_right = self.visit(ctx.expr(1))
        return Then(res_left, res_right)
        
    def visitBiconditionalExpr(self, ctx):
        print ('Visiting BiconditionalExpr (<->) ')
        res_left = self.visit(ctx.expr(0))
        res_right = self.visit(ctx.expr(1))
        return Biconditional(res_left, res_right)

    def visitParens(self, ctx):
        print('Visiting ParenExpr (...)')
        return self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        print('Visiting NotExpr (~) ')
        return Not(self.visit(ctx.expr()))

