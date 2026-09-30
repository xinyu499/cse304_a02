#XinyuHe ID:116048576

import sys
from decaf_lexer import lexer
from decaf_parser import parser

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    lexer.lineno = 1
    parser.parse(data, lexer=lexer)
    print("Yes")

if __name__ == "__main__":
    main()