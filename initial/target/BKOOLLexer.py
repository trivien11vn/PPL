# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0088\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\7\2\66\n\2\f\2\16\29\13\2\3\3\6\3<")
        buf.write("\n\3\r\3\16\3=\3\4\6\4A\n\4\r\4\16\4B\3\4\3\4\6\4G\n\4")
        buf.write("\r\4\16\4H\3\5\3\5\7\5M\n\5\f\5\16\5P\13\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\6\25z\n\25\r\25\16\25{\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\2\2\32\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\3\2\6\4")
        buf.write("\2C\\c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\16\17\"\"\2\u008d")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\3\63\3\2\2\2\5;\3\2\2\2\7@\3")
        buf.write("\2\2\2\tJ\3\2\2\2\13S\3\2\2\2\rY\3\2\2\2\17[\3\2\2\2\21")
        buf.write("]\3\2\2\2\23_\3\2\2\2\25b\3\2\2\2\27d\3\2\2\2\31f\3\2")
        buf.write("\2\2\33i\3\2\2\2\35k\3\2\2\2\37m\3\2\2\2!o\3\2\2\2#q\3")
        buf.write("\2\2\2%s\3\2\2\2\'u\3\2\2\2)y\3\2\2\2+}\3\2\2\2-\u0081")
        buf.write("\3\2\2\2/\u0084\3\2\2\2\61\u0086\3\2\2\2\63\67\t\2\2\2")
        buf.write("\64\66\t\3\2\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2")
        buf.write("\678\3\2\2\28\4\3\2\2\29\67\3\2\2\2:<\t\4\2\2;:\3\2\2")
        buf.write("\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\6\3\2\2\2?A\t\4\2\2")
        buf.write("@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2DF\7")
        buf.write("\60\2\2EG\t\4\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2")
        buf.write("\2\2I\b\3\2\2\2JN\7$\2\2KM\13\2\2\2LK\3\2\2\2MP\3\2\2")
        buf.write("\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\7$\2\2R\n")
        buf.write("\3\2\2\2ST\7c\2\2TU\7t\2\2UV\7t\2\2VW\7c\2\2WX\7{\2\2")
        buf.write("X\f\3\2\2\2YZ\7*\2\2Z\16\3\2\2\2[\\\7+\2\2\\\20\3\2\2")
        buf.write("\2]^\7.\2\2^\22\3\2\2\2_`\7?\2\2`a\7@\2\2a\24\3\2\2\2")
        buf.write("bc\7?\2\2c\26\3\2\2\2de\7=\2\2e\30\3\2\2\2fg\7,\2\2gh")
        buf.write("\7,\2\2h\32\3\2\2\2ij\7\60\2\2j\34\3\2\2\2kl\7,\2\2l\36")
        buf.write("\3\2\2\2mn\7\61\2\2n \3\2\2\2op\7\'\2\2p\"\3\2\2\2qr\7")
        buf.write("-\2\2r$\3\2\2\2st\7/\2\2t&\3\2\2\2uv\7A\2\2vw\7A\2\2w")
        buf.write("(\3\2\2\2xz\t\2\2\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3")
        buf.write("\2\2\2|*\3\2\2\2}~\t\5\2\2~\177\3\2\2\2\177\u0080\b\26")
        buf.write("\2\2\u0080,\3\2\2\2\u0081\u0082\13\2\2\2\u0082\u0083\b")
        buf.write("\27\3\2\u0083.\3\2\2\2\u0084\u0085\13\2\2\2\u0085\60\3")
        buf.write("\2\2\2\u0086\u0087\13\2\2\2\u0087\62\3\2\2\2\t\2\67=B")
        buf.write("HN{\4\b\2\2\3\27\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VARNAME = 1
    INTLIT = 2
    FLOATLIT = 3
    STRINGLIT = 4
    ARRAY = 5
    LP = 6
    RP = 7
    COMMA = 8
    ARROW = 9
    EQ = 10
    SEMI = 11
    DSTAR = 12
    DOT = 13
    MUL = 14
    DIV = 15
    MOD = 16
    ADD = 17
    SUB = 18
    DQUES = 19
    ID = 20
    WS = 21
    ERROR_CHAR = 22
    ILLEGAL_ESCAPE = 23
    UNCLOSE_STRING = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'('", "')'", "','", "'=>'", "'='", "';'", "'**'", 
            "'.'", "'*'", "'/'", "'%'", "'+'", "'-'", "'??'" ]

    symbolicNames = [ "<INVALID>",
            "VARNAME", "INTLIT", "FLOATLIT", "STRINGLIT", "ARRAY", "LP", 
            "RP", "COMMA", "ARROW", "EQ", "SEMI", "DSTAR", "DOT", "MUL", 
            "DIV", "MOD", "ADD", "SUB", "DQUES", "ID", "WS", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "VARNAME", "INTLIT", "FLOATLIT", "STRINGLIT", "ARRAY", 
                  "LP", "RP", "COMMA", "ARROW", "EQ", "SEMI", "DSTAR", "DOT", 
                  "MUL", "DIV", "MOD", "ADD", "SUB", "DQUES", "ID", "WS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[21] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	raise ErrorToken(self.text);

     


