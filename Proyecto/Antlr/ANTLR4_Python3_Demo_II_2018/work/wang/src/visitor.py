__author__ = 'jszheng'
__coauthor__ = 'loriacarlos@gmail.com'

from WangVisitor import WangVisitor
from WangParser import WangParser
from ....formula import *
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
            if not formulaPrint:
                yield "La expresión no es correcta"
                print(f"La expresion no es correcta\n")
            else:
                yield "La expresión es correcta"
                print(f"La expresion es correcta\n")
        
    def visitPremises(self, ctx):
        list_res = self.visit(ctx.sequence())
        print(f"Premisas: {list_res}")
        return list_res
        
        
    def visitConclusions(self, ctx):
        list_res = self.visit(ctx.sequence())
        print(f"Conclusiones: {list_res}")
        return list_res
        
    def visitFormExpr(self, ctx):
        #print(f'\nStart Visiting FormExpr (=>) {len(ctx.conclusions())} children')
        res_premises = self.visit(ctx.premises())
        res_conclusions = self.visit(ctx.conclusions())
        #Verificar si premisas esta vacia
        if not res_premises:
            return None
        elif not res_conclusions:
            return Deduction(res_premises)
        else:
            return Deduction(res_premises, res_conclusions)
    
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

    def visitParens(self, ctx):
        print('Visiting ParenExpr (...)')
        return self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        print('Visiting NotExpr (~) ')
        return Not(self.visit(ctx.expr()))

