import ply.lex as lex

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
    'ASSIGN_OP',  # +=, -=, etc
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
    'COMMENT',
    'EOF'
)

# Regular expressions for tokens
t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'  # Float regex
t_BOOLEAN = r'true|false'
t_CHAR = r"'.'"
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Updated keywords and rules
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
    'break': 'BREAK',  # Updated to include break
    'continue': 'CONTINUE',  # Updated to include continue
    'elif': 'ELIF'  # Updated to include elif
}

# Updated special symbols
t_ASSIGN = r'='
t_MATH_OP = r'[+\-*/%]'
t_EXPONENT = r'\*\*'
t_BITWISE_OP = r'[&|~^]'
t_ASSIGN_OP = r'\+=|-=|\*=|/=|%=|&=|\|=|\^='
t_COMPARISON_OP = r'(==|!=|<|>|<=|>=)'
t_LOGICAL_OP = r'(and|or|not)'
t_SEPARATOR = r':|,'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'

# Updated strings and comments
def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'  # Updated to handle double quoted strings
    t.value = t.value[1:-1]
    return t

def t_COMMENT(t):
    r'//.*|\#.*'  # Updated to handle single-line comments with # symbol
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

# Lexer
lexer = lex.lex()

# Testing the lexer
data = '''
function add(a, b):
    let result = a + b
    return result

print(add(3, 5))  # Output: 8
'''

lexer.input(data)

# Tokenize the input and print tokens
for token in lexer:
    print(token)
