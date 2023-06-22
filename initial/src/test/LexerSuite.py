import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_one(self):
        """test one"""
        testcase =	"'Yanxi Palace - 2018'"
        expect =  "'Yanxi Palace - 2018',<EOF>"
        self.assertTrue(TestLexer.test(testcase,expect,100))