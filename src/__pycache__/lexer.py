from ply import lex

# Define tokens
tokens = (
    'NUMBER',
    'BOOLEAN',
    'CHAR',
    'ILF',      # 'if' keyword
    'ELZ',      # 'else' keyword
    'ELIL',     # 'elif' keyword
    'WHILK',    # 'while' keyword
    'FRZ',      # 'for' keyword
    'PET',      # 'let' keyword
    'FOX',      # 'const' keyword
    'FLORP',    # 'function' keyword
    'PLITZ',    # 'print' keyword
    'RYTORN',   # 'return' keyword
    'BRYK',     # 'break' keyword
    'CONZORP',  # 'continue' keyword
    'TLIP',     # 'true' keyword
    'FLOP',     # 'false' keyword
    'NOL',      # 'null' keyword
    'NI',       # 'in' keyword
    'IDENTIFIER',
    'ASSIGN',
    'EQUAL_TO',
    'NOT_EQUAL_TO',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_EQUAL',
    'GREATER_THAN_EQUAL',
    'AND',
    'OR',
    'NOT',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'NEWLINE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'COMMENT',
    'EOF',
)


# Regular expressions for keyword tokens
t_ILF = r'ilf'
t_ELZ = r'elz'
t_ELIL = r'elil'
t_WHILK = r'whilk'
t_FRZ = r'frz'
t_PET = r'pet'
t_FOX = r'fox'
t_FLORP = r'florp'
t_PLITZ = r'plitz'
t_RYTORN = r'rytorn'
t_BRYK = r'bryk'
t_CONZORP = r'conzorp'
t_TLIP = r'tlip'
t_FLOP = r'flop'
t_NOL = r'nol'
t_NI = r'ni'


# Regular expressions for tokens
t_NUMBER = r'[0-7]+'
# t_FLOAT = r'\d+\.\d+'
t_BOOLEAN = r'true|false'
t_CHAR = r"'.'"
# t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-7_]*'
# Regular expression for IDENTIFIER token
t_IDENTIFIER = r'(?!ilf)[a-zA-Z_][a-zA-Z0-9_]*'
# Updated special symbols
t_ASSIGN = r'='
t_EQUAL_TO = r'=='
t_NOT_EQUAL_TO = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUAL = r'<='
t_GREATER_THAN_EQUAL = r'>='
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

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
