from ply import yacc
from lexer import tokens

# Define the precedence of operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Define the grammar rules


def p_start(p):
    '''start : statements'''
    p[0] = p[1]


def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_statement(p):
    '''statement : expression
                 | conditional'''
    p[0] = p[1]


def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression GREATER_THAN term
                  | expression LESS_THAN term
                  | expression EQUAL_TO term
                  | expression NOT_EQUAL_TO term
                  | term'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = ('number', p[1])
    else:
        p[0] = p[2]


def p_conditional(p):
    '''conditional : ILF LPAREN expression RPAREN LCURLY statements RCURLY
                   | ILF LPAREN expression RPAREN LCURLY statements RCURLY ELZ LCURLY statements RCURLY
                   | ILF LPAREN expression RPAREN LCURLY statements RCURLY ELIL LPAREN expression RPAREN LCURLY statements RCURLY ELZ LCURLY statements RCURLY'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    elif len(p) == 12:
        p[0] = ('if_else', p[3], p[6], p[10])
    elif len(p) == 18:
        p[0] = ('if_elif_else', p[3], p[6], p[10], p[14], p[17])

# Error rule for syntax errors


def p_error(p):
    if p:
        print(
            f"Syntax error at line {p.lineno} with token {p.type}: {p.value}")
    else:
        print("Syntax error: Unexpected end of input or unknown token")


# Build the parser
parser = yacc.yacc()
