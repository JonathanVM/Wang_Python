__author__ = 'jszheng'
__coauthor__ = 'loriacarlos@gmail.com'

from WangVisitor import WangVisitor
from WangParser import WangParser
#from Proyecto.formula import *

"""
    Tests Wang Visitor
    See grammar/Wang.g4
    based on jszheng git https://github.com/jszheng/py3antlr4book
    Example calc
"""
class WangPrintVisitor(WangVisitor):
    def __init__(self):
        pass
        
    def visitFormExpr(self, ctx):
        print(f'\nStart Visiting FormExpr (=>) {len(ctx.sequence())} children')
        children = ctx.sequence()
        for ch in children:
            self.visit(ch)
    
    def visitSeqExpr(self, ctx):
        print(f'Visiting SeqExpr (,) with {len(ctx.expr())} children')
        children = ctx.expr()
        for ch in children:
            self.visit(ch)
    
    def visitId(self, ctx):
        name = ctx.ID().getText()
        print(f'Visiting Id={name}')

    def visitAndExpr(self, ctx):
        print('Visiting AndExpr (&)')
		And(ctx.expr(0),ctx.expr(1))
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        

    def visitOrExpr(self, ctx):
        print('Visiting OrExpr (|)')
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
       

    def visitParens(self, ctx):
        print('Visiting ParenExpr (...)')
        self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        print('Visiting NotExpr (~) ')
        self.visit(ctx.expr())
        

    
