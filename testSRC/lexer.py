from ply import lex

# Define tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define a rule for NUMBER token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for ignoring whitespace
t_ignore = ' \t'

# Define a rule for tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule for error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
