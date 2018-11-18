"""
    Tests Wang Parser
    See grammar/Wang.g4
    based on jszheng git https://github.com/jszheng/py3antlr4book Example calc
    Extended by loriacarlos@gmail.com
    
"""
__author__ = 'jszheng'
__coauthor__ = 'loriacarlos@gmail.com'

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from antlr4.InputStream import InputStream
from WangLexer import WangLexer
from WangParser import WangParser
from visitor import WangPrintVisitor

class MyErrorListener(ErrorListener):
    """
        Based on https://stackoverflow.com/questions/18132078/handling-errors-in-antlr4
    """
    def syntaxError(self,  recognizer, 
                            offendingSymbol,
                            line, 
                            charPositionInLine,
                            msg, 
                            e):
        error_msg = f"{self.__class__.__name__}: line {line}: {charPositionInLine} {msg}"
        raise SyntaxError(error_msg)

if __name__ == '__main__':
    print("*** Testing Wang Parser (EIF400 II-2018) ***")
    if len(sys.argv) > 1:
        file = sys.argv[1]
        print(f'*** Processing from file "{file}" ***')
        input_stream = FileStream(file)
    else:
        print(f'*** Processing from console ***\n>', end='')
        to_parse_line = sys.stdin.readline()
        # Use demo line if none was typed
        if len(to_parse_line) <= 1: # Just enter was hit
            to_parse_line = "q1 | q2 & q3 => q1, q2"
            print(f"Empty line. Testing with demo: {to_parse_line}")
        #
        input_stream = InputStream(to_parse_line)
        
    # Setup Lexer 
    print(f"Data:\n{input_stream}")
    lexer = WangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    #Setup Parser (and own ErrorListener)
    parser = WangParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    try:
        tree = parser.assertion()
    except SyntaxError as e:
        print(e.msg)
        sys.exit(-1)
    #Setup the Visitor and visit Parse tree
    visitor = WangPrintVisitor()
    print("*** Starts visit of data ***")
    res = list(visitor.visit(tree))
    for i in range(len(res)):
        print(f"Resultado: {res[i]}")
    
