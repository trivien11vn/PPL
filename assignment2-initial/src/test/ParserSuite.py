import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    
    def test1(self):
        """test variable declaration"""
        input = """ a,b,c : string; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test2(self):
        input = """ a,b,c : string = "a","b","c"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        input = """a,b,c : string = "a","b","c","d"; """
        expect = "Error on line 1 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4(self):
        input = """ a,b,c,d : string = 1,2,3; """
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    def test5(self):
        input = """a,b,c,d : string = a[1],b+d,{123,4},foo(goo(hoo())) ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    """function declaration"""
    def test6(self):
        input = """
            main: function integer (){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        input = """ 
            main:function array [2,2] of string (out b: string){
                for(i = -a[b[c["2"]]] , (i+4 > 5) == true, a * -goo()){
                    {{}}
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        input = """
            fact: function void (inherit out x : void){
                
            }
        """
        expect = "Error on line 2 col 49: void"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        input = """
            fact: function integer(a,b: array){
                
            }
        """
        expect = "Error on line 2 col 36: ,"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        input = input = """
            main: function void () {
                x = foo(-{1,2,3});
                while (true) {
                    do
                    while(false);
                }
            }
        """
        expect = "Error on line 6 col 20: while"
        self.assertTrue(TestParser.test(input, expect, 210))

    """ test statement """
    def test11(self):
        input = input = """
            if(i) return 1;
        """
        expect = "Error on line 2 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        input = input = """
        main: function void (){
            if (i) return 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        input = """
            main: function void (){
                x: integer = 1;
                x = x + -foo(b,c,d,e);
                if(x) return 1;
                else return 3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = """
        main: function void (inherit out x: string){
            if(true){
                id = (------------id == 21) > 4;
            }
            else {
                if(false){}else{}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        input = """
            main:function void (){
                if (x) 
                    if(y) return 1; 
                    else return 2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test16(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            if(--a[foo(8,{1,3,4}),a[a[a[5]]]]) return;
            else 
                if (_1) return a==2+d; 
                else return true;
        }      
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test17(self):
        input = """
          fact: function integer (){
              if(if) return 3;
          }  
        """
        expect = "Error on line 3 col 17: if"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """
            fibo: function integer (n: integer){
                if (n==1) return 1;
                if (n==0) return 0;
                return n + fibo(n-1);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """
        main: function void (){
            while(true)
                do{
                    a[-"a"]=b>d;
                }while(1);
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """
            main: function string(out inherit x: array [1] of string){}  
        """
        expect = "Error on line 2 col 38: inherit"
        self.assertTrue(TestParser.test(input, expect, 220))


    def test21(self):
        input = """
            test : function void (inherit out x : integer){
                test1: function void(){}
            }
        """
        expect = "Error on line 3 col 23: function"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        input = """
            __init__:function void(){
                input = self = input;
            }
        """
        expect = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """
            a:integer = a[1];
            b: string = {-foo(),123,"string"};
            sum: function integer(a:integer, b:integer){
                return (a+b);
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test24(self):
        input = """
            max:function integer (x:integer, y:integer){
                if (x > y)
                    return x;
                else
                    return y;
            }  
            main:function void(){
                m:integer = max(9,!-1);
                print(m);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    
    def test25(self):
        input = """
        sub: function integer(){{{{
            do x = x + 1;
            while(true)
        }}}}  
        """
        expect = "Error on line 3 col 15: x"
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test26(self):
        input = """
            True:function boolean(x:integer = true){
                return true;
            }  
        """
        expect = "Error on line 2 col 44: ="
        self.assertTrue(TestParser.test(input, expect, 226))
    
    def test27(self):
        input = """
            I_Luv_U: function string(life: integer){
                while(life != end){
                    print("I" + "Will" + "Keep" + "Loving" + "You");
                    life = life + 1;
                }
                return I_Luv_U(life-life);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """
            main:function void(){
                return main(-main((-main----main+-main(main[1,main()]))))
            }  
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """
            Travelling_path: function string(start: string,end:string){
                while(start!=end!=end){}
            }   
        """
        expect = "Error on line 3 col 32: !="
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """
            Travelling_path: function string(start: string,end:string){
                while(start!=end){
                    path = path + start;
                    start = nextDest(start);
                }
                return path;
            }   
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))  


    def test31(self):
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 231)) 


    def test32(self):
        input = """
            x:integer = {1,2,3==4>6}  
        """
        expect = "Error on line 2 col 33: >"
        self.assertTrue(TestParser.test(input, expect, 232)) 
    
    def test_33(self):
        input = """
            x:integer = {1,2,3==foo()+(4>6)} ;  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233)) 
    
    def test34(self):
        input = """
          fact: function integer (){
              {
                  {  
                    return;
                  }
              }  
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test35(self):
        input = """
          fact: function integer (){
              {
                  {  
                    a = b[];
                  }
              }
            }  
        """
        expect = "Error on line 5 col 26: ]"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """
          a: integer = (a+b)[1];  
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """
          fact: function integer (){
            while(true) print(expr);
            a[foo(a[-1])[2,foo()]] = id[id]; 
          }
  
        """
        expect = "Error on line 4 col 24: ["
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """a,b,c: string = "\\"123 ;  """
        expect = """\\"123 ;  """
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """
            a,_ : auto = _,_;
            main:function void (){
                x: void ;
            }
        """
        expect = "Error on line 4 col 19: void"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """a,b,c:array [2_1_2e-10,3] of string; """
        expect = "Error on line 1 col 13: 212e-10"
        self.assertTrue(TestParser.test(input, expect, 240))

    
    def test41(self):
        input = """a: array [2] of integer = {}; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """
        a,b,c: array [] of integer; 
        """
        expect = "Error on line 2 col 22: ]"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """a: array[index] of integer; """
        expect = "Error on line 1 col 9: index"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """
            main: function void (){
                a:string = "\nabc\\n";
            }  
        """
        expect = ""
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """
            isEqual: function boolean (_1:string, _2:string){
                return _1==_2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """_x_:string = {{\n}}; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """_x_:string = {{\\n}}; """
        expect = "\\"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """//if(a==1) return 2;"""
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """
            /* This 
            is 
            a 
            comment */
            concat:function string(string1:string, string2:string){
                return string1::string2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """
            concat:function string(string1:string,string2:string,string3:string){
                return string1::string2::string3;
            }
        """
        expect = "Error on line 3 col 39: ::"
        self.assertTrue(TestParser.test(input, expect, 250))
    

    def test51(self):
        input = """
            concat:function string(string1:string,string2:string,string3:string){
                return {(string1::(string2::string3))};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test52(self):
        input = """
            main:function void (){
                a = a+b::c+d;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """
            func: function array [2,2] of integer (){
                return {1},{2},{3};
            }  
        """
        expect = "Error on line 3 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test54(self):
        input = """
            arr:function integer () {
                return {{},{},{}};
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """
            &a = c + d;  
        """
        expect = "&"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test56(self):
        input = """
            test: function integer () inherit t {
                return true||false::"a";
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """
              test: function integer () inherit t {
                return true==false>=x;
            } 
        """
        expect = "Error on line 3 col 34: >="
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """
            break;
        """
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """
            fact: function integer (out x:string){
                ma,n={1,2,3},4;
            }  
        """
        expect = "Error on line 3 col 20: ="
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        input = """
            main:function string(){
                self.val = 1;
            }
        """
        expect = "Error on line 3 col 20: ."
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        input = """
            a:string = {"}"}; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        input = """
            program: function string(){
                for (i = foo(goo(hoo({1,2,3}))), (x+2)==(z>=a[4]), a[{1}] + 1)
                {
                
                }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test63(self):
        input = """
            func:function void() {
                a[1::2] = 1;
                return;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        input = """
            hpt: string = "dep trai\\n";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """
            hpt: string = "dep trai\\" ;
        """
        expect = "dep trai\\\" ;"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        input = """
            /* @#$%^^&************(())*/
            factorial: function float (n:float){
                if (n==1) return 1;
                return n * factorial(n-1);

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        input = """
            floaT: function float (){
                return 1.;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """
            main:function float (){
                foo(1.E-10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        input = """
            main:function float(){
                foo(goo(););
            }
        """
        expect = "Error on line 3 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """
        a:integer = a[1,/*111_*///aa];
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 270))
    
    def test71(self):
        input = """
            b:string = /*/*/* 123 */;
        """
        expect = "Error on line 2 col 28: *"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        input = """
            main:function array [-1] of integer (){}
        """
        expect = "Error on line 2 col 33: -"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test73(self):
        input = """
            main:function void(){
                a = /*/*/ "abc\rcba";
            }
        """
        expect = "abc"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
            fact: function integer (inherit x:string){
                \n\n\n\n\n
                a="!@#$%^&";
                b
            }
        """
        expect = "Error on line 11 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test75(self):
        input = """
            _1:string = ("asd"::123)::foo(bc::{123,321});
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        input = """
             _1:string = ("asd"::123)::(a[4]::foo(bc::{123,321}));
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        input = """
            _1:string = "asd"::(123::a[4])::foo(bc::{123,321});
        """
        expect = "Error on line 2 col 42: ::"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test78(self):
        input = """
            new_func_: function integer (out x:string){
              a=a[2_3_________,3];
            }
        """
        expect = "Error on line 3 col 21: _________"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        input = """
            HpTIsmE: function integer (out x:string){
                a_b_c_=1_2_3_4_5.E-9;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test80(self):
        input = """
            x: float = 1_2_3.e-10 + ---2_3_4.E20;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test81(self):
        input = """
            main: function void(x:integer){
                for(a[2]=--------goo(),-"a" == "a"::a, a[a[a[a[a[a[a[4]]]]]]] <= true){
                    do{
                        while(false) x = x - + 4;
                    }while(true);
                }
            }
        """
        expect = "Error on line 5 col 45: +"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test82(self):
        input = """
            quadratic_eqation_solver: function float(a:float,b:float,c:float){
                delta = b*b - 4*a*c;
                x1 = (-b - sqrt(delta))/(2*a) ;
                x2 = (-b + sqrt(delta))/(2*a) ;
                return {x1,x2};
            }
            main:function void (){
                print(quadratic_equation_solver(1,2,1));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test83(self):
        input = """
            quadratic_eqation_solver: function float(a:float,b:float,c:float){
                delta = b*b - 4*a*c;
                x1 = (-b - sqrt(delta))/(2*a) ;
                x2 = (-b + sqrt(delta))/(2*a) ;
                return {x1,x2};
            }
            quartic_equation_solver: function float(a:float,b:float,c:float){
                res: array [2] of float = quadratic_equation_solver(a,b,c);
                x1,x2,x3,x4:float = -squrt(res[0]),sqrt(res[o]),-sqrt(res[1]),sqrt(res[1]);
                return {x1,x2,x3,x4};
            }
            main:function void (){
                print(quartic_equation_solver(1,2,1));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test84(self):
        input = """
            //Hello world in MT22 language
            main: function void(){
                printStr("Hello world");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test85(self):
        input = """
            main: function void () {
                if(this) a = +foo;
            }
        """
        expect = "Error on line 3 col 29: +"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        input = """
            eat: function void(animal: string){
                if (animal=="dog") food = meat;
                else if (animal == "cat") food = fish;
                else food = worm;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,286))

    def test87(self):
        input = """
            a >> b;
        """
        expect = "Error on line 2 col 14: >"
        self.assertTrue(TestParser.test(input, expect, 287))
    
    def test88(self):
        input = """
            eat: function void(animal: string){
                if (animal=="dog") food = meat;
                else {if (animal == "cat") food = fish;}
                else food = worm;
            }
        """
        expect = "Error on line 5 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        input = """
            eat: function void(animal: string){
                if (animal=="dog") {food = meat;}
                else {if (animal == "cat") {food = fish;}
                else {food = worm;}}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        input = """
            main:function void (){
                do{
                    a = ("123" >= "321")::-123_321.E;
                }while(true);
            }
        """
        expect = "Error on line 4 col 51: E"
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test91(self):
        input = """
            main: function void(){
                for(a["ds"::cd]=goo(),"+++a" == "$a%"::1_a, _ <= true){
                    do{
                        
                    }while(true);
                }
            }
        """
        expect = "Error on line 3 col 56: _a"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        input = """
            "<EOF>"
        """
        expect = "Error on line 2 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        input = """
            def:function void(){
                a: array[1] of array [1] of integer;
            }
        """
        expect = "Error on line 3 col 31: array"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test94(self):
        input = """
            arr:array [2,3] of auto;
        """
        expect = "Error on line 2 col 31: auto"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        input = """
            a,b : function void(){}
        """
        expect = "Error on line 2 col 18: function"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        input = """
            _1:integer = 1;
            _2:integer = 2;
            main: function void(_1:integer){
                _1 = _2 * _2 / a ///*/*/*/*asdasd*/ ;
            }
        """
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect,296))

    def test97(self):
        input = """
            bool1,bool2:boolean = a[true],b[false];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test98(self):
        input = """
            main: function boolean (x:boolean){
                {
                    if(1) do{
                    
                    }while(a);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """
            a: string = "\\n\\r\\t\\d ";
        """
        expect = "\\n\\r\\t\\d"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test100(self):
        input = """
            main:function void(){
                foo(
                    3,
                    4,
                    -goo(),
                    a[t],
                    .E2
                )
                ;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
    
