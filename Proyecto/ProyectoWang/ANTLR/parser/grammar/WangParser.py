# Generated from .\grammar\Wang.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\5\3\5\3\6\5\6%\n\6\3\7")
        buf.write("\3\7\3\7\7\7*\n\7\f\7\16\7-\13\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\67\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b\3\b\2\3\16\t")
        buf.write("\2\4\6\b\n\f\16\2\2\2L\2\20\3\2\2\2\4\32\3\2\2\2\6\37")
        buf.write("\3\2\2\2\b!\3\2\2\2\n$\3\2\2\2\f&\3\2\2\2\16\66\3\2\2")
        buf.write("\2\20\25\5\4\3\2\21\22\7\6\2\2\22\24\5\4\3\2\23\21\3\2")
        buf.write("\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3")
        buf.write("\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2\2\32\35")
        buf.write("\5\6\4\2\33\34\7\7\2\2\34\36\5\b\5\2\35\33\3\2\2\2\35")
        buf.write("\36\3\2\2\2\36\5\3\2\2\2\37 \5\n\6\2 \7\3\2\2\2!\"\5\n")
        buf.write("\6\2\"\t\3\2\2\2#%\5\f\7\2$#\3\2\2\2$%\3\2\2\2%\13\3\2")
        buf.write("\2\2&+\5\16\b\2\'(\7\5\2\2(*\5\16\b\2)\'\3\2\2\2*-\3\2")
        buf.write("\2\2+)\3\2\2\2+,\3\2\2\2,\r\3\2\2\2-+\3\2\2\2./\b\b\1")
        buf.write("\2/\60\7\b\2\2\60\67\5\16\b\t\61\67\7\r\2\2\62\63\7\3")
        buf.write("\2\2\63\64\5\16\b\2\64\65\7\4\2\2\65\67\3\2\2\2\66.\3")
        buf.write("\2\2\2\66\61\3\2\2\2\66\62\3\2\2\2\67F\3\2\2\289\f\b\2")
        buf.write("\29:\7\t\2\2:E\5\16\b\t;<\f\7\2\2<=\7\n\2\2=E\5\16\b\b")
        buf.write(">?\f\6\2\2?@\7\13\2\2@E\5\16\b\7AB\f\5\2\2BC\7\f\2\2C")
        buf.write("E\5\16\b\5D8\3\2\2\2D;\3\2\2\2D>\3\2\2\2DA\3\2\2\2EH\3")
        buf.write("\2\2\2FD\3\2\2\2FG\3\2\2\2G\17\3\2\2\2HF\3\2\2\2\t\25")
        buf.write("\35$+\66DF")
        return buf.getvalue()


class WangParser ( Parser ):

    grammarFileName = "Wang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'.'", "'=>'", "'~'", 
                     "'&'", "'|'", "'<->'", "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMA", "DOT", 
                      "LEADSTO", "NOT", "AND", "OR", "BICONDITIONAL", "IMPLIES", 
                      "ID", "WS", "ErrorChar" ]

    RULE_assertion = 0
    RULE_formula = 1
    RULE_premises = 2
    RULE_conclusions = 3
    RULE_sequence = 4
    RULE_listexpr = 5
    RULE_expr = 6

    ruleNames =  [ "assertion", "formula", "premises", "conclusions", "sequence", 
                   "listexpr", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    COMMA=3
    DOT=4
    LEADSTO=5
    NOT=6
    AND=7
    OR=8
    BICONDITIONAL=9
    IMPLIES=10
    ID=11
    WS=12
    ErrorChar=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class AssertionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.FormulaContext)
            else:
                return self.getTypedRuleContext(WangParser.FormulaContext,i)


        def EOF(self):
            return self.getToken(WangParser.EOF, 0)

        def getRuleIndex(self):
            return WangParser.RULE_assertion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertion" ):
                return visitor.visitAssertion(self)
            else:
                return visitor.visitChildren(self)




    def assertion(self):

        localctx = WangParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assertion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.formula()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WangParser.DOT:
                self.state = 15
                self.match(WangParser.DOT)
                self.state = 16
                self.formula()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(WangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WangParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FormExprContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def premises(self):
            return self.getTypedRuleContext(WangParser.PremisesContext,0)

        def conclusions(self):
            return self.getTypedRuleContext(WangParser.ConclusionsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormExpr" ):
                return visitor.visitFormExpr(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = WangParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formula)
        self._la = 0 # Token type
        try:
            localctx = WangParser.FormExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.premises()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WangParser.LEADSTO:
                self.state = 25
                self.match(WangParser.LEADSTO)
                self.state = 26
                self.conclusions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PremisesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(WangParser.SequenceContext,0)


        def getRuleIndex(self):
            return WangParser.RULE_premises

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPremises" ):
                return visitor.visitPremises(self)
            else:
                return visitor.visitChildren(self)




    def premises(self):

        localctx = WangParser.PremisesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_premises)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConclusionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(WangParser.SequenceContext,0)


        def getRuleIndex(self):
            return WangParser.RULE_conclusions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConclusions" ):
                return visitor.visitConclusions(self)
            else:
                return visitor.visitChildren(self)




    def conclusions(self):

        localctx = WangParser.ConclusionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conclusions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listexpr(self):
            return self.getTypedRuleContext(WangParser.ListexprContext,0)


        def getRuleIndex(self):
            return WangParser.RULE_sequence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = WangParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << WangParser.T__0) | (1 << WangParser.NOT) | (1 << WangParser.ID))) != 0):
                self.state = 33
                self.listexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WangParser.RULE_listexpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SeqExprContext(ListexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ListexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqExpr" ):
                return visitor.visitSeqExpr(self)
            else:
                return visitor.visitChildren(self)



    def listexpr(self):

        localctx = WangParser.ListexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listexpr)
        self._la = 0 # Token type
        try:
            localctx = WangParser.SeqExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.expr(0)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WangParser.COMMA:
                self.state = 37
                self.match(WangParser.COMMA)
                self.state = 38
                self.expr(0)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class BiconditionalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiconditionalExpr" ):
                return visitor.visitBiconditionalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ImplyExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplyExpr" ):
                return visitor.visitImplyExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WangParser.NOT]:
                localctx = WangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 45
                self.match(WangParser.NOT)
                self.state = 46
                self.expr(7)
                pass
            elif token in [WangParser.ID]:
                localctx = WangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(WangParser.ID)
                pass
            elif token in [WangParser.T__0]:
                localctx = WangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(WangParser.T__0)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(WangParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = WangParser.AndExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        localctx.op = self.match(WangParser.AND)
                        self.state = 56
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = WangParser.OrExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        localctx.op = self.match(WangParser.OR)
                        self.state = 59
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = WangParser.BiconditionalExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 61
                        localctx.op = self.match(WangParser.BICONDITIONAL)
                        self.state = 62
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = WangParser.ImplyExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        localctx.op = self.match(WangParser.IMPLIES)
                        self.state = 65
                        self.expr(3)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




