import ply.lex as lex

# Token names
tokens = (
    'NUMBER',
    'IDENTIFIER',
    'KEYWORD',
    'ASSIGN',
    'MATH_OP',
    'COMPARISON_OP',
    'LOGICAL_OP',
    'SEPARATOR',
    'STRING',
    'LPAREN',
    'RPAREN',
    'DOUBLEQUOTE'
)

# Regular expressions for tokens
t_NUMBER = r'[0-7]+'  # Base 8 numbers
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Keywords
keywords = {
    'if': 'KEYWORD',
    'else': 'KEYWORD',
    'while': 'KEYWORD',
    'for': 'KEYWORD',
    'pet': 'KEYWORD',  # var/let
    'fox': 'KEYWORD',  # const
    'glorp': 'KEYWORD'
}

# rules for keywords
def t_KEYWORD(t):
    r'(if|else|while|for|pet|fox|glorp)\b'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

# Special symbols
t_ASSIGN = r'='
t_MATH_OP = r'[+\-*/]'
t_COMPARISON_OP = r'(==|!=|<|>|<=|>=)'
t_LOGICAL_OP = r'(and|or|not)'
t_SEPARATOR = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Strings
def t_STRING(t):
    r"'[^']*'"
    t.value = t.value[1:-1]
    return t

# comments
def t_COMMENT(t):
    r"//.*"
    pass

# ignored characters (whitespace and comments)
t_ignore = ' \t'

# Rule for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Lexer
lexer = lex.lex()

# Testing the lexer
data = '''
pet x = 7
fox unchanging = 100
pet s = 'hello'
if x == 7:
    x = x + 1
else:
    x = 0
glorp my_function:
    print('This is a function')
'''

lexer.input(data)

# Tokenize the input and print tokens
for token in lexer:
    print(token)
