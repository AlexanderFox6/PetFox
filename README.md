# PetFox
This is the creation of a new programming language that operates in base eight. Our idea is that we have discovered extraterrestrial life that only has eight fingers. To help progress communication with aliens, we needed to create a programming language that does math in the same base as these beings. The name of our language combines the names of the two creators: Alex Fox and Nolan Pettit.

### Tokens:
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
    'RPAREN'

### Keywords:
    'if': 'KEYWORD',
    'else': 'KEYWORD',
    'while': 'KEYWORD',
    'for': 'KEYWORD',
    'pet': 'KEYWORD',
    'fox': 'KEYWORD',
    'glorp': 'KEYWORD',
    'print': 'KEYWORD',
    'return': 'KEYWORD'

    The keyword, pet, is used for creating variables
    The keyword, fox, is used for defining constants
    The keyword, glorp, is used for function definitions

### Special Symbols:
    t_ASSIGN = r'='
    t_MATH_OP = r'[+\-*/]'
    t_COMPARISON_OP = r'(==|!=|<|>|<=|>=)'
    t_LOGICAL_OP = r'(and|or|not)'
    t_SEPARATOR = r':'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

### Rules:
    Keywords:
    def t_KEYWORD(t):
        r'(if|else|while|for|pet|fox|glorp|print|return)\b'
        t.type = keywords.get(t.value, 'IDENTIFIER')
        return t

    Strings:
    def t_STRING(t):
        r"'[^']*'"
        t.value = t.value[1:-1]
        return t

    Comments:
    def t_COMMENT(t):
        r"//.*"
        pass

    New Lines:
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    Error Handling:
    def t_error(t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

### Example Usage:
    data = '''
    glorp my_function(y):
        pet x = 5
        fox unchanging = 144
        pet s = 'hello'
        print(s)
        if x == 5:
            x = x + 1
        else:
            y - 2
            x = 0
        return x
    
    my_function(17)
    '''
    
    lexer.input(data)
    
    # Tokenize the input and print tokens
    for token in lexer:
        print(token)

    The first 10 lines of output from this program are: 
        LexToken(KEYWORD,'glorp',2,1)
        LexToken(IDENTIFIER,'my_function',2,7)
        LexToken(LPAREN,'(',2,18)
        LexToken(IDENTIFIER,'y',2,19)
        LexToken(RPAREN,')',2,20)
        LexToken(SEPARATOR,':',2,21)
        LexToken(KEYWORD,'pet',3,27)
        LexToken(IDENTIFIER,'x',3,31)
        LexToken(ASSIGN,'=',3,33)
        LexToken(NUMBER,'5',3,35)
    


    
