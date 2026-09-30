#XinyuHe ID:116048576
import sys
from decaf_lexer import tokens, lexer
import ply.yacc as yacc

start = 'program'


precedence = (
    ('nonassoc', 'IFX'),          
    ('nonassoc', 'ELSE'),
    ('right', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('nonassoc', 'LT', 'GT', 'LEQ', 'GEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT', 'UPLUS', 'UMINUS'),
)



def p_program(p):
    '''program : class_decl_list'''
    pass

def p_class_decl_list(p):
    '''class_decl_list : class_decl_list class_decl
                       | empty'''
    pass

def p_class_decl(p):
    '''class_decl : CLASS ID LBRACE class_body_decl_list RBRACE
                  | CLASS ID EXTENDS ID LBRACE class_body_decl_list RBRACE'''
    pass

def p_class_body_decl_list(p):
    '''class_body_decl_list : class_body_decl_list class_body_decl
                            | class_body_decl'''
    pass

def p_class_body_decl(p):
    '''class_body_decl : field_decl
                       | method_decl
                       | constructor_decl'''
    pass


def p_modifier(p):
    '''modifier : empty
                | PUBLIC
                | PRIVATE
                | STATIC
                | PUBLIC STATIC
                | PRIVATE STATIC'''
    pass

def p_field_decl(p):
    '''field_decl : modifier var_decl'''
    pass

def p_var_decl(p):
    '''var_decl : type variables SEMI'''
    pass

def p_type(p):
    '''type : INT
            | FLOAT
            | BOOLEAN
            | ID'''
    pass

def p_variables(p):
    '''variables : variables COMMA variable
                 | variable'''
    pass

def p_variable(p):
    '''variable : ID'''
    pass

def p_method_decl(p):
    '''method_decl : modifier type ID LPAREN formals_opt RPAREN block
                   | modifier VOID ID LPAREN formals_opt RPAREN block'''
    pass

def p_constructor_decl(p):
    '''constructor_decl : modifier ID LPAREN formals_opt RPAREN block'''
    pass

def p_formals_opt(p):
    '''formals_opt : formals
                   | empty'''
    pass

def p_formals(p):
    '''formals : formals COMMA formal_param
               | formal_param'''
    pass

def p_formal_param(p):
    '''formal_param : type variable'''
    pass


def p_block(p):
    '''block : LBRACE stmt_list RBRACE'''
    pass

def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | empty'''
    pass

def p_stmt_if(p):
    '''stmt : IF LPAREN expr RPAREN stmt %prec IFX
            | IF LPAREN expr RPAREN stmt ELSE stmt'''
    pass

def p_stmt_while(p):
    '''stmt : WHILE LPAREN expr RPAREN stmt'''
    pass

def p_stmt_for(p):
    '''stmt : FOR LPAREN stmt_expr_opt SEMI expr_opt SEMI stmt_expr_opt RPAREN stmt'''
    pass

def p_stmt_return(p):
    '''stmt : RETURN expr_opt SEMI'''
    pass

def p_stmt_simple(p):
    '''stmt : stmt_expr SEMI
            | BREAK SEMI
            | CONTINUE SEMI
            | block
            | var_decl
            | SEMI'''
    pass

def p_expr_opt(p):
    '''expr_opt : expr
                | empty'''
    pass

def p_stmt_expr_opt(p):
    '''stmt_expr_opt : stmt_expr
                     | empty'''
    pass

def p_literal(p):
    '''literal : INT_CONST
               | FLOAT_CONST
               | STRING_CONST
               | NULL
               | TRUE
               | FALSE'''
    pass

def p_primary(p):
    '''primary : literal
               | THIS
               | SUPER
               | LPAREN expr RPAREN
               | NEW ID LPAREN arguments_opt RPAREN
               | lhs
               | method_invocation'''
    pass

def p_arguments_opt(p):
    '''arguments_opt : arguments
                     | empty'''
    pass

def p_arguments(p):
    '''arguments : arguments COMMA expr
                 | expr'''
    pass

def p_lhs(p):
    '''lhs : field_access'''
    pass

def p_field_access(p):
    '''field_access : primary DOT ID
                    | ID'''
    pass

def p_method_invocation(p):
    '''method_invocation : field_access LPAREN arguments_opt RPAREN'''
    pass

def p_assign(p):
    '''assign : lhs ASSIGN expr
              | lhs INCR
              | INCR lhs
              | lhs DECR
              | DECR lhs'''
    pass

def p_stmt_expr(p):
    '''stmt_expr : assign
                 | method_invocation'''
    pass

def p_expr_basic(p):
    '''expr : primary
            | assign'''
    pass

def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr AND expr
            | expr OR expr
            | expr EQ expr
            | expr NEQ expr
            | expr LT expr
            | expr GT expr
            | expr LEQ expr
            | expr GEQ expr'''
    pass

def p_expr_unary(p):
    '''expr : NOT expr
            | PLUS expr %prec UPLUS
            | MINUS expr %prec UMINUS'''
    pass


def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}: unexpected token '{p.value}'")
    else:
        print(f"Syntax error at line {lexer.lineno}: unexpected end of file")
    sys.exit(1)


parser = yacc.yacc()