import ply.yacc as yacc
from tokens import lexer

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
              | ELSE
    '''
    p[0] = p[1]

def p_assignment_statement(p):
    'assignment_statement : IDENTIFIER ASSIGN expression NEWLINE'
    p[0] = ('assignment', p[1], p[3])

def p_if_statement(p):
    '''
    if_statement : if_clause NEWLINE statement_list
                 | if_clause NEWLINE statement_list ELIF NEWLINE statement_list
                 | if_clause NEWLINE statement_list ELIF NEWLINE statement_list NEWLINE ELSE NEWLINE statement_list
    '''
    if len(p) == 4:
        p[0] = ('if', p[1], p[3])
    elif len(p) == 7:
        p[0] = ('if', p[1], p[3], ('elif', p[5], p[7]))
    else:
        p[0] = ('if', p[1], p[3], ('elif', p[5], p[7]), ('else', p[9]))

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
    expression : literal
               | LPAREN expression RPAREN
               | expression MATH_OP expression
               | expression COMPARISON_OP expression
               | expression LOGICAL_OP expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = ('binop', p[2], p[1], p[3])

def p_literal(p):
    '''
    literal : NUMBER
            | FLOAT
            | BOOLEAN
            | CHAR
            | IDENTIFIER
            | STRING
    '''
    p[0] = ('literal', p[1])

# Add a rule to handle unknown tokens
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno} with token {p.type}: {p.value}")
    else:
        print("Syntax error: Unexpected end of input or unknown token")


# Build the parser
parser = yacc.yacc()

# Test the parser
if __name__ == '__main__':
    while True:
        try:
            data = input("Enter an expression: ")
            if data.lower() == 'exit':
                break
            
            result = parser.parse(data, lexer=lexer)
            print(result)
        except EOFError:
            break

