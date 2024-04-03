import ply.yacc as yacc
from tokens import tokens

# Grammar rules
def p_statement(p):
    '''
    statement : assignment_statement
              | if_statement
              | while_statement
              | expression_statement
              | BREAK
              | CONTINUE
              | ELIF
    '''
    p[0] = p[1]

def p_assignment_statement(p):
    'assignment_statement : IDENTIFIER ASSIGN expression NEWLINE'
    p[0] = ('assignment', p[1], p[3])

# def p_if_statement(p):
#     '''
#     if_statement : if_clause NEWLINE statement NEWLINE
#                  | if_clause NEWLINE statement ELIF statement
#     '''
#     if len(p) == 5:
#         p[0] = ('if', p[1], p[3])
#     else:
#         p[0] = ('if', p[1], p[3], p[5])
def p_if_statement(p):
    '''
    if_statement : if_clause NEWLINE statement
                 | if_clause NEWLINE statement NEWLINE ELIF NEWLINE statement
                 | if_clause NEWLINE statement NEWLINE ELIF NEWLINE statement NEWLINE ELSE NEWLINE statement
    '''
    p[0] = ('if', p[1], *p[3:])


# def p_if_clause(p):
#     'if_clause : KEYWORD expression'
#     p[0] = ('if_clause', p[1], p[2])
def p_if_clause(p):
    '''
    if_clause : KEYWORD expression
              | KEYWORD expression LCURLY NEWLINE statement_list RCURLY
    '''
    if len(p) == 3:
        p[0] = ('if_clause', p[1], p[2])
    else:
        p[0] = ('if_clause', p[1], p[2], p[5])
        
def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]



def p_while_statement(p):
    'while_statement : while_clause NEWLINE statement NEWLINE'
    p[0] = ('while', p[1], p[3])

def p_while_clause(p):
    'while_clause : KEYWORD expression'
    p[0] = ('while_clause', p[1], p[2])

def p_expression_statement(p):
    'expression_statement : expression NEWLINE'
    p[0] = ('expression', p[1])

def p_expression(p):
    '''
    expression : NUMBER
               | FLOAT
               | BOOLEAN
               | CHAR
               | IDENTIFIER
               | STRING
               | math_expression
               | comparison_expression
               | logical_expression
    '''
    p[0] = ('expression', p[1])

def p_math_expression(p):
    'math_expression : expression MATH_OP expression'
    p[0] = ('math_expression', p[1], p[2], p[3])

def p_comparison_expression(p):
    'comparison_expression : expression COMPARISON_OP expression'
    p[0] = ('comparison_expression', p[1], p[2], p[3])

def p_logical_expression(p):
    'logical_expression : expression LOGICAL_OP expression'
    p[0] = ('logical_expression', p[1], p[2], p[3])

# Rule for error handling
def p_error(p):
    print(f"Syntax error at line {p.lineno} with token {p.type}")

    


# Build the parser
parser = yacc.yacc()

# Test the parser
data = """
if x == 5:
    print("x is 5")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")
"""


result = parser.parse(data)
print(result)

