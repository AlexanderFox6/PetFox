import ply.lex as lex

# List of token names
tokens = (
    'NUMBER',   # this does not get alien name
    'PLUS',    # this does not get alien name
    'MINUS',    # this does not get alien name
    'TIMES',        # this does not get alien name
    'DIVIDE',   # this does not get alien name  
    'LPAREN',  # this does not get alien name
    'RPAREN',   # this does not get alien name
    'OCTAL_NUMBER', # this does not get alien name
    'KEYWORD',  # this does not get alien name
    'NEWLINE',  # this does not get alien name
    'COMMENT',  # this does not get alien name
    'STRING',   # this does not get alien name
    'GREATER_THAN', # this does not get alien name
    'LESS_THAN',    # this does not get alien name
    'GREATER_THAN_EQUAL',   # this does not get alien name
    'LESS_THAN_EQUAL',  # this does not get alien name
    'EQUAL_TO', # this does not get alien name
    'NOT_EQUAL_TO', # this does not get alien name
    'AND',  
    'OR',
    'NOT',
    'LCURLY',   # this does not get alien name
    'RCURLY',   # this does not get alien name
    'SEMICOLON',    # this does not get alien name
    'COMMA',    # this does not get alien name
    'DOT',  # this does not get alien name
    'COLON',    # this does not get alien name
    'ARROW',    # this does not get alien name
    'HASH', # this does not get alien name
    'AT',   # this does not get alien name
    'DOLLAR',   # this does not get alien name
    'PERCENT',
    'CARET',
    'AMPERSAND',
    'ASTERISK',
    'UNDERSCORE',
    'BACKTICK',
    'TILDE',
    'PIPE',
    'QUESTION',
    'EXCLAMATION',
    'BACKSLASH',
    'FORWARD_SLASH',
    'PLUS_EQUALS',
    'MINUS_EQUALS',
    'TIMES_EQUALS',
    'DIVIDE_EQUALS',
    'MODULO_EQUALS',
    'CARET_EQUALS',
    'AMPERSAND_EQUALS',
    'PIPE_EQUALS',
    'LEFT_SHIFT_EQUALS',
    'RIGHT_SHIFT_EQUALS',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LEFT_SHIFT',
    'RIGHT_SHIFT',
    'INCREMENT',
    'DECREMENT',
    'ELLIPSIS',
    'ARROW_STAR',
    'DOT_STAR', # this does not get alien name
    
    'PLITZ',  # New token for print statements
    'IDENTIFIER',  # New token for identifiers
    'ILF',          # 'if' keyword
    'ELZ',         # 'else' keyword
    'WHILK',       # 'while' keyword
    'FRZ',         # 'for' keyword
    'RETURN',
    'ELIL',     # 'elif' keyword
    'FLORP',
    'statements',
    'ASSIGN',
    'LBRACKET',
    'RBRACKET',
    'MODULO',
    'QUOTE',

)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_EQUALS = r'='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_THAN_EQUAL = r'>='
t_LESS_THAN_EQUAL = r'<='
t_EQUAL_TO = r'=='
t_NOT_EQUAL_TO = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_ARROW = r'->'
t_AT = r'@'
t_DOLLAR = r'\$'
t_PERCENT = r'%'
t_CARET = r'\^'
t_AMPERSAND = r'&'
t_ASTERISK = r'\*'
t_UNDERSCORE = r'_'
t_BACKTICK = r'`'
t_TILDE = r'~'
t_PIPE = r'\|'
t_QUESTION = r'\?'
t_EXCLAMATION = r'!'
t_BACKSLASH = r'\\'
t_FORWARD_SLASH = r'/'
t_PLUS_EQUALS = r'\+='
t_MINUS_EQUALS = r'-='
t_TIMES_EQUALS = r'\*='
t_DIVIDE_EQUALS = r'/='
t_MODULO_EQUALS = r'%='
t_CARET_EQUALS = r'\^='
t_AMPERSAND_EQUALS = r'&='
t_PIPE_EQUALS = r'\|='
t_LEFT_SHIFT_EQUALS = r'<<='
t_RIGHT_SHIFT_EQUALS = r'>>='

t_LEFT_SHIFT = r'<<'
t_RIGHT_SHIFT = r'>>'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_ELLIPSIS = r'\.\.\.'
t_ARROW_STAR = r'->\*'
t_DOT_STAR = r'\.\*'
t_PLITZ = r'[Pp][Ll][Ii][Tt][Zz]'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_MODULO = r'%'
t_ASSIGN = r'='
t_FRZ = r'[Ff][Rr][Zz]'
t_QUOTE = r'\"'


def t_WHILK(t):
    r'whilk'
    return t

def t_ILF(t): # rule for if keyword
    r'ilf'
    return t

def t_ELZ(t): # rule for else keyword
    r'elz'
    return t

def t_ELIL(t):  # rule for elif keyword
    r'elil'
    return t

def t_FLORP(t): # rule for function keyword
    r'florp'
    return t

# Define a rule for octal numbers
def t_OCTAL_NUMBER(t):
    r'0[oO]?[0-7]+'
    t.value = int(t.value, 8)
    return t

# Define a rule for keywords
def t_KEYWORD(t):
    r'ilf|elz|whilk|return|break|continue|switch|case|default|do|goto|typedef|struct|union|enum|sizeof|auto|register|static|extern|const|volatile|inline|restrict|_Bool|_Complex|_Imaginary|void|char|short|int|long|float|double|signed|unsigned|_Alignas|_Alignof|_Atomic|_Generic|_Noreturn|_Static_assert|_Thread_local|bool|true|false|NULL'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Define a rule for comments
def t_COMMENT(t):
    r'//.*'
    pass


# Define a rule for strings
def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1]
    return t

def t_STATEMENTS(t):
    r'statements'
    return t

def t_NUMBER(t):
    # numbers 0-7
    r'[0-7]+'
    t.value = int(t.value)
    return t
    

def t_BOOLEAN(t):
    r'true|false'
    return t

def t_CHAR(t):
    r"'.'"
    t.value = t.value[1:-1]
    return t

# List of keywords
keywords = {
    'ilf', 'elz', 'whilk', 'frz', 'return', 'break', 'continue', 'switch', 'case', 'default', 'do', 'goto',
    'typedef', 'struct', 'union', 'enum', 'sizeof', 'auto', 'register', 'static', 'extern', 'const', 'volatile',
    'inline', 'restrict', '_Bool', '_Complex', '_Imaginary', 'void', 'char', 'short', 'int', 'long', 'float',
    'double', 'signed', 'unsigned', '_Alignas', '_Alignof', '_Atomic', '_Generic', '_Noreturn', '_Static_assert',
    '_Thread_local', 'bool', 'true', 'false', 'NULL'
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'IDENTIFIER' if t.value not in keywords else t.value.upper()
    return t



# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    # Test the lexer
    data = '''
       (5>3) && (3<5)
       
    '''
    lexer.input(data)
    for token in lexer:
        print(token)
