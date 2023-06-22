grammar BKIT;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


program: vardecllist EOF ;
vardecllist: vardecl vardecllist | vardecl;
vardecl: VARNAME EQ expr SEMI;
arr_type: arr_item | arr_asso;
arr_item: ARRAY LP exprlist RP;
arr_asso: ARRAY LP pairlist RP;

exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;
expr: expr1 DQUES expr1 | expr1;
expr1: expr2 (ADD|SUB) expr1 | expr2;
expr2: expr2 (MUL|DIV|MOD) expr3 | expr3;
expr3: expr3 DOT expr4 | expr4;
expr4: expr5 DSTAR expr4 | expr5;
expr5: VARNAME | INTLIT | FLOATLIT | STRINGLIT | arr_type ;
pairlist: pairprime | ;
pairprime: pair COMMA pairprime | pair;
pair: VARNAME ARROW expr;
VARNAME : [a-zA-Z][a-zA-Z0-9]* ;
INTLIT  : [0-9]+ ;                // integer literal
FLOATLIT: [0-9]+ '.' [0-9]+ ;  
STRINGLIT: '"' .* '"';

ARRAY: 'array' ; 
LP: '(' ;                         // left parenthesis
RP: ')' ;                         // right parenthesis
COMMA: ',' ;                      // comma
ARROW: '=>' ;                     // arrow symbol
EQ: '=' ;                         // equal sign
SEMI: ';' ;                       // semicolon
DSTAR: '**' ;                     // double star operator
DOT: '.' ;                        // dot operator
MUL: '*' ;                        // multiplication operator
DIV: '/' ;                        // division operator
MOD: '%' ;                        // modulo operator
ADD: '+' ;                        // addition operator
SUB: '-' ;                        // subtraction operator
DQUES: '??' ; 

ID: [a-zA-Z]+;
WS: [ \t\n\f\r] -> skip;
ERROR_CHAR: .{
	raise ErrorToken(self.text);
};
ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;
