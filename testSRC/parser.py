from ply import yacc
from lexer import tokens

# Define the grammar rules


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])


def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = ('/', p[1], p[3])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_number(p):
    'factor : NUMBER'
    p[0] = ('number', p[1])


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors


def p_error(p):
    if p:
        print(
            f"Syntax error at line {p.lineno} with token {p.type}: {p.value}")
    else:
        print("Syntax error: Unexpected end of input or unknown token")


# Build the parser
parser = yacc.yacc()
