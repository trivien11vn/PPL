# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01d4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\7")
        buf.write("\2\u0086\n\2\f\2\16\2\u0089\13\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3\u0094\n\3\f\3\16\3\u0097\13\3\3\3\5")
        buf.write("\3\u009a\n\3\3\3\3\3\5\3\u009e\n\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\7\63\u015a\n\63\f\63\16")
        buf.write("\63\u015d\13\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u0168\n\65\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\5\65\u0171\n\65\3\66\3\66\7\66\u0175\n\66\f\66\16")
        buf.write("\66\u0178\13\66\3\66\3\66\3\66\3\67\3\67\5\67\u017f\n")
        buf.write("\67\38\38\38\39\39\39\59\u0187\n9\3:\3:\3:\7:\u018c\n")
        buf.write(":\f:\16:\u018f\13:\3:\3:\7:\u0193\n:\f:\16:\u0196\13:")
        buf.write("\3:\3:\6:\u019a\n:\r:\16:\u019b\6:\u019e\n:\r:\16:\u019f")
        buf.write("\5:\u01a2\n:\3;\3;\7;\u01a6\n;\f;\16;\u01a9\13;\3<\3<")
        buf.write("\5<\u01ad\n<\3<\6<\u01b0\n<\r<\16<\u01b1\3=\6=\u01b5\n")
        buf.write("=\r=\16=\u01b6\3=\3=\3>\3>\7>\u01bd\n>\f>\16>\u01c0\13")
        buf.write(">\3>\3>\5>\u01c4\n>\3>\3>\3?\3?\7?\u01ca\n?\f?\16?\u01cd")
        buf.write("\13?\3?\3?\3?\3@\3@\3@\3\u0087\2A\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w\2y8{9}:\177;")
        buf.write("\3\2\17\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\6\2\f")
        buf.write("\f\17\17$$^^\n\2$$))^^ddhhppttvv\3\2^^\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\6\2\f\f\17\17GHQ")
        buf.write("Q\3\2$$\2\u01e5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2")
        buf.write("\5\u008f\3\2\2\2\7\u00a1\3\2\2\2\t\u00a6\3\2\2\2\13\u00ac")
        buf.write("\3\2\2\2\r\u00b4\3\2\2\2\17\u00b7\3\2\2\2\21\u00bc\3\2")
        buf.write("\2\2\23\u00c2\3\2\2\2\25\u00c8\3\2\2\2\27\u00cc\3\2\2")
        buf.write("\2\31\u00d5\3\2\2\2\33\u00d8\3\2\2\2\35\u00e0\3\2\2\2")
        buf.write("\37\u00e7\3\2\2\2!\u00ee\3\2\2\2#\u00f3\3\2\2\2%\u00f9")
        buf.write("\3\2\2\2\'\u00fe\3\2\2\2)\u0102\3\2\2\2+\u010b\3\2\2\2")
        buf.write("-\u010e\3\2\2\2/\u0116\3\2\2\2\61\u011c\3\2\2\2\63\u011e")
        buf.write("\3\2\2\2\65\u0120\3\2\2\2\67\u0122\3\2\2\29\u0124\3\2")
        buf.write("\2\2;\u0126\3\2\2\2=\u0128\3\2\2\2?\u012b\3\2\2\2A\u012e")
        buf.write("\3\2\2\2C\u0131\3\2\2\2E\u0134\3\2\2\2G\u0136\3\2\2\2")
        buf.write("I\u0139\3\2\2\2K\u013b\3\2\2\2M\u013e\3\2\2\2O\u0141\3")
        buf.write("\2\2\2Q\u0143\3\2\2\2S\u0145\3\2\2\2U\u0147\3\2\2\2W\u0149")
        buf.write("\3\2\2\2Y\u014b\3\2\2\2[\u014d\3\2\2\2]\u014f\3\2\2\2")
        buf.write("_\u0151\3\2\2\2a\u0153\3\2\2\2c\u0155\3\2\2\2e\u0157\3")
        buf.write("\2\2\2g\u015e\3\2\2\2i\u0170\3\2\2\2k\u0172\3\2\2\2m\u017e")
        buf.write("\3\2\2\2o\u0180\3\2\2\2q\u0186\3\2\2\2s\u01a1\3\2\2\2")
        buf.write("u\u01a3\3\2\2\2w\u01aa\3\2\2\2y\u01b4\3\2\2\2{\u01ba\3")
        buf.write("\2\2\2}\u01c7\3\2\2\2\177\u01d1\3\2\2\2\u0081\u0082\7")
        buf.write("\61\2\2\u0082\u0083\7,\2\2\u0083\u0087\3\2\2\2\u0084\u0086")
        buf.write("\13\2\2\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u008a\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u008a\u008b\7,\2\2\u008b\u008c\7")
        buf.write("\61\2\2\u008c\u008d\3\2\2\2\u008d\u008e\b\2\2\2\u008e")
        buf.write("\4\3\2\2\2\u008f\u0090\7\61\2\2\u0090\u0091\7\61\2\2\u0091")
        buf.write("\u0095\3\2\2\2\u0092\u0094\n\2\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u009d\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a")
        buf.write("\7\17\2\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009e\7\f\2\2\u009c\u009e\7\2\2\3")
        buf.write("\u009d\u0099\3\2\2\2\u009d\u009c\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f\u00a0\b\3\2\2\u00a0\6\3\2\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\b\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7m\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7d\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7p\2\2\u00b3\f")
        buf.write("\3\2\2\2\u00b4\u00b5\7f\2\2\u00b5\u00b6\7q\2\2\u00b6\16")
        buf.write("\3\2\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7g\2\2\u00bb\20\3\2\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00c1\7g\2\2\u00c1\22\3\2\2\2\u00c2\u00c3")
        buf.write("\7h\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7v\2\2\u00c7\24\3\2\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7t\2\2\u00cb\26")
        buf.write("\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7p\2\2\u00d4\30")
        buf.write("\3\2\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7h\2\2\u00d7\32")
        buf.write("\3\2\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7i\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7t\2\2\u00df\34\3\2\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7w\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7p\2\2\u00e6\36")
        buf.write("\3\2\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7i\2\2\u00ed \3\2\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7g\2\2\u00f2\"")
        buf.write("\3\2\2\2\u00f3\u00f4\7y\2\2\u00f4\u00f5\7j\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7g\2\2\u00f8$\3")
        buf.write("\2\2\2\u00f9\u00fa\7x\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7f\2\2\u00fd&\3\2\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7w\2\2\u0100\u0101\7v\2\2\u0101(\3")
        buf.write("\2\2\2\u0102\u0103\7e\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7v\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7w\2\2\u0109\u010a\7g\2\2\u010a*\3")
        buf.write("\2\2\2\u010b\u010c\7q\2\2\u010c\u010d\7h\2\2\u010d,\3")
        buf.write("\2\2\2\u010e\u010f\7k\2\2\u010f\u0110\7p\2\2\u0110\u0111")
        buf.write("\7j\2\2\u0111\u0112\7g\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7v\2\2\u0115.\3\2\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7t\2\2\u0118\u0119\7t\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7{\2\2\u011b\60\3\2\2\2\u011c\u011d")
        buf.write("\7-\2\2\u011d\62\3\2\2\2\u011e\u011f\7/\2\2\u011f\64\3")
        buf.write("\2\2\2\u0120\u0121\7,\2\2\u0121\66\3\2\2\2\u0122\u0123")
        buf.write("\7\61\2\2\u01238\3\2\2\2\u0124\u0125\7\'\2\2\u0125:\3")
        buf.write("\2\2\2\u0126\u0127\7#\2\2\u0127<\3\2\2\2\u0128\u0129\7")
        buf.write("(\2\2\u0129\u012a\7(\2\2\u012a>\3\2\2\2\u012b\u012c\7")
        buf.write("~\2\2\u012c\u012d\7~\2\2\u012d@\3\2\2\2\u012e\u012f\7")
        buf.write("?\2\2\u012f\u0130\7?\2\2\u0130B\3\2\2\2\u0131\u0132\7")
        buf.write("#\2\2\u0132\u0133\7?\2\2\u0133D\3\2\2\2\u0134\u0135\7")
        buf.write(">\2\2\u0135F\3\2\2\2\u0136\u0137\7>\2\2\u0137\u0138\7")
        buf.write("?\2\2\u0138H\3\2\2\2\u0139\u013a\7@\2\2\u013aJ\3\2\2\2")
        buf.write("\u013b\u013c\7@\2\2\u013c\u013d\7?\2\2\u013dL\3\2\2\2")
        buf.write("\u013e\u013f\7<\2\2\u013f\u0140\7<\2\2\u0140N\3\2\2\2")
        buf.write("\u0141\u0142\7*\2\2\u0142P\3\2\2\2\u0143\u0144\7+\2\2")
        buf.write("\u0144R\3\2\2\2\u0145\u0146\7}\2\2\u0146T\3\2\2\2\u0147")
        buf.write("\u0148\7\177\2\2\u0148V\3\2\2\2\u0149\u014a\7]\2\2\u014a")
        buf.write("X\3\2\2\2\u014b\u014c\7_\2\2\u014cZ\3\2\2\2\u014d\u014e")
        buf.write("\7=\2\2\u014e\\\3\2\2\2\u014f\u0150\7<\2\2\u0150^\3\2")
        buf.write("\2\2\u0151\u0152\7.\2\2\u0152`\3\2\2\2\u0153\u0154\7\60")
        buf.write("\2\2\u0154b\3\2\2\2\u0155\u0156\7?\2\2\u0156d\3\2\2\2")
        buf.write("\u0157\u015b\t\3\2\2\u0158\u015a\t\4\2\2\u0159\u0158\3")
        buf.write("\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015cf\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f")
        buf.write("\5s:\2\u015f\u0160\b\64\3\2\u0160h\3\2\2\2\u0161\u0162")
        buf.write("\5s:\2\u0162\u0163\5u;\2\u0163\u0164\b\65\4\2\u0164\u0171")
        buf.write("\3\2\2\2\u0165\u0167\5s:\2\u0166\u0168\5u;\2\u0167\u0166")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016a\5w<\2\u016a\u016b\b\65\5\2\u016b\u0171\3\2\2\2")
        buf.write("\u016c\u016d\5u;\2\u016d\u016e\5w<\2\u016e\u016f\b\65")
        buf.write("\6\2\u016f\u0171\3\2\2\2\u0170\u0161\3\2\2\2\u0170\u0165")
        buf.write("\3\2\2\2\u0170\u016c\3\2\2\2\u0171j\3\2\2\2\u0172\u0176")
        buf.write("\7$\2\2\u0173\u0175\5m\67\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u0179\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\7")
        buf.write("$\2\2\u017a\u017b\b\66\7\2\u017bl\3\2\2\2\u017c\u017f")
        buf.write("\5o8\2\u017d\u017f\n\5\2\2\u017e\u017c\3\2\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017fn\3\2\2\2\u0180\u0181\7^\2\2\u0181\u0182")
        buf.write("\t\6\2\2\u0182p\3\2\2\2\u0183\u0184\7^\2\2\u0184\u0187")
        buf.write("\n\6\2\2\u0185\u0187\n\7\2\2\u0186\u0183\3\2\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187r\3\2\2\2\u0188\u01a2\7\62\2\2\u0189")
        buf.write("\u018d\t\b\2\2\u018a\u018c\t\t\2\2\u018b\u018a\3\2\2\2")
        buf.write("\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u01a2\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0194")
        buf.write("\t\b\2\2\u0191\u0193\t\t\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u019d\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0199\7")
        buf.write("a\2\2\u0198\u019a\t\t\2\2\u0199\u0198\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019e\3\2\2\2\u019d\u0197\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u0188\3\2\2\2\u01a1\u0189\3\2\2\2\u01a1\u0190")
        buf.write("\3\2\2\2\u01a2t\3\2\2\2\u01a3\u01a7\5a\61\2\u01a4\u01a6")
        buf.write("\t\t\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8v\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01aa\u01ac\t\n\2\2\u01ab\u01ad\t\13\2")
        buf.write("\2\u01ac\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af")
        buf.write("\3\2\2\2\u01ae\u01b0\t\t\2\2\u01af\u01ae\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2x\3\2\2\2\u01b3\u01b5\t\f\2\2\u01b4\u01b3\3\2\2")
        buf.write("\2\u01b5\u01b6\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\b=\2\2\u01b9")
        buf.write("z\3\2\2\2\u01ba\u01be\7$\2\2\u01bb\u01bd\5m\67\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c3\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c1\u01c4\t\r\2\2\u01c2\u01c4\n\16\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c6\b>\b\2\u01c6|\3\2\2\2\u01c7\u01cb\7$\2\2")
        buf.write("\u01c8\u01ca\5m\67\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3")
        buf.write("\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce")
        buf.write("\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\5q9\2\u01cf\u01d0")
        buf.write("\b?\t\2\u01d0~\3\2\2\2\u01d1\u01d2\13\2\2\2\u01d2\u01d3")
        buf.write("\b@\n\2\u01d3\u0080\3\2\2\2\31\2\u0087\u0095\u0099\u009d")
        buf.write("\u015b\u0167\u0170\u0176\u017e\u0186\u018d\u0194\u019b")
        buf.write("\u019f\u01a1\u01a7\u01ac\u01b1\u01b6\u01be\u01c3\u01cb")
        buf.write("\13\b\2\2\3\64\2\3\65\3\3\65\4\3\65\5\3\66\6\3>\7\3?\b")
        buf.write("\3@\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_BLOCK = 1
    COMMENT_LINE = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FALSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    INHERIT = 22
    ARRAY = 23
    ADDOP = 24
    SUBOP = 25
    MULOP = 26
    DIVOP = 27
    MOD = 28
    NOT = 29
    AND = 30
    OR = 31
    EQUAL = 32
    NOT_EQUAL = 33
    LESS = 34
    LESS_OR_EQUAL = 35
    GREATER = 36
    GREATER_OR_EQUAL = 37
    CONCATENATION = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    LSB = 43
    RSB = 44
    SEMI = 45
    COLON = 46
    COMMA = 47
    DOT = 48
    ASSIGN = 49
    ID = 50
    INT_LITERAL = 51
    REAL_LITERAL = 52
    STRING_LITERAL = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "':'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_BLOCK", "COMMENT_LINE", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "CONCATENATION", "LB", "RB", 
            "LP", "RP", "LSB", "RSB", "SEMI", "COLON", "COMMA", "DOT", "ASSIGN", 
            "ID", "INT_LITERAL", "REAL_LITERAL", "STRING_LITERAL", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT_BLOCK", "COMMENT_LINE", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
                  "GREATER_OR_EQUAL", "CONCATENATION", "LB", "RB", "LP", 
                  "RP", "LSB", "RSB", "SEMI", "COLON", "COMMA", "DOT", "ASSIGN", 
                  "ID", "INT_LITERAL", "REAL_LITERAL", "STRING_LITERAL", 
                  "CHAR", "ESC", "ILL_ESC", "INTT", "DEC", "EXPO", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INT_LITERAL_action 
            actions[51] = self.REAL_LITERAL_action 
            actions[52] = self.STRING_LITERAL_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def REAL_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	temp = str(self.text)
            	self.text = temp[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	raise ErrorToken(self.text)

     


