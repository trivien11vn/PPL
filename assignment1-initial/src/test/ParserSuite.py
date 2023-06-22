import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """ fact: function integer (n: integer) {
            for (i=1, i<10,i+1) {
                a= {1,2};
            {
               a: integer; 
            }
            }
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_2(self):
        input = """ fact: function integer (n: integer) {
            for (i=1, i<10,i+1) {
                a= 2==3;
            {
               return;
            }
            }
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_3(self):
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_4(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_5(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_6(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_7(self):
        input = """if (n == 0) return 1;"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_8(self):
        input = """a : array [2,3] of integer = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_9(self):
        input = """a : integer = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_10(self):
        input = input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            
            else return n * fact(n - 1);
            {
                
            }
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_11(self):
        input = input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            
            else return n * fact(n - 1);
            {
                ;
            }
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        """
        expect = "Error on line 7 col 16: ;"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_12(self):
        input = input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            
            else return n * fact(n - 1);
            {
                
            }
        }
        inc: function void(out n: integer, delta: integer) inherit abc {
            n = n + delta;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_13(self):
        input = input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            
            else return n * fact(n - 1);
            {
                
            }
        }
        inc: function void(out n: integer, delta: integer) inherit abc {
            n = abc(2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_14(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            n = (2+3);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_15(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            n = a[2==3,a>3];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test_16(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            n = readBoolean() ;
        }      
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test_17(self):
        input = """
        a:integer;
          fact: function integer (){
              do {x =2 ;}
              while(true);
              a=2;
              a: integer;
              return "123";
              a=2;
              return "123";
          }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_18(self):
        input = """
        a:integer;
          fact: function integer (){
              do {x = {1,2,3} ;}
              while (true);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_19(self):
        input = """
        a:integer;
          fact: function integer (){
              do {x = {1,2,3,.123e+10} ;}
              while (true);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_20(self):
        input = """
        a:integer;
          fact: function integer (){
              do {x = {1,2,3,01} ;}
              while (true);
            }  
        """
        expect = "Error on line 4 col 30: 1"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_21(self):
        input = """
        a:integer=1;
          fact: function integer (){
              do {x = {1,2,3,01} ;}
              while (true);
            }  
        """
        expect = "Error on line 4 col 30: 1"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_22(self):
        input = """
        a:integer;
          fact: function integer (){
              a = 1;
              do {x = {1,2,3,1} ;}
              while (true);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_23(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              a = 1;
              do {x = {1,2,3,1} ;}
              while (true);
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_24(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {}
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_25(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_26(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {
                  {  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_27(self):
        input = """
        a:integer = a[1];
          fact: function integer (){
              {
                  {  
                  return {12_3.e+5,123,"he ask me \\"",true, a[1,2],foo()};
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_28(self):
        input = """
        a:integer = "he aske me\n";
          fact: function integer (){
              {
                  {  
                  return {12_3.e+5,123,"he ask me \\"",true, a[1,2],foo()};
                  }
              }
            }  
        """
        expect = "he aske me"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_29(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  return {12_3.e+5,123,"he ask me \\"",true, a[1,2],foo()};
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_30(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  return ;
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))  
    def test_31(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  if(x==2);
                  else ;
                  }
              }
            }  
        """
        expect = "Error on line 6 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 231)) 
    def test_32(self):
        input = """
        a:integer = truee;
          fact: function integer (){
              {
                  {  
                  if(x==2);
                  else ;
                  }
              }
            }  
        """
        expect = "Error on line 6 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 232)) 
    def test_33(self):
        input = """
        a:integer = 1 ;
          fact: function integer (){
              {
                  {  
                  if(x==2) a=2;
                  else a=2;
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233)) 
    def test_34(self):
        input = """
        a,b,c:integer =1 ;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "Error on line 2 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_35(self):
        input = """
        a,b,c:integer =1,a[2[3]],3;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_36(self):
        input = """
        a,b,c:integer =1,a[a[3]],3;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_37(self):
        input = """
        a,b,c:integer =1,a[a[3]],3;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_38(self):
        input = """
        a,b,c:array [2_1_2,3_1] of string;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_39(self):
        input = """
        a,b,c:array [2_1_2,3_] of string;
          fact: function integer (){
              {
                  {  
                  
                  }
              }
            }  
        """
        expect = "Error on line 2 col 28: _"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_40(self):
        input = """
        a,b,c:array [2_1_2,3] of string; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_41(self):
        input = """
        a,b,c: auto; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_42(self):
        input = """
        a,b,c: void; 
        """
        expect = "Error on line 2 col 15: void"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_43(self):
        input = """
        _a_,b,c: string ; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_44(self):
        input = """
        _a_,0b,c: string ; 
        """
        expect = "Error on line 2 col 12: 0"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_45(self):
        input = """
        _a_,_0b,c: boolean ; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_46(self):
        input = """
        _a_,_0b,c: float; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_47(self):
        input = """
        _a_,_0b,c: float; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_48(self):
        input = """
        /* 0a:integer;
        */
        a: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_49(self):
        input = """
        // 0a:integer;
        
        a: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_50(self):
        input = """
        // 0a:integer;
        
        a: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_51(self):
        input = """
        // 0a:integer;
        
        {}
        """
        expect = "Error on line 4 col 8: {"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_52(self):
        input = """
        a:integer = a[1];
          fact: function integer (inherit out x:integer){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_53(self):
        input = """
        a:integer = a[1];
          fact: function integer (inherit x:integer){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_54(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:integer){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_55(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:void){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "Error on line 3 col 40: void"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_55(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:void){
              {
                  {
                      
                  }
              }
            }  
        """
        expect = "Error on line 3 col 40: void"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_56(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,2==3];
              if(x>3) a=2;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_57(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,foo(2)];
              if(x>3) a=2;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_58(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,foo(x,2),c[1]];
              if(x>3) a=2;
            }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_59(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              if(x==2) a=b[2,foo(x,2),c[1]];
              if(x>3) a=2;
              a= 2==3;
              a= (2+3);
              for(arr[1]=0, arr[1]<10,arr[1]+1);
              while(x<2)x=x+1;
            }  
        """
        expect = "Error on line 8 col 47: ;"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_60(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              for (i = 1, i < 10, i + 1) {
                writeInt(i);
                {
                    ;
                }
            }
            }  
        """
        expect = "Error on line 7 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_61(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              for (i = 1, i < 10, i + 1) {
                writeInt(i);
                {
                    ;
                }
            }
            }  
        """
        expect = "Error on line 7 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_62(self):
        input = """
        a:integer = a[1];
        return ;
          fact: function integer (out x:string){
              for (i = 1, i < 10, i + 1) {
                writeInt(i);
                {
                    ;
                }
            }
            }  
        """
        expect = "Error on line 3 col 8: return"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_63(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              {
                  
              
            } 
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_64(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              while(x==2) a=3;}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_65(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              do ;
              while (x>=2);
            }
        """
        expect = "Error on line 4 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_66(self):
        input = """
        a:integer = a[1];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_67(self):
        input = """
        a:integer = a[1,{1,2,3}];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_68(self):
        input = """
        a:integer = a[1,/*111_*/2];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_69(self):
        input = """
        a:integer = a[1,/*111_*/2_];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 33: _"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_70(self):
        input = """
        a:integer = a[1,2/*111_*///aa];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 3 col 10: fact"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_71(self):
        input = """
        a:integer = a[1,foo(1,{1,2,3}),boolean];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 39: boolean"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_72(self):
        input = """
        a:integer = a[1,foo(1,{1,2,3}),integer];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 39: integer"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_73(self):
        input = """
        a:integer = a[1,foo(1,{1,2,3}),float];
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 39: float"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_74(self):
        input = """
        a:integer = aa :: bb;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_75(self):
        input = """
        a:integer = aa :: bb :: cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 29: ::"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_76(self):
        input = """
        a:integer = (aa :: bb) :: cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_77(self):
        input = """
        a:integer = (aa == bb) >= cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_78(self):
        input = """
        a:integer = aa == bb >= cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "Error on line 2 col 29: >="
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_79(self):
        input = """
        a:integer = (aa && bb)&&cc;
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_80(self):
        input = """
        a:integer = 1 && (bb&&cc);
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_81(self):
        input = """
        a:integer = {foo(1,2),2};
          fact: function integer (out x:string){
              a=a[2,3];
              b= {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_82(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    n = n - delta - hallo;
                    n = n * delta * hallo;
                    /* multiple
                        line
                        comment
                    */
                    n = a[1, a[1, a[1,2]]]; // n[1,2] = 2 => n = a[1,2];
                    return n;
        """
        expect = "Error on line 16 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_83(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    n = n - delta - hallo;
                    n = n * delta * hallo;
                    /* multiple
                        line
                        comment
                    */
                    n = a[1, a[1, a[1,2]]]; // n[1,2] = 2 => n = a[1,2];
                    return n;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_84(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    return ;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_85(self):
        input = """
        a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    return ;
                    ;
                    }
        """
        expect = "Error on line 9 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_86(self):
    
        input = """
        learningtofly: function integer() {
                for (i = -foo(), i < 10, i :: -2 :: 3E-10) {
                    a = ---a;
                    }
        }
        """
        expect = "Error on line 3 col 49: ::"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_87(self):
        input = """
        main: function void () {
           for (i = 1, i < 10, i + 1) {
                writeInt(i);
                }
                return "aa"::"bb";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_88(self):
        input = """
            main:function void()
            {
                a:string="aaa"::"bbb"=="ccc";
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_89(self):
        input = """
            main:function void()
            {
                a:string="aaa"::"bbb"::"ccc";
                return;
            }
        """
        expect = "Error on line 4 col 37: ::"
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_90(self):
        input = """
            main:function void()
            {
                a:string="aaa">="bbb">="ccc";
                return;
            }
        """
        expect = "Error on line 4 col 37: >="
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_91(self):
        input = """
            main:function void()
            {
                a:string="aaa">=("bbb">="ccc");
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_92(self):
        input = """
            main:function void()
            {
                a:string="aaa"<=("bbb"<="ccc");
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_93(self):
        input = """
            main:function void()
            {
                a:string="aaa"<="bbb">="ccc";
                return;
            }
        """
        expect = "Error on line 4 col 37: >="
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_94(self):
        input = """
            main:function void()
            {
                a:string="aaa"<"bbb">"ccc";
                return;
            }
        """
        expect = "Error on line 4 col 36: >"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_95(self):
        input = """
           main:function void()
            {
                a:boolean=1==1!=1;
                return;
            }
        """
        expect = "Error on line 4 col 30: !="
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_96(self):
        input = """
           
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_97(self):
        input = """
           main:function boolean()
            {
                a:integer = ---3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_98(self):
        input = """
           main:function boolean()
            {
                a:integer = -(2+3);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_99(self):
        input = """
           a,b: float = 1_.2;
        """
        expect = "Error on line 2 col 25: _"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test_100(self):
        input = """
           a,b: float = 1_2.2;
        """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input, expect,300))
    


