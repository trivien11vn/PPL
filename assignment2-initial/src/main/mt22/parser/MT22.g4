grammar MT22;
/*
 * Student's name: Nguyen Hoang Tri Vien
 * Student ID: 2015043
 */
@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}

program:  decllist EOF ;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;
vardecl: idlist COLON (ato_typ|arr_typ|auto_typ) SEMI | ID abc expr SEMI;
abc: COMMA ID abc expr COMMA|COLON (ato_typ|arr_typ|auto_typ) ASSIGN;

funcdecl: ID COLON FUNCTION (ato_typ | void_typ |auto_typ | arr_typ) LB paralist RB (INHERIT ID)? funcbody;
paralist: paraprime | ;
paraprime: param COMMA paraprime | param;
param: (INHERIT)? (OUT)? ID COLON (ato_typ|auto_typ|arr_typ);

funcbody: block_stmt;

stmt: assignstmt
	|ifstmt
	|forstmt
	|whilestmt
	|dowhilestmt
	|breakstmt
	|continuestmt
	|returnstmt
	|callstmt
	| block_stmt 
	;
block_stmt: LP xet RP;
xet : xet_stmt xet| ;
xet_stmt: stmt | vardecl;
assignstmt: lhs ASSIGN expr SEMI;
lhs: ID | ID LSB exprprime RSB;
ifstmt: IF LB expr RB stmt (ELSE stmt)?;
forstmt: FOR LB (ID |ID LSB exprprime RSB) ASSIGN expr COMMA expr COMMA expr RB stmt;
whilestmt: WHILE LB expr RB stmt;
dowhilestmt: DO block_stmt WHILE LB expr RB SEMI;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN expr SEMI | RETURN SEMI;
callstmt: ID LB exprlist RB SEMI;

exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;
expr: expr1 CONCATENATION expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL | LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
expr4: expr4 (MULOP | DIVOP | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUBOP expr6 | expr7;
expr7: ID LSB exprprime RSB |expr8;
expr8: literal | ID | callexpr | LB expr RB;
callexpr: ID LB exprlist RB;



//comment
COMMENT_BLOCK  : '/*' .*? '*/' -> skip;
COMMENT_LINE: '//' ~ [\r\n]* ('\r'? '\n' | EOF) -> skip ;

/*-------------------Type-------------------*/

//types
arr_typ: 'array' LSB INT_LITERAL (COMMA INT_LITERAL)* RSB OF ato_typ;
ato_typ: int_typ| float_typ| bool_typ| string_typ;

int_typ: INTEGER;
float_typ: FLOAT;
bool_typ: BOOLEAN;
string_typ: STRING;
void_typ: VOID;
auto_typ: AUTO;




// Keywords
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

//operator
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';	
CONCATENATION: '::';


//separator
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
ASSIGN: '=';

//literal
idlist: ID COMMA idlist | ID;
ID: [a-zA-Z_] [a-zA-Z0-9_]*; 
literal: INT_LITERAL | REAL_LITERAL | bool_literal | STRING_LITERAL | array_literal;
INT_LITERAL : INTT {self.text = self.text.replace('_','')};
REAL_LITERAL: INTT DEC {self.text = self.text.replace('_','')} 
			| INTT DEC? EXPO {self.text = self.text.replace('_','')}
			| DEC EXPO {self.text = self.text.replace('_','')};
bool_literal: TRUE | FALSE;

STRING_LITERAL: '"' CHAR* '"'
{
	temp = str(self.text)
	self.text = temp[1:-1]
};
fragment CHAR: ESC | ~ [\r\n\\"];
fragment ESC: '\\' ([btnfr"\\']);
fragment ILL_ESC: '\\' ~([btnfr"\\']) | ~'\\';


array_literal: LP (expr (COMMA expr)*)? RP;


fragment INTT: '0' | [1-9][0-9]* | [1-9][0-9]* ('_' [0-9]+)+;
fragment DEC: DOT [0-9]*;
fragment EXPO: [eE] [-+]? [0-9]+;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



UNCLOSE_STRING: '"' CHAR* ([\r\nEOF] | ~'"')
{
	err_char = ['\r','\n',EOFError]
	if self.text[-1] in err_char:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' CHAR* ILL_ESC
{
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: .
{
	raise ErrorToken(self.text)
};