"""
    MSSV: 2015043
    Ho va ten: Nguyen Hoang Tri Vien
"""
from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class Symbol:
    def __init__(
        self, 
        name: str, 
        mtype: Type, 
        param: List[str] = None, 
        paramtype: List[Type] = None, 
        paraminherit: List[bool] = None, 
        paramout: List[bool] = None, 
        funcinherit: str = None, 
        returnType: Type = None
    ):
        self.name = name
        self.mtype = mtype
        if param is None:
            self.param = None
        else:
            self.param = param
        if paramtype is None:
            self.paramtype = None
        else:
            self.paramtype = paramtype
        if paraminherit is None:
            self.paraminherit = None
        else:
            self.paraminherit = paraminherit
        if paramout is None:
            self.paramout = None
        else:
            self.paramout = paramout
        self.funcinherit = funcinherit
        self.returnType = returnType



        
class Wrapper:
    def __init__(self, value):
        self.value = value
global_arr = []
inherit = None
prevent = None
in_loop = False
arrayy = None
check_return = False
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [[]])
    
    def visitProgram(self, ast, env):
        global global_arr
        global in_loop
        global inherit
        global prevent
        global arrayy
        global check_return
        check_return = False
        inherit = None
        prevent = None
        in_loop = False
        arrayy = None
        global_arr = ["readInteger","printInteger","readFloat","writeFloat","readBoolean","printBoolean","readString","printString","super","preventDefault"]
        env=[[
            Symbol(
                "readInteger",
                Wrapper(Function()),
                [],[],[],[],
                None,
                Wrapper(IntegerType())
            ),
            Symbol(
                "printInteger",
                Wrapper(Function()),
                ["anArg"],[Wrapper(IntegerType())],[False],[False],
                None,
                Wrapper(VoidType())
            ),
            Symbol(
                "readFloat",
                Wrapper(Function()),
                [],[],[],[],
                None,
                Wrapper(FloatType())
            ),
            Symbol(
                "writeFloat",
                Wrapper(Function()),
                ["anArg"],[Wrapper(FloatType())],[False],[False],
                None,
                Wrapper(VoidType())
            ),
            Symbol(
                "readBoolean",
                Wrapper(Function()),
                [],[],[],[],
                None,
                Wrapper(BooleanType())
            ),
            Symbol(
                "printBoolean",
                Wrapper(Function()),
                ["anArg"],[Wrapper(BooleanType())],[False],[False],
                None,
                Wrapper(VoidType())
            ),
            Symbol(
                "readString",
                Wrapper(Function()),
                [],[],[],[],
                None,
                Wrapper(StringType())
            ),
            Symbol(
                "printString",
                Wrapper(Function()),
                ["anArg"],[Wrapper(StringType())],[False],[False],
                None,
                Wrapper(VoidType())
            ),
        ]]
        for decl in ast.decls:
            if isinstance(decl, FuncDecl):
                env = self.createFuncDecl(decl, env) 
        
        for decl in ast.decls:
            if isinstance(decl, VarDecl):
                env = self.visit(decl, env)
            if isinstance(decl, FuncDecl):
                self.visit(decl, env)

        self.checkNoEntryPoint(env)
    
    def inferid(self, name,typ,env):
        flag= False
        for mm in range(len(env)):
            for nn in range(len(env[mm])):
                if env[mm][nn].name == name and not isinstance(env[mm][nn].mtype.value, Function):
                    env[mm][nn].mtype = typ
                    flag=True
                    break
            if flag: break
    def inferfunccall(self, name, typ, env):
        for i in range(len(env[-1])):
            if env[-1][i].name == name and isinstance(env[-1][i].mtype.value, Function):
                env[-1][i].returnType = typ
                break
            
    def visitVarDecl(self, ast, env):
        global global_arr
        if len(env)==1:
            for decl in global_arr:
                if decl == ast.name:
                    raise Redeclared(Variable(), ast.name)
            global_arr = global_arr + [ast.name] 
            vartype = self.visit(ast.typ, env)
            if type(vartype.value) is AutoType:
                vardecl = Symbol(name=ast.name, mtype=vartype)
                env[0] += [vardecl]
                if ast.init is None:
                    raise Invalid(Variable(), ast.name)
                else:
                    varinit = self.visit(ast.init,env)
                    if type(varinit.value) is VoidType:
                        raise TypeMismatchInExpression(ast.init)
                    else:
                        env[0][-1].mtype = varinit
                        return env
            else:
                if ast.init is not None:
                    varinit = self.visit(ast.init,env)
                    if type(varinit.value) is VoidType:
                        raise TypeMismatchInExpression(ast.init)
                    elif type(vartype.value) is ArrayType and type(varinit.value) is ArrayType:
                        if vartype.value.dimensions != varinit.value.dimensions or type(vartype.value.typ.value) is not type(varinit.value.typ.value):
                            raise TypeMismatchInVarDecl(ast)
                    elif type(vartype.value) is FloatType:
                        if type(varinit.value) is not FloatType and type(varinit.value) is not IntegerType:
                            raise TypeMismatchInVarDecl(ast)
                    elif type(varinit.value) is AutoType:
                        if type(ast.init) is FuncCall:
                            self.inferfunccall(ast.init.name, vartype,env)
                        
                        elif type(ast.init) is Id:
                            self.inferid(ast.init.name, vartype,env)
                    else:
                        if type(vartype.value) is not type(varinit.value):
                            raise TypeMismatchInVarDecl(ast)

                    vardecl = Symbol(name=ast.name, mtype=vartype)
                    env[0] += [vardecl]
                    return env
                else:
                    vardecl = Symbol(name=ast.name, mtype=vartype)
                    env[0] += [vardecl]
                    return env
        else:
            for decl in env[0]:
                if decl.name == ast.name:
                    raise Redeclared(Variable(),ast.name) 
            varname = ast.name
            vartype = self.visit(ast.typ,env)
            if type(vartype.value) is AutoType:
                vardecl = Symbol(name=varname, mtype=vartype)
                env[0] += [vardecl]
                if ast.init is None:
                    raise Invalid(Variable(), ast.name)
                else:
                    varinit = self.visit(ast.init,env)
                    if type(varinit.value) is VoidType:
                        raise TypeMismatchInExpression(ast.init)
                    else:
                        env[0][-1].mtype = varinit
                        return env
            else:
                if ast.init is not None:
                    varinit = self.visit(ast.init,env)
                    if type(varinit.value) is VoidType:
                        raise TypeMismatchInExpression(ast.init)
                    elif type(vartype.value) is ArrayType and type(varinit.value) is ArrayType:
                        if vartype.value.dimensions != varinit.value.dimensions or type(vartype.value.typ.value) is not type(varinit.value.typ.value):
                            raise TypeMismatchInVarDecl(ast)
                    elif type(vartype.value) is FloatType:
                        if type(varinit.value) is not FloatType and type(varinit.value) is not IntegerType:
                            raise TypeMismatchInVarDecl(ast)
                    elif type(varinit.value) is AutoType:
                        if type(ast.init) is FuncCall:
                            self.inferfunccall(ast.init.name, vartype,env)
                            
                        elif type(ast.init) is Id:
                            self.inferid(ast.init.name, vartype,env)
                    else:
                        if type(vartype.value) is not type(varinit.value):
                            raise TypeMismatchInVarDecl(ast)
                    vardecl = Symbol(name=ast.name, mtype=vartype)
                    env[0] += [vardecl]
                    return env
                else:
                    vardecl = Symbol(name=ast.name, mtype=vartype)
                    env[0] += [vardecl]
                    return env
            

    def checkPrevent(self, ast):
        if len(ast.body) > 0:
            if type(ast.body[0]) is CallStmt and ast.body[0].name == "preventDefault":
                if len(ast.body[0].args)>0:
                    raise TypeMismatchInExpression(ast.body[0].args[0])
                return True
        else: return False    
    def visitFuncDecl(self, ast, env):
        global global_arr
        for decl in global_arr:
            if decl == ast.name:
                raise Redeclared(Function(), ast.name)  
        global_arr = global_arr + [ast.name]
        global inherit
        global prevent
        for decl in env[-1]:
            if decl.name == ast.name:
                if decl.funcinherit is not None:
                    inherit = True
                    if self.checkPrevent(ast.body):
                        prevent = True
                    else: prevent = False
                else: inherit = False
                break                        
        local_env = [[]]+env
        for decl in ast.params:
            local_env = self.visit(decl, local_env)
        
        # n de luu cai chi so -> suy ra duoc cai ham
        n=0
        for i in range(len(env[-1])):
            if env[-1][i].name==ast.name: n=i         
            
        if inherit:
            func= None
            if prevent == False:
                funcinherit = local_env[-1][n].funcinherit
                for i in range(len(local_env[-1])):
                    if local_env[-1][i].name == funcinherit and type(env[-1][i].mtype.value) is Function:
                        func = local_env[-1][i]
                        break
                for i in range(len(func.param)):
                    if func.paraminherit[i]==True:
                        paramdecl = Symbol(
                            name = func.param[i],
                            mtype = func.paramtype[i]
                        )
                        local_env[0]+= [paramdecl]
                        
        self.visit(ast.body, local_env)
        
    def visitBlockStmt(self, ast, env):
        global global_arr
        global check_return
        old = False
        if len(env) == 2:
            n=0
            func_name = global_arr[-1]
            for i in range(len(env[-1])):
                if env[-1][i].name == func_name:
                    n=i
            if env[-1][n].funcinherit is not None:
                funcinherit = env[-1][n].funcinherit
                stt= 0
                for i in range(len(env[-1])):
                    if env[-1][i].name == funcinherit:
                        stt=i
                        break
                parentfunc = env[-1][stt]
                if len(parentfunc.param) == 0:
                    if len(ast.body)>0:
                        for i in range(len(ast.body)):
                            if i==0:
                                if type(ast.body[i]) is CallStmt and ast.body[i].name == "super":
                                    self.visit(ast.body[i],env)
                                elif type(ast.body[i]) is CallStmt and ast.body[i].name == "preventDefault":
                                    self.visit(ast.body[i],env)
                                else:
                                    if type(ast.body[i]) is VarDecl: env = self.visit(ast.body[i],env)
                                    elif type(ast.body[i]) is BlockStmt:
                                        local_env = [[]] + env
                                        self.visit(ast.body[i],local_env)
                                    elif type(ast.body[i]) is ReturnStmt:
                                        check_return = old
                                        self.visit(ast.body[i],env)
                                        old = check_return
                                    else: self.visit(ast.body[i],env)
                            else:
                                if type(ast.body[i]) is VarDecl: env = self.visit(ast.body[i],env)
                                elif type(ast.body[i]) is BlockStmt:
                                    local_env = [[]] + env
                                    self.visit(ast.body[i],local_env)
                                elif type(ast.body[i]) is ReturnStmt:
                                    check_return = old
                                    self.visit(ast.body[i],env)
                                    old = check_return
                                else: self.visit(ast.body[i],env)
                else:
                    if len(ast.body)>0:
                        for i in range(len(ast.body)):
                            if i==0:
                                if type(ast.body[i]) is not CallStmt:
                                    raise InvalidStatementInFunction(func_name)
                                elif type(ast.body[i]) is CallStmt and ast.body[i].name != "super" and ast.body[i].name != "preventDefault":
                                    raise InvalidStatementInFunction(func_name)
                                elif type(ast.body[i]) is CallStmt and ast.body[i].name == "super":
                                    for mm in range(len(parentfunc.param)):
                                        if parentfunc.paraminherit[mm] == True:
                                            name = parentfunc.param[mm]
                                            for nn in range(mm+1,len(parentfunc.param)):
                                                if parentfunc.param[nn] == name and parentfunc.paraminherit[nn] == True:
                                                    raise Redeclared(Parameter(), name)
                                    self.visit(ast.body[i],env)
                                elif type(ast.body[i]) is CallStmt and ast.body[i].name == "preventDefault":
                                    self.visit(ast.body[i],env)
                            else:
                                if type(ast.body[i]) is VarDecl: env = self.visit(ast.body[i],env)
                                elif type(ast.body[i]) is BlockStmt:
                                    local_env = [[]] + env
                                    self.visit(ast.body[i],local_env)
                                elif type(ast.body[i]) is ReturnStmt:
                                    check_return = old
                                    self.visit(ast.body[i],env)
                                    old = check_return
                                else: self.visit(ast.body[i],env)
                    else: raise InvalidStatementInFunction(func_name)
            else:
                for i in range(len(ast.body)):
                    if i==0:
                        if type(ast.body[i]) is CallStmt:
                            if ast.body[i].name == "super" or ast.body[i].name == "preventDefault":
                                raise InvalidStatementInFunction(func_name)
                            else: self.visit(ast.body[i],env)
                        else:
                            if type(ast.body[i]) is VarDecl: env = self.visit(ast.body[i],env)
                            elif type(ast.body[i]) is BlockStmt:
                                local_env = [[]] + env
                                self.visit(ast.body[i],local_env)
                            elif type(ast.body[i]) is ReturnStmt:
                                check_return = old
                                self.visit(ast.body[i],env)
                                old = check_return
                            else: self.visit(ast.body[i],env)                                    
                    else:
                        if type(ast.body[i]) is VarDecl: env = self.visit(ast.body[i],env)
                        elif type(ast.body[i]) is BlockStmt:
                            local_env = [[]] + env
                            self.visit(ast.body[i],local_env)
                        elif type(ast.body[i]) is ReturnStmt:
                            check_return = old
                            self.visit(ast.body[i],env)
                            old = check_return
                        else: self.visit(ast.body[i],env)
        else:
            for i in range(len(ast.body)):
                if type(ast.body[i]) is VarDecl: env = self.visit(ast.body[i],env)
                elif type(ast.body[i]) is BlockStmt:
                    local_env = [[]] + env
                    self.visit(ast.body[i],local_env)
                elif type(ast.body[i]) is ReturnStmt:
                    check_return = old
                    self.visit(ast.body[i],env)
                    old = check_return
                else: self.visit(ast.body[i],env)
                                    
    def visitParamDecl(self,ast,env):
        global global_arr
        for decl in env[0]:
            if decl.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
            
        # n de xac dinh vi tri cua ham trong env[-1] 
        n=0
        func_name = global_arr[-1]
        for x in range(len(env[-1])):
            if env[-1][x].name == func_name:
                n=x
                break
        typp = None
        for i in range(len(env[-1][n].param)):
            if env[-1][n].param[i] == ast.name:
                typp = env[-1][n].paramtype[i]
                break
        if inherit:
            funcinherit = env[-1][n].funcinherit
            stt= -1
            for x in range(len(env[-1])):
                if env[-1][x].name == funcinherit and type(env[-1][x].mtype.value) is Function:
                    stt=x
                    break
            if stt == -1:
                raise Undeclared(Function(),funcinherit)
            else:
                if prevent==False:
                    func = env[-1][stt]
                    for i in range(len(func.param)):
                        if func.param[i] == ast.name and func.paraminherit[i]==True:
                            raise Invalid(Parameter(),ast.name)                    
        paramdecl = Symbol(
            name = ast.name,
            mtype = typp
        )
        env[0]+= [paramdecl]
        return env
            
    def createFuncDecl(self, ast, env):  
        name = ast.name
        returntyp = self.visit(ast.return_type,env)

        param = []
        paramtype = []
        paraminherit = []
        paramout = []
        funcinherit = None
        for x in ast.params:
            param = self.getparamname(x, param)
            paramtype  = self.getparamtype(x, paramtype)
            paraminherit = self.getparaminherit(x, paraminherit)
            paramout = self.getparamout(x, paramout)
        if ast.inherit is not None:
            funcinherit = ast.inherit
        else:
            funcinherit = None
            
        funcdecl = Symbol(
            name = name,
            mtype = Wrapper(Function()),
            param = param,
            paramtype = paramtype,
            paraminherit = paraminherit,
            paramout = paramout,
            funcinherit = funcinherit,
            returnType=returntyp
        )
        env[0] += [funcdecl]
        return env
    
    def getparamname(self, ast,env):
        env = env + [ast.name]
        return env
    def getparamtype(self, ast,env):
        env = env + [self.visit(ast.typ,env)]
        return env
    def getparaminherit(self, ast,env):
        env = env + [ast.inherit]
        return env
    def getparamout(self, ast,env):
        env = env + [ast.out]
        return env
    
        
    def visitIntegerType(self, ast, env):
        return Wrapper(IntegerType())

    def visitFloatType(self, ast, env):
        return Wrapper(FloatType())
    
    def visitBooleanType(self, ast, env):
        return Wrapper(BooleanType())

    def visitStringType(self, ast, env):
        return Wrapper(StringType())
    
    def visitAutoType(self, ast, env):
        return Wrapper(AutoType())
    
    def visitVoidType(self, ast, env):
        return Wrapper(VoidType())
    
    def visitArrayType(self, ast, env):
        return Wrapper(ArrayType(ast.dimensions,self.visit(ast.typ, env)))
    
    
    def visitContinueStmt(self, ast, env):
        if in_loop == False:
            raise MustInLoop(ast)

    def visitBreakStmt(self, ast, env):
        if in_loop == False:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast, env):
        global global_arr
        global check_return
        funcname = global_arr[-1]
        func_type = None
        expr_type = None
        if ast.expr is None:
            expr_type = Wrapper(VoidType())
        else:
            expr_type = self.visit(ast.expr,env)
        for decl in env[-1]:
            if decl.name == funcname:
                func_type = decl.returnType
                break
        if check_return == False:
            check_return = True
            if type(func_type.value) is not AutoType and type(expr_type.value) is not AutoType:
                if type(func_type.value) is FloatType:
                    if type(expr_type.value) is not FloatType and type(expr_type.value) is not IntegerType:
                        raise TypeMismatchInStatement(ast)
                elif type(func_type.value) is ArrayType and type(expr_type.value) is ArrayType:
                    if func_type.value.dimensions != expr_type.value.dimensions or type(func_type.value.typ.value) is not type(expr_type.value.typ.value):
                        raise TypeMismatchInStatement(ast)
                elif type(func_type.value) is not type(expr_type.value):
                    raise TypeMismatchInStatement(ast)
            elif type(func_type.value) is AutoType:
                self.inferfunccall(funcname,expr_type,env)
            elif type(expr_type.value) is AutoType:
                if type(ast.expr) is Id:
                    self.inferid(ast.expr.name, func_type, env)
                if type(ast.expr) is FuncCall:
                    self.inferfunccall(ast.expr.name, func_type, env)    
                            
    def visitCallStmt(self, ast, env):
        # function thay cho chu method
        global global_arr
        function = ast.name
        find = False
        n=-1
        if function != "super" and function != "preventDefault":
            for i in range(len(env[-1])):
                if env[-1][i].name == function and isinstance(env[-1][i].mtype.value, Function):
                    find = True
                    n=i
                    break
            if not find: 
                raise Undeclared(Function(), ast.name)
            else:
                func = env[-1][n]
                a = len(ast.args) # len cua call stmt
                b = len(func.param) # len cua function
                if a!=b: raise TypeMismatchInStatement(ast)
                for i in range(a):
                    if type(func.paramtype[i].value) is not AutoType and type(self.visit(ast.args[i],env).value) is not AutoType:
                        if type(func.paramtype[i].value) is FloatType:
                            if type(self.visit(ast.args[i],env).value) is not FloatType and type(self.visit(ast.args[i],env).value) is not IntegerType:
                                raise TypeMismatchInStatement(ast)
                        elif type(func.paramtype[i].value) is ArrayType and type(self.visit(ast.args[i],env).value) is ArrayType:
                            if func.paramtype[i].value.dimensions != self.visit(ast.args[i],env).value.dimensions or type(func.paramtype[i].value.typ.value) is not type(self.visit(ast.args[i],env).value.typ.value):
                                raise TypeMismatchInStatement(ast)
                        elif type(func.paramtype[i].value) is not type(self.visit(ast.args[i],env).value):
                            raise TypeMismatchInStatement(ast)
                    if type(func.paramtype[i].value) is AutoType:
                        if type(self.visit(ast.args[i],env).value) is VoidType:
                            raise TypeMismatchInStatement(ast)
                        env[-1][n].paramtype[i] = self.visit(ast.args[i],env)
                        if ast.name == global_arr[-1]:
                            self.inferid(func.param[i],self.visit(ast.args[i],env),env)
                    if type(self.visit(ast.args[i],env).value) is AutoType:
                        if type(ast.args[i]) is FuncCall:
                            self.inferfunccall(ast.args[i].name, func.paramtype[i], env)
                            
                        if type(ast.args[i]) is Id:
                            self.inferid(ast.args[i].name, func.paramtype[i], env)
        else:
            if function == "preventDefault":
                if len(ast.args) > 0:
                    raise TypeMismatchInExpression(ast.args[0])
            if function == "super":
                funcname = global_arr[-1]
                funcinherit = ""
                func = None
                for i in range(len(env[-1])):
                    if env[-1][i].name == funcname and isinstance(env[-1][i].mtype.value, Function):
                        funcinherit = env[-1][i].funcinherit
                        break
                for i in range(len(env[-1])):
                    if env[-1][i].name == funcinherit and isinstance(env[-1][i].mtype.value, Function):
                        func = env[-1][i]
                        a = len(ast.args) # len cua call stmt
                        b = len(func.param) # len cua function
                        if a>b: raise TypeMismatchInExpression(ast.args[b])
                        elif a<b: raise TypeMismatchInExpression(None)
                        else:
                            for j in range(a):
                                if type(func.paramtype[j].value) is not AutoType and type(self.visit(ast.args[j],env).value) is not AutoType:
                                    if type(func.paramtype[j].value) is FloatType:
                                        if type(self.visit(ast.args[j],env).value) is not FloatType and type(self.visit(ast.args[j],env).value) is not IntegerType:
                                            raise TypeMismatchInExpression(ast.args[j])
                                    elif type(func.paramtype[j].value) is ArrayType and type(self.visit(ast.args[j],env).value) is ArrayType:
                                        if func.paramtype[j].value.dimensions != self.visit(ast.args[j],env).value.dimensions or type(func.paramtype[j].value.typ.value) is not type(self.visit(ast.args[j],env).value.typ.value):
                                            raise TypeMismatchInExpression(ast.args[j])
                                    elif type(func.paramtype[j].value) is not type(self.visit(ast.args[j],env).value):
                                        raise TypeMismatchInExpression(ast.args[j])
                                if type(func.paramtype[j].value) is AutoType:
                                    if type(self.visit(ast.args[j],env).value) is VoidType:
                                        raise TypeMismatchInExpression(ast.args[j])
                                    env[-1][i].paramtype[j] = self.visit(ast.args[j],env)
                                if type(self.visit(ast.args[j],env).value) is AutoType:  
                                    if type(ast.args[j]) is FuncCall:
                                        self.inferfunccall(ast.args[j].name, func.paramtype[j], env)
                                        
                                    if type(ast.args[j]) is Id:
                                        self.inferid(ast.args[j].name,func.paramtype[j],env)
                        break    
    def visitFuncCall(self, ast, env):
        name = ast.name
        find =False
        n=-1
        for i in range(len(env[-1])):
            if env[-1][i].name == name and isinstance(env[-1][i].mtype.value, Function):
                find=True
                n=i
                break
        if not find: 
            raise Undeclared(Function(),ast.name)
        else:
            func = env[-1][n]
            a = len(ast.args) # len cua call stmt
            b = len(func.param) # len cua function
            if a!=b: raise TypeMismatchInExpression(ast)
            for i in range(a):
                if type(func.paramtype[i].value) is not AutoType and type(self.visit(ast.args[i],env).value) is not AutoType:
                    if type(func.paramtype[i].value) is ArrayType and type(self.visit(ast.args[i],env).value) is ArrayType:
                        if func.paramtype[i].value.dimensions != self.visit(ast.args[i],env).value.dimensions or type(func.paramtype[i].value.typ.value) is not type(self.visit(ast.args[i],env).value.typ.value):
                            raise TypeMismatchInExpression(ast.args[j])
                    elif type(func.paramtype[i].value) is FloatType:
                        if type(self.visit(ast.args[i],env).value) is not FloatType and type(self.visit(ast.args[i],env).value) is not IntegerType:
                            raise TypeMismatchInExpression(ast.args[j])
                    elif type(func.paramtype[i].value) is not type(self.visit(ast.args[i],env).value):
                        raise TypeMismatchInExpression(ast)
                if type(func.paramtype[i].value) is AutoType:
                    if type(self.visit(ast.args[i],env).value) is VoidType:
                        raise TypeMismatchInExpression(ast)
                    env[-1][n].paramtype[i] = self.visit(ast.args[i],env)
                    if ast.name == global_arr[-1]:
                        self.inferid(func.param[i],self.visit(ast.args[i],env),env)
                if type(self.visit(ast.args[i],env).value) is AutoType:
                    if type(ast.args[i]) is FuncCall:
                        self.inferfunccall(ast.args[i].name,func.paramtype[i],env)
                        
                    if type(ast.args[i]) is Id:
                        self.infer(ast.args[i].name, func.paramtype[i], env)
        if type(env[-1][n].returnType.value) is VoidType:
            raise TypeMismatchInExpression(ast)
        else:
            return env[-1][n].returnType
    
    def visitBinExpr(self, ast, env):
        op = ast.op
        left = self.visit(ast.left, env)
        leftType = left

        right = self.visit(ast.right, env)
        rightType = right
        if op in ["&&", "||"]:
            if type(leftType.value) is BooleanType and type(rightType.value) is BooleanType:
                return Wrapper(BooleanType())
            if not isinstance(leftType.value, BooleanType) and not isinstance(leftType.value, AutoType):
                raise TypeMismatchInExpression(ast)
            if not isinstance(rightType.value, BooleanType) and not isinstance(rightType.value, AutoType):
                raise TypeMismatchInExpression(ast)
            if type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(BooleanType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(BooleanType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is AutoType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(BooleanType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(BooleanType()), env)
                return Wrapper(BooleanType())          
        if op in ["+", "-", "*", "/"]:
            if type(leftType.value) is IntegerType and type(rightType.value) is IntegerType:
                return Wrapper(IntegerType())
            if type(leftType.value) is FloatType and type(rightType.value) is FloatType:
                return Wrapper(FloatType())
            if type(leftType.value) is IntegerType and type(rightType.value) is FloatType:
                return Wrapper(FloatType())
            if type(leftType.value) is FloatType and type(rightType.value) is IntegerType:
                return Wrapper(FloatType())
            if type(leftType.value) is IntegerType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(IntegerType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(IntegerType()), env)
                return Wrapper(IntegerType())
            if type(leftType.value) is FloatType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name, Wrapper(FloatType()), env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(FloatType()), env)
                return Wrapper(FloatType())
            if type(leftType.value) is AutoType and type(rightType.value) is IntegerType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(IntegerType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name,Wrapper(IntegerType()), env)
                return Wrapper(IntegerType())
            if type(leftType.value) is AutoType and type(rightType.value) is FloatType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(FloatType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(FloatType()), env)
                return Wrapper(FloatType())
            raise TypeMismatchInExpression(ast)
        
        if op in ["%"]:
            if type(leftType.value) is IntegerType and type(rightType.value) is IntegerType:
                return Wrapper(IntegerType())
            if type(leftType.value) is IntegerType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(IntegerType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(IntegerType()), env)
                return Wrapper(IntegerType())
            if type(leftType.value) is AutoType and type(rightType.value) is IntegerType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(IntegerType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(IntegerType()), env)
                return Wrapper(IntegerType())
            raise TypeMismatchInExpression(ast)
        
        if op in ["::"]:
            if type(leftType.value) is StringType and type(rightType.value) is StringType:
                return Wrapper(StringType())
            if type(leftType.value) is StringType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(StringType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(StringType()), env)
                return Wrapper(StringType())
            if type(leftType.value) is AutoType and type(rightType.value) is StringType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(StringType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(StringType()), env)
                return Wrapper(StringType())
            raise TypeMismatchInExpression(ast)
        
        if op in ["==", "!="]:
            if type(leftType.value) is IntegerType and type(rightType.value) is IntegerType:
                return Wrapper(BooleanType())
            if type(leftType.value) is BooleanType and type(rightType.value) is BooleanType:
                return Wrapper(BooleanType())
            if type(leftType.value) is IntegerType and type(rightType.value) is BooleanType:
                return Wrapper(BooleanType())
            if type(leftType.value) is BooleanType and type(rightType.value) is IntegerType:
                return Wrapper(BooleanType())
            if type(leftType.value) is BooleanType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(BooleanType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(BooleanType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is IntegerType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(IntegerType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name,Wrapper(IntegerType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is AutoType and type(rightType.value) is BooleanType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(BooleanType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(BooleanType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is AutoType and type(rightType.value) is IntegerType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(IntegerType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(IntegerType()), env)
                return Wrapper(BooleanType())
            
            raise TypeMismatchInExpression(ast)

        if op in ["<", ">", "<=", ">="]:
            if type(leftType.value) is IntegerType and type(rightType.value) is IntegerType:
                return Wrapper(BooleanType())
            if type(leftType.value) is FloatType and type(rightType.value) is FloatType:
                return Wrapper(BooleanType())
            if type(leftType.value) is IntegerType and type(rightType.value) is FloatType:
                return Wrapper(BooleanType())
            if type(leftType.value) is FloatType and type(rightType.value) is IntegerType:
                return Wrapper(BooleanType())
            
            if type(leftType.value) is IntegerType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(IntegerType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(IntegerType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is FloatType and type(rightType.value) is AutoType:
                if type(ast.right) is FuncCall:
                    self.inferfunccall(ast.right.name,Wrapper(FloatType()),env)
                    
                if type(ast.right) is Id:
                    self.inferid(ast.right.name, Wrapper(FloatType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is AutoType and type(rightType.value) is IntegerType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(IntegerType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(IntegerType()), env)
                return Wrapper(BooleanType())
            if type(leftType.value) is AutoType and type(rightType.value) is FloatType:
                if type(ast.left) is FuncCall:
                    self.inferfunccall(ast.left.name,Wrapper(FloatType()),env)
                    
                if type(ast.left) is Id:
                    self.inferid(ast.left.name, Wrapper(FloatType()), env)
                return Wrapper(BooleanType())
            raise TypeMismatchInExpression(ast)
    def visitUnExpr(self, ast, env):
        op = ast.op
        val = self.visit(ast.val, env)
        valType = val
        if op == "!":
            if type(valType.value) is BooleanType:
                return Wrapper(BooleanType())
            if type(valType.value) is AutoType:
                funcname = ast.val.name
                for i in range(len(env[-1])):
                    if env[-1][i].name == funcname and isinstance(env[-1][i].mtype.value, Function):
                        env[-1][i].returnType = Wrapper(BooleanType())
                        break
                return Wrapper(BooleanType())
            if not isinstance(val.value, BooleanType()):
                raise TypeMismatchInExpression(ast)
        if op == "-":
            if type(valType.value) is IntegerType:
                return Wrapper(IntegerType())
            if type(valType.value) is FloatType:
                return Wrapper(FloatType())
            raise TypeMismatchInExpression(ast)
        
        
    def visitArrayCell(self, ast, env):
        arrayName = ast.name
        array = None
        find = False
        for decl in env:
            for var in decl:
                if var.name == arrayName:
                    if type(var.mtype.value) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                    else: array = var
                    find = True 
                    break
            if find: break
        if not find: raise Undeclared(Identifier(),ast.name) 

        array_type = array.mtype
        if len(array_type.value.dimensions) < len(ast.cell):
            raise TypeMismatchInExpression(ast)

        for ind in ast.cell:
            indType = self.visit(ind, env)
            if type(indType.value) is not IntegerType:
                raise TypeMismatchInExpression(ast)

        if len(ast.cell) == len(array_type.value.dimensions):
            return array_type.value.typ
        else: 
            lenn = len(ast.cell)
            dimen = array_type.value.dimensions[lenn:]
            return Wrapper(ArrayType(dimen,array_type.value.typ))
    
    def visitForStmt(self, ast, env):
        global in_loop
        global check_return
        assign = self.visit(ast.init.lhs, env)
        if type(assign.value) is AutoType:
            if type(ast.init.lhs) is FuncCall:
                self.inferfunccall(ast.init.lhs.name,Wrapper(IntegerType()),env)
                
            elif type(ast.init.lhs) is Id:
                self.inferid(ast.init.lhs.name,Wrapper(IntegerType()),env)
        elif type(assign.value) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.init, env) 
        cond = self.visit(ast.cond, env)
        if type(cond.value) is AutoType:
            if type(ast.cond) is FuncCall:
                self.inferfunccall(ast.cond.name,Wrapper(BooleanType()),env)
                
            elif type(ast.cond) is Id:
                self.inferid(ast.cond.name,Wrapper(BooleanType()),env)
        elif type(cond.value) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        upd = self.visit(ast.upd, env)
        if type(upd.value) is AutoType:
            if type(ast.upd) is FuncCall:
                self.inferfunccall(ast.upd.name,Wrapper(IntegerType()),env)
                
            elif type(ast.upd) is Id:
                self.inferid(ast.upd.name,Wrapper(IntegerType()),env)
        elif type(upd.value) is not IntegerType:
                raise TypeMismatchInStatement(ast)
        check_return = False
        if in_loop == False:
            in_loop = True    
            if type(ast.stmt) is BlockStmt:
                local_env = [[]] + env
                self.visit(ast.stmt, local_env)
            else:
                self.visit(ast.stmt, env)
            in_loop = False
        else:
            if type(ast.stmt) is BlockStmt:
                local_env = [[]] + env
                self.visit(ast.stmt, local_env)
            else:
                self.visit(ast.stmt, env)
    
    def visitWhileStmt(self, ast, env):
        global in_loop
        global check_return
        expr = self.visit(ast.cond, env)
        if type(expr.value) is AutoType:
            if type(ast.cond) is FuncCall:
                self.inferfunccall(ast.cond.name,Wrapper(BooleanType()), env)
                
            elif type(ast.cond) is Id:
                self.inferid(ast.cond.name,Wrapper(BooleanType()), env)
        elif type(expr.value) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        check_return = False
        if in_loop == False:
            in_loop = True    
            if type(ast.stmt) is BlockStmt:
                local_env = [[]] + env
                self.visit(ast.stmt, local_env)
            else:
                self.visit(ast.stmt, env)
            in_loop = False
        else:
            if type(ast.stmt) is BlockStmt:
                local_env = [[]] + env
                self.visit(ast.stmt, local_env)
            else:
                self.visit(ast.stmt, env)
    
    def visitDoWhileStmt(self, ast, env):
        global in_loop
        global check_return
        local_env = [[]] + env
        check_return = False
        if in_loop == False:
            in_loop = True
            self.visit(ast.stmt, local_env)
            in_loop = False
        else:
            self.visit(ast.stmt, local_env)
        expr = self.visit(ast.cond, env)
        if type(expr.value) is AutoType:
            if type(ast.cond) is FuncCall:
                self.inferfunccall(ast.cond.name,Wrapper(BooleanType()), env)
                
            elif type(ast.cond) is Id:
                self.inferid(ast.cond.name,Wrapper(BooleanType()), env)
        elif type(expr.value) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
    def visitIfStmt(self, ast, env):
        global check_return
        exprType = self.visit(ast.cond, env)
        if type(exprType.value) is AutoType:
            if type(ast.cond) is FuncCall:
                self.inferfunccall(ast.cond.name,Wrapper(BooleanType()),env)
                
            elif type(ast.cond) is Id:
                self.inferid(ast.cond.name,Wrapper(BooleanType()),env)
        elif type(exprType.value) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        check_return = False
        if type(ast.tstmt) is BlockStmt:
            local_env_true = [[]] + env
            self.visit(ast.tstmt, local_env_true)
        else:
            self.visit(ast.tstmt, env)
        
        if ast.fstmt is not None:
            check_return = False
            if type(ast.fstmt) is BlockStmt:
                local_env_false = [[]] + env
                self.visit(ast.fstmt, local_env_false)
            else:
                self.visit(ast.fstmt, env)
    
    def visitAssignStmt(self, ast, env):
        right = self.visit(ast.rhs, env)
        rightType = right
        left = self.visit(ast.lhs, env)
        leftType = left
        if isinstance(leftType.value, VoidType) or isinstance(leftType.value, ArrayType):
            raise TypeMismatchInStatement(ast)
        if isinstance(rightType.value, AutoType):
            if type(ast.rhs) is FuncCall:
                self.inferfunccall(ast.rhs.name,leftType,env)
                
            if type(ast.rhs) is Id:
                self.inferid(ast.rhs.name, leftType, env)
        elif isinstance(leftType.value, AutoType):
            if type(ast.lhs) is Id:
                self.inferid(ast.lhs.name, rightType, env)
        elif isinstance(leftType.value, FloatType):
            if type(rightType.value) is not FloatType and type(rightType.value) is not IntegerType:
                raise TypeMismatchInStatement(ast)
        elif type(leftType.value) is not type(rightType.value):
            raise TypeMismatchInStatement(ast)
    
    def checkNoEntryPoint(self, env):
        for symbol in env[-1]:
            if isinstance(symbol.mtype.value, Function) and isinstance(symbol.returnType.value, VoidType):
                if symbol.name == "main" and len(symbol.param) == 0:
                    return
        raise NoEntryPoint()

    def visitId(self, ast, env):
        id=None
        find=False
        for decl in env:
            for var in decl:
                if var.name == ast.name and not isinstance(var.mtype.value, Function):
                    find = True
                    id = var
                    break
            if find: break
        if not find: raise Undeclared(Identifier(),ast.name)
        else: 
            return id.mtype
        
    def visitIntegerLit(self, ast, env):
        return Wrapper(IntegerType())

    def visitFloatLit(self, ast, env):
        return Wrapper(FloatType())
    
    def visitBooleanLit(self, ast, env):
        return Wrapper(BooleanType())

    def visitStringLit(self, ast, env):
        return Wrapper(StringType())

    def visitArrayLit(self, ast, env):
        global arrayy
        if arrayy is None:
            arrayy = ast
        elems = ast.explist
        elemsType = self.visit(elems[0], env)

        for elem in ast.explist:
            elemtyp = self.visit(elem, env)
            if type(elemtyp.value) is ArrayType and type(elemsType.value) is ArrayType:
                if elemtyp.value.dimensions != elemsType.value.dimensions or type(elemtyp.value.typ.value) is not type(elemsType.value.typ.value):
                    x= arrayy
                    arrayy = None
                    raise IllegalArrayLiteral(x)
            elif type(elemtyp.value) is not type(elemsType.value):
                x= arrayy
                arrayy = None
                raise IllegalArrayLiteral(x)            
        dimen = [len(elems)] + (
            elemsType.value.dimensions if type(elemsType.value) is ArrayType else []
        )   
        if type(elemsType.value) is ArrayType: 
            if ast == arrayy: arrayy = None
            return Wrapper(ArrayType(dimen, elemsType.value.typ))
        else:
            if ast == arrayy: arrayy = None   
            return Wrapper(ArrayType(dimen, elemsType))
