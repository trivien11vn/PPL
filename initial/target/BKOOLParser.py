# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u008d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3,\n\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\5\5\65\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\5\bC\n\b\3\t\3\t\3\t\3\t\3\t\5\tJ\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\nQ\n\n\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("X\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f`\n\f\f\f\16\fc\13\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\7\rk\n\r\f\r\16\rn\13\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16u\n\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17|\n\17\3\20\3\20\5\20\u0080\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0087\n\21\3\22\3\22\3\22\3\22\3\22\2")
        buf.write("\4\26\30\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("\2\4\3\2\23\24\3\2\20\22\2\u008a\2$\3\2\2\2\4+\3\2\2\2")
        buf.write("\6-\3\2\2\2\b\64\3\2\2\2\n\66\3\2\2\2\f;\3\2\2\2\16B\3")
        buf.write("\2\2\2\20I\3\2\2\2\22P\3\2\2\2\24W\3\2\2\2\26Y\3\2\2\2")
        buf.write("\30d\3\2\2\2\32t\3\2\2\2\34{\3\2\2\2\36\177\3\2\2\2 \u0086")
        buf.write("\3\2\2\2\"\u0088\3\2\2\2$%\5\4\3\2%&\7\2\2\3&\3\3\2\2")
        buf.write("\2\'(\5\6\4\2()\5\4\3\2),\3\2\2\2*,\5\6\4\2+\'\3\2\2\2")
        buf.write("+*\3\2\2\2,\5\3\2\2\2-.\7\3\2\2./\7\f\2\2/\60\5\22\n\2")
        buf.write("\60\61\7\r\2\2\61\7\3\2\2\2\62\65\5\n\6\2\63\65\5\f\7")
        buf.write("\2\64\62\3\2\2\2\64\63\3\2\2\2\65\t\3\2\2\2\66\67\7\7")
        buf.write("\2\2\678\7\b\2\289\5\16\b\29:\7\t\2\2:\13\3\2\2\2;<\7")
        buf.write("\7\2\2<=\7\b\2\2=>\5\36\20\2>?\7\t\2\2?\r\3\2\2\2@C\5")
        buf.write("\20\t\2AC\3\2\2\2B@\3\2\2\2BA\3\2\2\2C\17\3\2\2\2DE\5")
        buf.write("\22\n\2EF\7\n\2\2FG\5\20\t\2GJ\3\2\2\2HJ\5\22\n\2ID\3")
        buf.write("\2\2\2IH\3\2\2\2J\21\3\2\2\2KL\5\24\13\2LM\7\25\2\2MN")
        buf.write("\5\24\13\2NQ\3\2\2\2OQ\5\24\13\2PK\3\2\2\2PO\3\2\2\2Q")
        buf.write("\23\3\2\2\2RS\5\26\f\2ST\t\2\2\2TU\5\24\13\2UX\3\2\2\2")
        buf.write("VX\5\26\f\2WR\3\2\2\2WV\3\2\2\2X\25\3\2\2\2YZ\b\f\1\2")
        buf.write("Z[\5\30\r\2[a\3\2\2\2\\]\f\4\2\2]^\t\3\2\2^`\5\30\r\2")
        buf.write("_\\\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\27\3\2\2\2")
        buf.write("ca\3\2\2\2de\b\r\1\2ef\5\32\16\2fl\3\2\2\2gh\f\4\2\2h")
        buf.write("i\7\17\2\2ik\5\32\16\2jg\3\2\2\2kn\3\2\2\2lj\3\2\2\2l")
        buf.write("m\3\2\2\2m\31\3\2\2\2nl\3\2\2\2op\5\34\17\2pq\7\16\2\2")
        buf.write("qr\5\32\16\2ru\3\2\2\2su\5\34\17\2to\3\2\2\2ts\3\2\2\2")
        buf.write("u\33\3\2\2\2v|\7\3\2\2w|\7\4\2\2x|\7\5\2\2y|\7\6\2\2z")
        buf.write("|\5\b\5\2{v\3\2\2\2{w\3\2\2\2{x\3\2\2\2{y\3\2\2\2{z\3")
        buf.write("\2\2\2|\35\3\2\2\2}\u0080\5 \21\2~\u0080\3\2\2\2\177}")
        buf.write("\3\2\2\2\177~\3\2\2\2\u0080\37\3\2\2\2\u0081\u0082\5\"")
        buf.write("\22\2\u0082\u0083\7\n\2\2\u0083\u0084\5 \21\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0087\5\"\22\2\u0086\u0081\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087!\3\2\2\2\u0088\u0089\7\3\2\2\u0089")
        buf.write("\u008a\7\13\2\2\u008a\u008b\5\22\n\2\u008b#\3\2\2\2\16")
        buf.write("+\64BIPWalt{\177\u0086")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'array'", "'('", "')'", "','", "'=>'", 
                     "'='", "';'", "'**'", "'.'", "'*'", "'/'", "'%'", "'+'", 
                     "'-'", "'??'" ]

    symbolicNames = [ "<INVALID>", "VARNAME", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "ARRAY", "LP", "RP", "COMMA", "ARROW", "EQ", "SEMI", 
                      "DSTAR", "DOT", "MUL", "DIV", "MOD", "ADD", "SUB", 
                      "DQUES", "ID", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_vardecllist = 1
    RULE_vardecl = 2
    RULE_arr_type = 3
    RULE_arr_item = 4
    RULE_arr_asso = 5
    RULE_exprlist = 6
    RULE_exprprime = 7
    RULE_expr = 8
    RULE_expr1 = 9
    RULE_expr2 = 10
    RULE_expr3 = 11
    RULE_expr4 = 12
    RULE_expr5 = 13
    RULE_pairlist = 14
    RULE_pairprime = 15
    RULE_pair = 16

    ruleNames =  [ "program", "vardecllist", "vardecl", "arr_type", "arr_item", 
                   "arr_asso", "exprlist", "exprprime", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "pairlist", "pairprime", 
                   "pair" ]

    EOF = Token.EOF
    VARNAME=1
    INTLIT=2
    FLOATLIT=3
    STRINGLIT=4
    ARRAY=5
    LP=6
    RP=7
    COMMA=8
    ARROW=9
    EQ=10
    SEMI=11
    DSTAR=12
    DOT=13
    MUL=14
    DIV=15
    MOD=16
    ADD=17
    SUB=18
    DQUES=19
    ID=20
    WS=21
    ERROR_CHAR=22
    ILLEGAL_ESCAPE=23
    UNCLOSE_STRING=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecllist(self):
            return self.getTypedRuleContext(BKOOLParser.VardecllistContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.vardecllist()
            self.state = 35
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def vardecllist(self):
            return self.getTypedRuleContext(BKOOLParser.VardecllistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecllist" ):
                return visitor.visitVardecllist(self)
            else:
                return visitor.visitChildren(self)




    def vardecllist(self):

        localctx = BKOOLParser.VardecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecllist)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.vardecl()
                self.state = 38
                self.vardecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(BKOOLParser.VARNAME, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(BKOOLParser.VARNAME)
            self.state = 44
            self.match(BKOOLParser.EQ)
            self.state = 45
            self.expr()
            self.state = 46
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_item(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_itemContext,0)


        def arr_asso(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_assoContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = BKOOLParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arr_type)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.arr_item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.arr_asso()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKOOLParser.ARRAY, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_item" ):
                return visitor.visitArr_item(self)
            else:
                return visitor.visitChildren(self)




    def arr_item(self):

        localctx = BKOOLParser.Arr_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arr_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(BKOOLParser.ARRAY)
            self.state = 53
            self.match(BKOOLParser.LP)
            self.state = 54
            self.exprlist()
            self.state = 55
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_assoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKOOLParser.ARRAY, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def pairlist(self):
            return self.getTypedRuleContext(BKOOLParser.PairlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_asso

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_asso" ):
                return visitor.visitArr_asso(self)
            else:
                return visitor.visitChildren(self)




    def arr_asso(self):

        localctx = BKOOLParser.Arr_assoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arr_asso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(BKOOLParser.ARRAY)
            self.state = 58
            self.match(BKOOLParser.LP)
            self.state = 59
            self.pairlist()
            self.state = 60
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprlist)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.VARNAME, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.exprprime()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = BKOOLParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exprprime)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.expr()
                self.state = 67
                self.match(BKOOLParser.COMMA)
                self.state = 68
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def DQUES(self):
            return self.getToken(BKOOLParser.DQUES, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.expr1()
                self.state = 74
                self.match(BKOOLParser.DQUES)
                self.state = 75
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.expr2(0)
                self.state = 81
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 82
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 90
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 91
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 92
                    self.expr3(0) 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 101
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 102
                    self.match(BKOOLParser.DOT)
                    self.state = 103
                    self.expr4() 
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def DSTAR(self):
            return self.getToken(BKOOLParser.DSTAR, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = BKOOLParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr4)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.expr5()
                self.state = 110
                self.match(BKOOLParser.DSTAR)
                self.state = 111
                self.expr4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(BKOOLParser.VARNAME, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arr_type(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = BKOOLParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr5)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.VARNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(BKOOLParser.VARNAME)
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.arr_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pairprime(self):
            return self.getTypedRuleContext(BKOOLParser.PairprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_pairlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairlist" ):
                return visitor.visitPairlist(self)
            else:
                return visitor.visitChildren(self)




    def pairlist(self):

        localctx = BKOOLParser.PairlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_pairlist)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.VARNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.pairprime()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self):
            return self.getTypedRuleContext(BKOOLParser.PairContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def pairprime(self):
            return self.getTypedRuleContext(BKOOLParser.PairprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_pairprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairprime" ):
                return visitor.visitPairprime(self)
            else:
                return visitor.visitChildren(self)




    def pairprime(self):

        localctx = BKOOLParser.PairprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pairprime)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.pair()
                self.state = 128
                self.match(BKOOLParser.COMMA)
                self.state = 129
                self.pairprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.pair()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(BKOOLParser.VARNAME, 0)

        def ARROW(self):
            return self.getToken(BKOOLParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = BKOOLParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKOOLParser.VARNAME)
            self.state = 135
            self.match(BKOOLParser.ARROW)
            self.state = 136
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr2_sempred
        self._predicates[11] = self.expr3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




