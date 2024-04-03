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
