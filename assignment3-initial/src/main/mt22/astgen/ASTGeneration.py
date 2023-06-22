from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        #program:  decllist EOF ;
        return Program(ctx.decllist().accept(self))
    
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        #decllist: decl decllist | decl;
        if ctx.getChildCount() == 1:
            return ctx.decl().accept(self)
        else:
            return ctx.decl().accept(self) + ctx.decllist().accept(self)
    
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        #decl: vardecl | funcdecl;
        if ctx.vardecl():
            return ctx.vardecl().accept(self)
        else:
            return ctx.funcdecl().accept(self)
    
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        #vardecl: idlist COLON (ato_typ|arr_typ|auto_typ) SEMI | ID abc expr SEMI;
        if ctx.idlist():
            if ctx.ato_typ(): 
                typ = ctx.ato_typ().accept(self)
                ids = ctx.idlist().accept(self)
                return [VarDecl(x,typ) for x in ids]
            elif ctx.arr_typ():
                typ = ctx.arr_typ().accept(self)
                ids = ctx.idlist().accept(self)
                return [VarDecl(x,typ) for x in ids]
            else: 
                typ = ctx.auto_typ().accept(self)
                ids = ctx.idlist().accept(self)
                return [VarDecl(x,typ) for x in ids] 
        else:
            idlistt = [ctx.ID().getText()]
            abc = ctx.abc().accept(self)
            exprlistt = []
            if len(abc) == 1:
                typ = abc[0]
                return [VarDecl(x,typ,y) for x in idlistt for y in [ctx.expr().accept(self)]] 
            else:
                x=len(abc)
                a= int(x/2)
                typ = abc[a]
                for i in range(0,x):
                    if i < a:
                        idlistt+= [abc[i]]
                    elif i > a:
                        exprlistt += [abc[i]]
                exprlistt += [ctx.expr().accept(self)]
                return [VarDecl(idlistt[i],typ,exprlistt[i]) for i in range(0,len(idlistt))] 
                    
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        #idlist: ID COMMA idlist | ID;
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()] + ctx.idlist().accept(self)
    
    def visitAbc(self, ctx:MT22Parser.AbcContext):
        #abc: COMMA ID abc expr COMMA|COLON (ato_typ|arr_typ|auto_typ) ASSIGN;
        if ctx.COMMA():
            return [ctx.ID().getText()] + ctx.abc().accept(self) + [ctx.expr().accept(self)]
        
        elif ctx.COLON():
            if ctx.ato_typ():
                return [ctx.ato_typ().accept(self)]
            elif ctx.arr_typ():
                return [ctx.arr_typ().accept(self)]
            elif ctx.auto_typ():
                return [ctx.auto_typ().accept(self)]
    
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        #funcdecl: ID COLON FUNCTION (ato_typ | void_typ |auto_typ | arr_typ) LB paralist RB (INHERIT ID)? funcbody;
        id = ctx.ID(0).getText()
        if ctx.ato_typ(): typ=ctx.ato_typ().accept(self)
        elif ctx.void_typ(): typ=ctx.void_typ().accept(self)
        elif ctx.auto_typ(): typ=ctx.auto_typ().accept(self)
        elif ctx.arr_typ(): typ=ctx.arr_typ().accept(self)
        param = ctx.paralist().accept(self)
        body=ctx.funcbody().accept(self)
        if ctx.INHERIT(): return [FuncDecl(id,typ,param,ctx.ID(1).getText(),body)]
        else: return [FuncDecl(id,typ,param,None,body)]

    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        #paralist: paraprime | ;
        if ctx.getChildCount() == 0:
            return []
        elif ctx.getChildCount() == 1:
            return ctx.paraprime().accept(self)
    
    def visitParaprime(self, ctx:MT22Parser.ParaprimeContext):
        #paraprime: param COMMA paraprime | param;
        if ctx.getChildCount() == 1:
            return [ctx.param().accept(self)]
        elif ctx.getChildCount() == 3:
            return [ctx.param().accept(self)]+ ctx.paraprime().accept(self)
        
    def visitParam(self, ctx:MT22Parser.ParamContext):
        #param: (INHERIT)? (OUT)? ID COLON (ato_typ|auto_typ|arr_typ);
        if ctx.INHERIT():
            inheritt = True
        else: inheritt = False
        if ctx.OUT():
            outt = True
        else: outt = False
        id  = ctx.ID().getText()
        if ctx.ato_typ(): typ=ctx.ato_typ().accept(self)
        elif ctx.auto_typ(): typ=ctx.auto_typ().accept(self)
        elif ctx.arr_typ(): typ=ctx.arr_typ().accept(self)
        return ParamDecl(id,typ,outt,inheritt)
    
    def visitAto_typ(self, ctx:MT22Parser.Ato_typContext):
        #ato_typ: int_typ| float_typ| bool_typ| string_typ;
        if ctx.int_typ(): return ctx.int_typ().accept(self)
        if ctx.float_typ(): return ctx.float_typ().accept(self)
        if ctx.bool_typ(): return ctx.bool_typ().accept(self)
        if ctx.string_typ(): return ctx.string_typ().accept(self)
    
    def visitAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        #auto_typ: AUTO;
        return AutoType()
    
    def visitVoid_typ(self, ctx:MT22Parser.Void_typContext):
        #void_typ: VOID;
        return VoidType()
    
    def visitInt_typ(self, ctx:MT22Parser.Int_typContext):
        #int_typ: INTEGER;
        return IntegerType()

    def visitFloat_typ(self, ctx:MT22Parser.Float_typContext):
        #float_typ: FLOAT;
        return FloatType()
    def visitBool_typ(self, ctx:MT22Parser.Bool_typContext):
        #bool_typ: BOOLEAN;
        return BooleanType()

    def visitString_typ(self, ctx:MT22Parser.String_typContext):
        #string_typ: STRING;
        return StringType()
    
    def visitArr_typ(self, ctx:MT22Parser.Arr_typContext):
        #arr_typ: 'array' LSB INT_LITERAL (COMMA INT_LITERAL)* RSB OF ato_typ;
        result = []
        result.append(int(ctx.INT_LITERAL(0).getText()))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1,size+1):
                result.append(int(ctx.INT_LITERAL(i).getText()))
        typ = ctx.ato_typ().accept(self)
        return ArrayType(result,typ)

    
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        #dowhilestmt: DO block_stmt WHILE LB expr RB SEMI;
        cond = ctx.expr().accept(self)
        loop = ctx.block_stmt().accept(self)
        return DoWhileStmt(cond, loop)
    
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        #whilestmt: WHILE LB expr RB stmt;
        cond = ctx.expr().accept(self)
        loop = ctx.stmt().accept(self)
        return WhileStmt(cond, loop)
    
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        #callstmt: ID LB exprlist RB SEMI;
        return CallStmt(ctx.ID().getText(),ctx.exprlist().accept(self))
    
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        #exprlist: exprprime | ;
        if ctx.getChildCount() == 0:
            return []
        elif ctx.getChildCount() == 1:
            return ctx.exprprime().accept(self)
    
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        #exprprime: expr COMMA exprprime | expr;
        if ctx.getChildCount() == 1:
            return [ctx.expr().accept(self)]
        elif ctx.getChildCount() == 3:
            return [ctx.expr().accept(self)] + ctx.exprprime().accept(self)
    
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        #expr: expr1 CONCATENATION expr1 | expr1;
        if ctx.getChildCount() == 1:
            return ctx.expr1(0).accept(self)
        else:
            left= ctx.expr1(0).accept(self)
            right= ctx.expr1(1).accept(self)
            op = "::"
            return BinExpr(op, left, right)
    
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        #expr1: expr2 (EQUAL | NOT_EQUAL | LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr2 | expr2;
        if ctx.getChildCount() == 1:
            return ctx.expr2(0).accept(self)
        else:
            left= ctx.expr2(0).accept(self)
            right= ctx.expr2(1).accept(self)
            if ctx.EQUAL(): op = "=="
            elif ctx.NOT_EQUAL(): op = "!="
            elif ctx.LESS(): op = "<"
            elif ctx.GREATER(): op = ">"
            elif ctx.LESS_OR_EQUAL(): op = "<="
            elif ctx.GREATER_OR_EQUAL(): op = ">="
            return BinExpr(op, left, right)
    
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        #expr2: expr2 (AND | OR) expr3 | expr3;
        if ctx.getChildCount() == 1:
            return ctx.expr3().accept(self)
        else:
            left= ctx.expr2().accept(self)
            right= ctx.expr3().accept(self)
            if ctx.AND(): op = "&&"
            elif ctx.OR(): op = "||"
            return BinExpr(op, left, right)
    
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        #expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
        if ctx.getChildCount() == 1:
            return ctx.expr4().accept(self)
        else:
            left= ctx.expr3().accept(self)
            right= ctx.expr4().accept(self)
            if ctx.ADDOP(): op = "+"
            else :op = "-"
            return BinExpr(op, left, right)
    
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        #expr4: expr4 (MULOP | DIVOP | MOD) expr5 | expr5;
        if ctx.getChildCount() == 1:
            return ctx.expr5().accept(self)
        else:
            left= ctx.expr4().accept(self)
            right= ctx.expr5().accept(self)
            if ctx.MULOP(): op = "*"
            elif ctx.DIVOP(): op = "/"
            elif ctx.MOD(): op = "%"
            return BinExpr(op, left, right)
    
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        #expr5: NOT expr5 | expr6;
        if ctx.getChildCount() == 1:
            return ctx.expr6().accept(self)
        else:
            operand = ctx.expr5().accept(self)
            op = "!"
            return UnExpr(op, operand)

    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        #expr6: SUBOP expr6 | expr7;
        if ctx.getChildCount() == 1:
            return ctx.expr7().accept(self)
        else:
            operand = ctx.expr6().accept(self)
            op = "-"
            return UnExpr(op, operand)
    
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        #expr7: ID LSB exprprime RSB |expr8;
        if ctx.getChildCount() == 1:
            return ctx.expr8().accept(self)
        else:
            return ArrayCell(ctx.ID().getText(),ctx.exprprime().accept(self))
            
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        #expr8: literal | ID | callexpr | LB expr RB;
        if ctx.getChildCount() == 1:
            if ctx.literal(): return ctx.literal().accept(self)
            elif ctx.ID(): return Id(ctx.ID().getText())
            else: return ctx.callexpr().accept(self)
        else:
            return ctx.expr().accept(self)
    
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        #callexpr: ID LB exprlist RB;
        return FuncCall(ctx.ID().getText(),ctx.exprlist().accept(self))
               
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        #block_stmt: LP xet RP;
        return BlockStmt(ctx.xet().accept(self))
    
    def visitXet(self, ctx:MT22Parser.XetContext):
        #xet : xet_stmt xet| ;
        if ctx.getChildCount() == 0: return []
        else: return ctx.xet_stmt().accept(self) + ctx.xet().accept(self)
    
    def visitXet_stmt(self, ctx:MT22Parser.Xet_stmtContext):
        #xet_stmt: stmt | vardecl;
        if ctx.stmt(): return [ctx.stmt().accept(self)]
        else: return ctx.vardecl().accept(self)
    
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        #assignstmt: lhs ASSIGN expr SEMI;
        return AssignStmt(ctx.lhs().accept(self), ctx.expr().accept(self))
    
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        #lhs: ID | ID LSB exprprime RSB;
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.getChildCount() == 4:
            return ArrayCell(ctx.ID().getText(),ctx.exprprime().accept(self))
        
    
        
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        #ifstmt: IF LB expr RB stmt (ELSE stmt)?;
        if ctx.ELSE():
            return IfStmt(ctx.expr().accept(self),
                    ctx.stmt(0).accept(self),
                    ctx.stmt(1).accept(self))
        else: 
            return IfStmt(ctx.expr().accept(self),
                    ctx.stmt(0).accept(self))
        
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        #forstmt: FOR LB (ID | ID LSB exprprime RSB) ASSIGN expr COMMA expr COMMA expr RB stmt;
        if ctx.LSB(): 
            a=ArrayCell(ctx.ID().getText(),ctx.exprprime().accept(self))
            assig = AssignStmt(a,ctx.expr(0).accept(self))
        else:
            assig = AssignStmt(Id(ctx.ID().getText()),ctx.expr(0).accept(self))
        cond = ctx.expr(1).accept(self)
        upd = ctx.expr(2).accept(self)
        loop = ctx.stmt().accept(self)
        return ForStmt(assig, cond, upd, loop)
        
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        #breakstmt: BREAK SEMI;
        return BreakStmt()
    
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        #continuestmt: CONTINUE SEMI;
        return ContinueStmt()

    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        #returnstmt: RETURN expr SEMI | RETURN SEMI;
        if(ctx.getChildCount()==3):
            return ReturnStmt(ctx.expr().accept(self))
        return ReturnStmt()
    
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        #literal: INT_LITERAL | REAL_LITERAL | bool_literal | STRING_LITERAL | array_literal;
        if ctx.REAL_LITERAL():
            return FloatLit(float("0"+ctx.REAL_LITERAL().getText()))
        elif ctx.INT_LITERAL():
            return IntegerLit(int(ctx.INT_LITERAL().getText()))
        elif ctx.bool_literal():
            return BooleanLit(ctx.bool_literal().accept(self))
        elif ctx.STRING_LITERAL():
            return StringLit(ctx.STRING_LITERAL().getText())
        elif ctx.array_literal():
            return ctx.array_literal().accept(self)
    def visitBool_literal(self, ctx:MT22Parser.Bool_literalContext):
        #bool_literal: TRUE | FALSE;
        return bool(True) if ctx.TRUE() else bool(False)
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        #array_literal: LP (expr (COMMA expr)*)? RP;
        result = []
        if ctx.expr():
            result.append(ctx.expr(0).accept(self))
            if ctx.COMMA():
                size = len(ctx.COMMA())
                for i in range(1,size+1):
                    result.append(ctx.expr(i).accept(self))
            return ArrayLit(result)
        else: return ArrayLit(result)
    