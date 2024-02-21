import ply.lex as lex

# token names
tokens = (
    'NUMBER',
    'IDENTIFIER',
    'KEYWORD',
    'ASSIGN',
    'ARITHMETIC_OP',
    'COMPARISON_OP',
    'LOGICAL_OP',
    'SEPARATOR',
    'STRING'

)

# regular expressions for tokens
t_NUMBER = r'[0-7]+'  # Base 8 numbers
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# keywords
keywords = {
    'if': 'KEYWORD',
    'else': 'KEYWORD',
    'while': 'KEYWORD',
    'for': 'KEYWORD',
    'pet': 'KEYWORD',  # var/let
    'fox': 'KEYWORD'  # const
    # We will need more here but this is what i started with
}

# Define rules for keywords


def t_KEYWORD(t):
    r'(if|else|while|for|pet|fox)\b'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t


# special symbols
t_ASSIGN = r'='
t_ARITHMETIC_OP = r'[+\-*/]'
t_COMPARISON_OP = r'(==|!=|<|>|<=|>=)'
t_LOGICAL_OP = r'(and|or|not)'
t_SEPARATOR = r':'

# strings


def t_STRING(t):
    r"'[^']*'"
    t.value = t.value[1:-1]
    return t


# ignored characters (whitespace and comments)
t_ignore = ' \t'

# rule for newlines


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# error handling rule


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# lexer
lexer = lex.lex()

# testing the lexer here
data = '''
pet x = 7
fox unchanging = 100
pet s = 'hello'
if x == 7:
    x = x + 1
else:
    x = 0
'''

lexer.input(data)


# tokenize the input and print tokens

for token in lexer:
    print(token)
