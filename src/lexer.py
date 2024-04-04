import ply.lex as lex
import ply.yacc as yacc

# Token names
tokens = (
    'NUMBER',
    'FLOAT',
    'BOOLEAN',
    'CHAR',
    'IDENTIFIER',
    'KEYWORD',
    'ASSIGN',
    'MATH_OP',
    'EXPONENT',
    'BITWISE_OP',
    'ASSIGN_OP',  
    'COMPARISON_OP',
    'LOGICAL_OP',
    'SEPARATOR',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'NEWLINE',
    'BREAK',
    'CONTINUE',
    'ELIF',
    'ELSE',  # Define ELSE token
    'COMMENT',
    'EOF'
)

# Regular expressions for tokens
t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_BOOLEAN = r'true|false'
t_CHAR = r"'.'"
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Updated keywords
keywords = {
    'if': 'KEYWORD',
    'else': 'KEYWORD',
    'while': 'KEYWORD',
    'for': 'KEYWORD',
    'let': 'KEYWORD',  
    'const': 'KEYWORD',  
    'function': 'KEYWORD',  
    'print': 'KEYWORD',
    'return': 'KEYWORD',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'elif': 'ELIF'
}

# Updated special symbols
t_ASSIGN = r'='
t_MATH_OP = r'[+\-*/%]'
t_EXPONENT = r'\*\*'
t_BITWISE_OP = r'[&|~^]'
t_ASSIGN_OP = r'\+=|-=|\*=|/=|%=|&=|\|=|\^='
t_COMPARISON_OP = r'==|!=|<|>|<=|>='
t_LOGICAL_OP = r'and|or|not'
t_SEPARATOR = r':|,'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'

# Updated strings and comments
def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1]
    return t

def t_COMMENT(t):
    r'//.*|\#.*'
    pass

# Rule for newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Ignored characters (whitespace and comments)
t_ignore = ' \t'

# End of file token
def t_eof(t):
    return None

# Build the lexer
lexer = lex.lex()

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

# Define operator precedence and associativity
precedence = (
    ('left', 'MATH_OP'),
    ('left', 'COMPARISON_OP'),
    ('left', 'LOGICAL_OP'),
)

# Build the parser
parser = yacc.yacc()

# Test the parser
if __name__ == '__main__':
    while True:
        try:
            data = input("Enter an expression: ")
            if data.lower() == 'exit':
                break

            # Tokenize the input string
            lexer.input(data.lower())
            while True:
                tok = lexer.token()
                if not tok:
                    break  # No more input
                print(tok)

            # Parse the input string
            result = parser.parse(data.lower())
            print(result)
        except EOFError:
            break
        except Exception as e:
            print("Error:", e)
            continue  # Continue to next iteration
