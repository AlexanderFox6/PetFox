from ply import lex

# Define tokens
tokens = (
    'NUMBER',
    'FLOAT',
    'BOOLEAN',
    'CHAR',
    'IDENTIFIER',
    'KEYWORD',
    'ASSIGN',
    'BITWISE_OP',
    'ASSIGN_OP',
    'COMPARISON_OP',
    'LOGICAL_OP',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'NEWLINE',
    'BREAK',
    'CONTINUE',
    'ELIF',
    'ELSE',
    'END',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Regular expressions for tokens
t_NUMBER = r'[0-7]+'
t_FLOAT = r'\d+\.\d+'
t_BOOLEAN = r'true|false'
t_CHAR = r"'.'"
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-7_]*'


# Updated keywords
keywords = {
    'ilf': 'ILF',        # if
    'elz': 'ELZ',        # else
    'elil': 'ELIL',      # elif
    'whilk': 'WHILK',    # while
    'frz': 'FRZ',        # for
    'pet': 'PET',        # let
    'fox': 'FOX',        # const
    'florp': 'FLORP',    # function
    'plitz': 'PLITZ',    # print
    'rytorn': 'RYTORN',  # return
    'bryk': 'BRYK',      # break
    'conzorp': 'CONZORP',  # continue
    'tlip': 'TLIP',      # true
    'flop': 'FLOP',      # false
    'nol': 'NOL',        # null
    'ni': 'NI',          # in
}


# Updated special symbols
t_ASSIGN = r'='
t_BITWISE_OP = r'[&|~^]'
t_ASSIGN_OP = r'\+=|-=|\*=|/=|%=|&=|\|=|\^='
t_COMPARISON_OP = r'==|!=|<|>|<=|>='
t_LOGICAL_OP = r'and|or|not'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_END = r';'

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


lexer = lex.lex()
