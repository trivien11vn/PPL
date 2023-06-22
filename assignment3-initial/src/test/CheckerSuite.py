import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

	def test1(self):
		input = """
		main: function auto (a:integer, b: string){
			return "1";
		}"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input, expect, 401))

	def test2(self):
		input = """
		main: function void (a:integer, b: string){
		
		}
		main: function void (a:integer, b: string){
		
		}"""
		expect = "Redeclared Function: main"
		self.assertTrue(TestChecker.test(input, expect, 402))

	def test3(self):
		input = """
		foo: function void (a:integer, b: string) inherit main{
			super();
		}
		main: function void (){
		
		}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 403))

	def test4(self):
		input = """
		main: function void (a:integer, b: string) inherit hoo{
		
		}"""
		expect = "Undeclared Function: hoo"
		self.assertTrue(TestChecker.test(input, expect, 404))

	def test5(self):
		input = """
		main: function void (a:integer, b: string) inherit hoo{
		
		}
		hoo: function void (inherit a:integer){}"""
		expect = "Invalid statement in function: main"
		self.assertTrue(TestChecker.test(input, expect, 405))

	def test6(self):
		input = """
		main: function void () inherit hoo{

		}
		hoo: function void (){}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 406))
	
	def test7(self):
		input = """
		main: function void () inherit hoo{
			super("1");

		}
		hoo: function void (inherit a: string){}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 407))
	
	
	def test8(self):
		input = """
		main: function void (z:integer, b: string) inherit hoo{
			super("1");

		}
		hoo: function void (){}"""
		expect = "Type mismatch in expression: StringLit(1)"
		self.assertTrue(TestChecker.test(input, expect, 408))
	
	def test9(self):
		input = """
		main: function void (z:integer, b: string) inherit hoo{
			super();

		}
		hoo: function void (a: string){}"""
		expect = "Type mismatch in expression: "
		self.assertTrue(TestChecker.test(input, expect, 409))


	def test10(self):
		input = """
		main: function void (z:integer, b: string) inherit hoo{
			super("1");

		}
		hoo: function void (a: string, a:string){}"""
		expect = "Type mismatch in expression: "
		self.assertTrue(TestChecker.test(input, expect, 410))

	def test11(self):
		input = """
		foo: function void (z:integer, b: string){

		}
		main: function void () inherit foo{
			super(1,"1");
		}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 411))
	
	def test12(self):
		input = """
		foo: function void (inherit z:integer, b: string){
		
		}
		main: function void () inherit foo{
			super(z,"1");
		}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 412))
	
	def test13(self):
		input = """
		foo: function void (inherit z:integer, b: string) inherit hoo{
			super(a);
		}
		hoo: function void (inherit a: string){
		}
		main:function void () {}"""	
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 413))
	
	def test14(self):
		input = """
		main: function void () inherit hoo{
			super(a);
		}
		hoo: function void (inherit a: string){
		}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 414))

	def test15(self):
		input = """
		goo: function string (inherit z:integer, b: string) inherit hoo{
			super(a);
			return	a;
		}
		hoo: function void (inherit a: string){
		}
		main:function void () {}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 415))

	def test16(self):
		input = """
		main: function string (inherit z:integer, b: string) inherit hoo{
			super(a);
			return	z;
		}
		hoo: function void (inherit a: string){
		}"""
		expect = "Type mismatch in statement: ReturnStmt(Id(z))"
		self.assertTrue(TestChecker.test(input, expect, 416))
	
	def test17(self):
		input = """
		goo: function auto (inherit z:integer, b: string) inherit hoo{
			super(a);
			return	z;
		}
		hoo: function void (inherit a: string){
		}
		main: function void(){}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 417))
	
	def test18(self):
		input = """
		main: function auto (inherit z:integer, b: string) inherit hoo{
			return	z;
		}
		hoo: function void (inherit a: string){
		}"""
		expect = "Invalid statement in function: main"
		self.assertTrue(TestChecker.test(input, expect, 418))
	
	def test19(self):
		input = """
		a : integer;
		foo: function auto (inherit z:integer, b: string){
			return	z;
		}
		main:function void() {}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 419))
	
	def test20(self):
		input = """
		a : string;
		foo: function auto (inherit a:integer, b: string){
			return a;
		}
		main: function void(){}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 420))
	
	def test21(self):
		input = """
		a : integer;
		main: function void (){
			
		}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 421))
	
	def test22(self):
		input = """
		foo: function auto (inherit z:integer, b: string) inherit hoo{
			preventDefault();
			return	z;
		}
		hoo: function void (inherit a: string){
		}
		main: function void(){}"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 422))
	
	def test23(self):
		input = """
		main: function auto (inherit z:integer, b: string) inherit hoo{
			preventDefault();
			a : integer;
			return	z;
		}
		hoo: function void (inherit a: string){
		}"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input, expect, 423))
	
	def test24(self):
		input = """a:integer = 10;
			main:function void (a:integer){}
		"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input, expect, 424))
	
	def test25(self):
		input = """a:integer = "1";
			main:function void (){}
		"""
		expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, StringLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 425))

	def test26(self):
		input = """a:integer ;
			main:function void (){
				for(a = 1, a<1, a + 1){
					break;
				}
			}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 426))
	
	def test27(self):
		input = """a:integer ;
			main:function void (){
				break;
			}
		"""
		expect = "Must in loop: BreakStmt()"
		self.assertTrue(TestChecker.test(input, expect, 427))

	def test28(self):
		input = """a:integer ;
			main:function void (){
				for(a = 1, a<1, a + 1){
					{
						break;
					}
				}
			}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 428))

	def test29(self):
		input = """a:integer ;
			main:function void (){
				for(a = 1, a<1, a + 1){
					for(a = 1, a > 2, a - 2){
						break;
					}
					continue;
				}
			}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 429))
	
	def test30(self):
		input = """a:integer ;
			main:function auto (){
				for(a = 1, a<1, a + 1){
					for(a = 1, a > 2, a - 2){
						return 2;
					}
					continue;
				}
			}
		"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input, expect, 430))
	
	def test31(self):
		input = """a:integer ;
			main:function string (){
				for(a = 1, a<1, a + 1){
					for(a = 1, a > 2, a - 2){
						return 2;
					}
					continue;
				}
			}
		"""
		expect = "Type mismatch in statement: ReturnStmt(IntegerLit(2))"
		self.assertTrue(TestChecker.test(input, expect, 431))
	
	def test32(self):
		input = """a:string ;
			foo: function void () inherit goo {
				super(a);
			}

			goo:function string (inherit x: auto){
				
			}
			main:function void(){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 432))

	
	def test33(self):
		input = """a:integer = 1 + 2;
		main:function void (){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 433))
	
	def test34(self):
		input = """a:float = 1 + 2;
		main:function void (){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 434))

	def test35(self):
		input = """a:string = 1 + 2;
		main:function void (){}
		"""
		expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, IntegerLit(1), IntegerLit(2)))"
		self.assertTrue(TestChecker.test(input, expect, 435))
	
	def test36(self):
		input = """a:string = "1"::"2";
		main:function void (){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 436))

	def test37(self):
		input = """a:float = -1.2;
		main:function void (){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 437))

	def test38(self):
		input = """a:boolean = !(true || false);
		main:function void (){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 438))

	def test39(self):
		input = """a:boolean = foo();
		main:function void (){}
		"""
		expect = "Undeclared Function: foo"
		self.assertTrue(TestChecker.test(input, expect, 439))
	
	def test40(self):
		input = """a:boolean = foo();
		foo:function boolean (){}
		main:function void(){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 440))

	def test41(self):
		input = """a:boolean = foo(foo(false));
		foo:function boolean (a: boolean){}
		main:function void(){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 441))

	def test42(self):
		input = """a:boolean = foo(foo(false));
		main: function void(){}
		foo:function auto (a: boolean){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 442))

	def test43(self):
		input = """a:integer = 1 + foo(foo(false));
		foo:function auto (a: boolean){}
		main:function void(){}
		"""
		expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), FuncCall(foo, [FuncCall(foo, [BooleanLit(False)])]))"
		self.assertTrue(TestChecker.test(input, expect, 443))

	def test44(self):
		input = """a:boolean =  main(main(false));
		b: string = main(main(false));
		main:function auto (a: boolean){}
		"""
		expect = "Type mismatch in Variable Declaration: VarDecl(b, StringType, FuncCall(main, [FuncCall(main, [BooleanLit(False)])]))"
		self.assertTrue(TestChecker.test(input, expect, 444))

	def test45(self):
		input = """a:integer = main(1);
		main:function auto (a: boolean){}
		"""
		expect = "Type mismatch in expression: FuncCall(main, [IntegerLit(1)])"
		self.assertTrue(TestChecker.test(input, expect, 445))
	
	def test46(self):
		input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType())])
		expect = "Invalid Variable: c"
		self.assertTrue(TestChecker.test(input, expect, 446))

	def test47(self):
		input = """a:integer = foo(true);
		foo:function auto (z: boolean){
			for (a=1,a<5.0, a + 2){
				break;
				return a;
			}
		}
		main:function void(){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 447))

	def test48(self):
		input = """
		foo:function integer (z: auto){
			z = 1;
		}
		main:function void (){
			a: integer = foo("1");
			b:integer = foo(2);
		}
		"""
		expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(2)])"
		self.assertTrue(TestChecker.test(input, expect, 448))

	def test49(self):
		input = """
		foo:function integer (z: auto){
			z = 1;
			z = "1";
		}
		main:function void (){
			a: integer = foo("1");
			b:integer = foo(2);
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(z), StringLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 449))
	
	def test50(self):
		input = """
		main:function void () inherit foo {
			super(1);
		}
		foo:function auto (inherit z : auto){
			 z= "5";
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(z), StringLit(5))"
		self.assertTrue(TestChecker.test(input, expect, 450))
	
	def test51(self):
		input = """
		main:function void () {
			while(true){}
		}

		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 451))

	def test52(self):
		input = """
		main:function void () {
			while(foo()){}
		}
		foo: function auto(){
			return 1;
		}
		"""
		expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 452))

	def test53(self):
		input = """
		main:function void () {
			while(foo(1)){}
		}
		foo: function auto(a: auto){
			a = true;
			return 1;
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
		self.assertTrue(TestChecker.test(input, expect, 453))

	def test54(self):
		input = """
		main:function void () {
			if(true){
				a:integer;
			}
		}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 454))

	def test55(self):
		input = """
		main:function void () {
			if(true){
				a:integer;
			}else{
				a:integer;
			}
		}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 455))

	
	def test56(self):
		input = """
		main:function void () {
			if(foo()){
				a:integer;
			}
		}
		foo: function auto (){
			return "1";
		}
		"""
		expect = "Type mismatch in statement: ReturnStmt(StringLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 456))

	def test57(self):
		input = """
		main:function void () {
			do {
				a:integer = 1;
			}while(false || true);
		}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 457))

	def test58(self):
		input = """
		main:function void () inherit foo{
			super(1);
			a = 1;
			a = true;
		}
		foo: function void (inherit a: auto){
		
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
		self.assertTrue(TestChecker.test(input, expect, 458))
	
	def test59(self):
		input = """
		main:function void () inherit foo{
			super(2);
			a = 1;
			b : integer;
			b = foo(1);
		}
		foo: function auto (inherit a: auto){
			return false;
		}
		"""
		expect = "Type mismatch in statement: ReturnStmt(BooleanLit(False))"
		self.assertTrue(TestChecker.test(input, expect, 459))
	
	def test60(self):
		input = """
		main:function void () inherit foo{
			preventDefault();
			a = 1;
		}
		foo: function auto (inherit a: auto){
			a = true;
		}
		"""
		expect = "Undeclared Identifier: a"
		self.assertTrue(TestChecker.test(input, expect, 460))

	def test61(self):
		input = """
		main:function void () {
			
		}
		goo:function string (a:string){}
		foo: function auto ( a: auto){
			goo(a);
			a = 1;

		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(a), IntegerLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 461))

	def test62(self):
		input = """
		main:function void () {
			goo(foo());
			a : integer = foo();
		}
		goo:function string (a:string){}
		foo: function auto (){}
		"""
		expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"
		self.assertTrue(TestChecker.test(input, expect, 462))

	def test63(self):
		input = """
		test: function string (y : auto){
			 y = 2;
			 return "1";
		}
		main:function void (){
			test(true);
		}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 463))

	def test64(self):
		input = """
		a: array [1] of integer = {"1"};
		"""
		expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1], IntegerType), ArrayLit([StringLit(1)]))"
		self.assertTrue(TestChecker.test(input, expect, 464))

	def test65(self):
		input = """
		a: array [1] of integer = {"1",1};
		"""
		expect = "Illegal array literal: ArrayLit([StringLit(1), IntegerLit(1)])"
		self.assertTrue(TestChecker.test(input, expect, 465))
	
	def test66(self):
		input = """
		a: array [1,2] of integer = {{1,1}, {"a","a"}};
		"""
		expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([StringLit(a), StringLit(a)])])"
		self.assertTrue(TestChecker.test(input, expect, 466))

	def test67(self):
		input = """
		a: array [1,2] of integer = {{{2},{2}}};
		"""
		expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(2)])])]))"
		self.assertTrue(TestChecker.test(input, expect, 467))

	def test68(self):
		input = """
		a: auto;
		"""
		expect = "Invalid Variable: a"
		self.assertTrue(TestChecker.test(input, expect, 468))

	def test69(self):
		input = """
		a: array [1] of integer;
		main: function void (){
			a[0] = 1; 
		}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 469))

	def test70(self):
		input = """
		a: array [1] of integer;
		main: function void (){
			a[0] = "1"; 
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 470))

	def test72(self):
		input = """
		a: array [1] of integer;
		main: function void (){
			a = {"1"}; 
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(a), ArrayLit([StringLit(1)]))"
		self.assertTrue(TestChecker.test(input, expect, 472))

	def test73(self):
		input = """
		a: array [1] of integer;
		main: function void (){
			a = {1,1}; 
		}
		"""
		expect = "Type mismatch in statement: AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(1)]))"
		self.assertTrue(TestChecker.test(input, expect, 473))

	def test74(self):
		input = """
		sub:function auto (){
		return 1;
		}
		x: float = sub() + 2.0;
		y: integer = sub();
		main: function void (){}
		"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 474))
	

	def test75(self):
		input = """
		main: function void() {
            a: string = "ghgf"::Ha({{{1,2,3}}});
        }
        
        Ha: function string(e:array [1,1,3] of integer) {
            return e[1,2+e[1,1]];
        }
        
        Ha: function auto() {
            a: auto = {{1,2,3},{1,2,3}};
            return a;
        }"""
		expect = "Type mismatch in expression: BinExpr(+, IntegerLit(2), ArrayCell(e, [IntegerLit(1), IntegerLit(1)]))"
		self.assertTrue(TestChecker.test(input, expect, 475))
	
	def test76(self):
		input = """
		foo : function auto () {
			if (true) {
       	 		return 4;
    		} else {
        		return true;
    		}
		}"""
		expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
		self.assertTrue(TestChecker.test(input, expect, 476))

	def test77(self):
		input = """
		foo : function auto () {
			return 1;
			return "2";
		}"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input, expect, 477))

	def test78(self):
		input = """
		foo : function auto () {
			if(true){
				return "a";
			}
			return 1;
		}"""
		expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 478))

	
	def test80(self):
		input = """
        foo:function void() inherit main {
			preventDefault();
        }
        
        main: function void() {
            a:integer;
        }"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 480))

	def test81(self):
		input = """
        foo:function void() inherit main {
			preventDefault(1);
        }
        
        main: function void() {
            a:integer;
        }"""
		expect = "Type mismatch in expression: IntegerLit(1)"
		self.assertTrue(TestChecker.test(input, expect, 481))

	def test82(self):
		input = """
            foo: function integer (a:integer){
               for (a = "1",a<1, 1){}
            }
            """
		expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 482))
	
	def test83(self):
		input = """
            foo: function integer (a:auto){
               for (a = 1,a<1, 1){}
	       		a = "a";
            }
            """
		expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(a))"
		self.assertTrue(TestChecker.test(input, expect, 483))

	def test84(self):
		input = """
            foo: function integer (a:auto){
               for (a = "1",a<1, 1){}
	       		a = "a";
            }
            """
		expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(1))"
		self.assertTrue(TestChecker.test(input, expect, 484))

	def test85(self):
		input = """
			sqrt:function float (delta:float){}
            quadratic_equation_solver: function array [2] of float (a:float,b:float,c:float){
                delta:float = b*b - 4*a*c;
                x1:float = (-b - sqrt(delta))/(2*a) ;
                x2:float = (-b + sqrt(delta))/(2*a) ;
                return {x1,x2};
            }
            main:function void (){
                writeFloat(quadratic_equation_solver(1,2,1));
            }
        """
		expect = "Type mismatch in statement: CallStmt(writeFloat, FuncCall(quadratic_equation_solver, [IntegerLit(1), IntegerLit(2), IntegerLit(1)]))"
		self.assertTrue(TestChecker.test(input, expect, 485))

	def test86(self):
		input = """
			sqrt:function float (delta:float){}
            quadratic_equation_solver: function array [2] of float (a:float,b:float,c:float){
                delta:float = b*b - 4*a*c;
                x1:float = (-b - sqrt(delta))/(2*a) ;
                x2:float = (-b + sqrt(delta))/(2*a) ;
                return x1 * x2;
            }
            main:function void (){
                writeFloat(quadratic_equation_solver(1,2,1));
            }
        """
		expect = "Type mismatch in statement: ReturnStmt(BinExpr(*, Id(x1), Id(x2)))"
		self.assertTrue(TestChecker.test(input, expect, 486))

	def test87(self):
		input = """
			sqrt:function float (delta:float){}
            quadratic_equation_solver: function float (a:float,b:float,c:float){
                delta:float = b*b - 4*a*c;
                x1:float = (-b - sqrt(delta))/(2*a) ;
                x2:float = (-b + sqrt(delta))/(2*a) ;
                return x1 * x2;
            }
            main:function void (){
                writeFloat(quadratic_equation_solver(1,2,1));
            }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 487))

	def test88(self):
		input = """
            quadratic_equation_solver: function float (a:float,b:float,c:float){
				return a;
				return "1";
				return true;
            }
            main:function void (){
                writeFloat(quadratic_equation_solver(1,2,1));
            }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 488))

	def test89(self):
		input = """
            quadratic_equation_solver: function float (a:float,b:float,c:float){
				if(true){
					return 1;
				}
				return true;
            }
        """
		expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
		self.assertTrue(TestChecker.test(input, expect, 489))

	def test90(self):
		input = """
            quadratic_equation_solver: function float (a:auto,b:float,c:float){
				if(true){
					return a;
				}
				return true;
            }
        """
		expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
		self.assertTrue(TestChecker.test(input, expect, 490))

	def test91(self):
		input = """
            quadratic_equation_solver: function float (a:auto,b:float,c:float){
				if(true){
					return a;
				}
				a = true;
            }
        """
		expect = "Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"
		self.assertTrue(TestChecker.test(input, expect, 491))

	def test92(self):
		input = """
			sqrt:function float (delta:float){}
            quadratic_equation_solver: function array [2] of float (a:float,b:float,c:float){
                delta:float = b*b - 4*a*c;
                x1:float = (-b - sqrt(delta))/(2*a) ;
                x2:float = (-b + sqrt(delta))/(2*a) ;
                return {x1 , x2};
            }
	     	 quartic_equation_solver: function array [4] of float(a:float,b:float,c:float){
                res: array [2] of float = quadratic_equation_solver(a,b,c);
                x1,x2,x3,x4:float = -sqrt(res[0]),sqrt(res[0]),-sqrt(res[1]),sqrt(res[1]);
                return {x1,x2,x3,x4};
            }

            main:function void (){
				res: array [4] of float = quartic_equation_solver(1,2,1);
                writeFloat(res[0]);
            }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 492))

	def test93(self):
		input = """
            a:string = "Hello world";
	    	main: function void (){
				a = "Hi" :: (a :: a);
				i: float = 2;
				while (true){
					if (i > 4) printString(a);
					else break;
					i = i -1;
				}

			}
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 493))

	def test94(self):
		input = """
	    	main: function void (){
				a:string = "a";
				i: float = 2;
				while (true){
					if (i > 4) printString(a);
					else while (true){
						if (i > 4) printString(a);
						else while (true){
							if (i > 4) printString(a);
							else break;
							i = i -1;
						}
						i = i -1;
						continue;
					}
					i = i -1;
					break;
				}

			}
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 494))

	

	def test96(self):
		input = """
	    	main: function void (){
				a : array [1,2,3,4] of integer = {{{{1,1,1,1},{1,1,1,1},{1,1,1,1}},{{1,1,1,1},{1,1,1,1},{1,1,1,1}}}};
				a[1*a[1,1,1,1],2-3*4+5,a[1,2,3,4]::"2"]= {1,2,3,4};
			}
        """
		expect = "Type mismatch in expression: BinExpr(::, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), StringLit(2))"
		self.assertTrue(TestChecker.test(input, expect, 496))

	def test97(self):
		input = """
	    	main: function void (){
				a : array [1,2,3,4] of string;
				a["1"::a[1,1,1,1],2-3*4+5,a[1,2,3,4]::a[2,3,4,5]]= {1,2,3,4};
			}
        """
		expect = "Type mismatch in expression: ArrayCell(a, [BinExpr(::, StringLit(1), ArrayCell(a, [IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(1)])), BinExpr(+, BinExpr(-, IntegerLit(2), BinExpr(*, IntegerLit(3), IntegerLit(4))), IntegerLit(5)), BinExpr(::, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayCell(a, [IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))])"
		self.assertTrue(TestChecker.test(input, expect, 497))

	def test98(self):
		input = """
	    	main: function void (){
				readFloat();
			}
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 498))

	def test99(self):
		input = """
	    	main: function void (){
				a: array[1,2] of float = {{readFloat(),readFloat()}};
			}
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 499))

	def test100(self):
		input = """
	    	main: function void (){
				a: integer;
				for (a=1, a < 2, a -1){
					continue;
					do {
						break;
						c : array[2] of boolean;
						b:boolean = true||false&&c[1,2];
					}while(false);
				}
			}
        """
		expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1), IntegerLit(2)])"
		self.assertTrue(TestChecker.test(input, expect, 500))


