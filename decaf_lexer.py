#XinyuHe ID:116048576

import sys
import ply.lex as lex


reserved = {
    'boolean': 'BOOLEAN', 'break': 'BREAK', 'continue': 'CONTINUE', 'class': 'CLASS', 'else': 'ELSE', 'extends': 'EXTENDS',
    'false': 'FALSE', 'float': 'FLOAT', 'for': 'FOR', 'if': 'IF', 'int': 'INT', 'new': 'NEW', 'null': 'NULL', 'private': 'PRIVATE',
    'public': 'PUBLIC', 'return': 'RETURN', 'static': 'STATIC', 'super': 'SUPER', 'this': 'THIS', 'true': 'TRUE', 'void': 'VOID', 'while': 'WHILE',
}

tokens = [
    'ID', 'INT_CONST', 'FLOAT_CONST', 'STRING_CONST', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'AND', 'OR', 'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ',
    'ASSIGN', 'INCR', 'DECR', 'NOT', 'DOT', 'COMMA', 'SEMI', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
] + list(reserved.values())

t_INCR = r'\+\+'
t_DECR = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_AND = r'&&'
t_OR = r'\|\|'
t_EQ = r'=='
t_NEQ = r'!='
t_LEQ = r'<='
t_GEQ = r'>='
t_LT = r'<'
t_GT = r'>'
t_ASSIGN = r'='
t_NOT = r'!'
t_DOT = r'\.'
t_COMMA = r','
t_SEMI = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ignore = ' \t\r'

def t_CBlock(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')  

def t_CLine(t):
    r'//[^\n]*'
    pass

def t_DIVIDE(t):
    r'/'
    return t

def t_FLOAT_CONST(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_INT_CONST(t):
    r'[0-9]+'
    return t

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING_CONST(t):
    r'"[^"\n]*"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Lexical error at line {t.lexer.lineno}: illegal character '{t.value[0]}'")
    sys.exit(1)

lexer = lex.lex()
