from ply import yacc
# Get the token map from the lexer. This is required.
from lexer import tokens



# Define the grammar
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('PLUS', p[1], p[3])
    
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('MINUS', p[1], p[3])
    
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
    
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('TIMES', p[1], p[3])
    
def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = ('DIVIDE', p[1], p[3])
    
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = ('number', p[1])
    
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
    
def p_factor_identifier(p):
    'factor : IDENTIFIER'
    p[0] = ('IDENTIFIER', p[1])
    
def p_expression_greater_than(p):
    'expression : expression GREATER_THAN term'
    p[0] = ('GREATER_THAN', p[1], p[3])
    
def p_expression_greater_than_equal(p):
    'expression : expression GREATER_THAN_EQUAL term'
    p[0] = ('GREATER_THAN_EQUAL', p[1], p[3])

    
def p_expression_less_than(p):
    'expression : expression LESS_THAN term'
    p[0] = ('LESS_THAN', p[1], p[3])
    
def p_expression_for_loop(p):
    '''
    expression : FRZ LPAREN IDENTIFIER ASSIGN expression SEMICOLON expression SEMICOLON expression RPAREN LCURLY multiline_code RCURLY
               | FRZ LPAREN IDENTIFIER ASSIGN expression SEMICOLON expression SEMICOLON expression RPAREN LCURLY RCURLY
    '''
    if len(p) == 15:
        p[0] = ('frz', p[3], p[5], p[7], p[9], p[12])
    elif len(p) == 14:
        p[0] = ('frz', p[3], p[5], p[7], p[9], p[12], p[13])
    elif len(p) == 13:
        p[0] = ('frz', p[3], p[5], p[7], p[9], p[12], p[13], p[14])
    elif len(p) == 12:
        p[0] = ('frz', p[3], p[5], p[7], p[9], p[12], p[13], p[14])





def p_expression_while_loop(p):
    '''
    expression : WHILK LPAREN expression RPAREN LCURLY multiline_code RCURLY
               | WHILK LPAREN expression RPAREN LCURLY multiline_code RCURLY NEWLINE
    '''
    if len(p) == 8:
        p[0] = ('whilk', p[3], p[6])
    elif len(p) == 9:
        p[0] = ('whilk', p[3], p[6], p[7])




# New rules for multiline code within curly braces
def p_multiline_code(p):
    '''
    multiline_code : expression
                   | expression NEWLINE multiline_code
                   | empty
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[3] is None:
            p[0] = (p[1],)
        else:
            p[0] = (p[1],) + p[3]
    else:
        p[0] = None



    
def p_expression_less_than_equal(p):
    'expression : expression LESS_THAN_EQUAL term'
    p[0] = ('LESS_THAN_EQUAL', p[1], p[3])
    
def p_expression_equal_to(p):
    'expression : expression EQUAL_TO term'
    p[0] = ('EQUAL_TO', p[1], p[3])
    
def p_expression_not_equal_to(p):
    'expression : expression NOT_EQUAL_TO term'
    p[0] = ('NOT_EQUAL_TO', p[1], p[3])
    
def p_expression_ilf_elz(p):
    '''
    expression : ILF LPAREN expression RPAREN LCURLY expression RCURLY ELZ LCURLY expression RCURLY
    '''
    p[0] = ('ilf-elz', p[3], p[6], p[10])
    
# allow for and/or logic to work for ilf statements
def p_expression_ilf(p):
    '''
    expression : ILF LPAREN expression RPAREN LCURLY expression RCURLY
               | ILF LPAREN expression AND expression RPAREN LCURLY expression RCURLY
               | ILF LPAREN expression OR expression RPAREN LCURLY expression RCURLY
    '''
    if len(p) == 8:
        p[0] = ('ilf', p[3], p[6])
    elif len(p) == 10:
        p[0] = ('ilf', ('and' if p[4] == '&&' else 'or'), p[3], p[5], p[8])


    
def p_expression_ilf_elil_elz(p):
    '''
    expression : ILF LPAREN expression RPAREN LCURLY expression RCURLY ELIL LPAREN expression RPAREN LCURLY expression RCURLY ELZ LCURLY expression RCURLY
    '''
    p[0] = ('ilf-elil-elz', [(p[3], p[6]), (p[10], p[13])], p[17])
    
# Add productions for logical operations
def p_expression_or(p):
    'expression : expression OR expression'
    p[0] = ('||', p[1], p[3])

def p_expression_and(p):
    'expression : expression AND expression'
    p[0] = ('&&', p[1], p[3])


def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('!', p[2])



def p_elil_list(p):
    '''
    elil_list : ELIL LPAREN expression RPAREN LCURLY expression RCURLY elil_list
              | empty
    '''
    if len(p) > 2:
        p[0] = [('elil', p[3], p[6])] + p[8]
    else:
        p[0] = []

def p_elz_block(p):
    '''
    elz_block : ELZ LCURLY expression RCURLY
               | empty
    '''
    if len(p) > 2:
        p[0] = p[3]
    else:
        p[0] = None


def p_expression_function_call(p):
    'expression : IDENTIFIER LPAREN function_call_args RPAREN'
    p[0] = ('florp_call', p[1], p[3])

def p_function_call_args(p):
    '''
    function_call_args : expression COMMA function_call_args
                       | expression
    '''
    if len(p) > 2:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]





    

        
def p_function(p):
    '''
    expression : FLORP IDENTIFIER LPAREN parameter_list RPAREN LCURLY statement RCURLY
               | FLORP IDENTIFIER LPAREN parameter_list RPAREN LCURLY expression RCURLY
    '''
    p[0] = ('florp', p[2], p[4], p[7])


def p_parameter_list(p):
    '''
    parameter_list : IDENTIFIER COMMA parameter_list
                   | IDENTIFIER
                   | empty
    '''
    if len(p) > 2:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []


   
def p_expression_print(p):
        'expression : IDENTIFIER LPAREN expression RPAREN multiline_code'
        if p[1] == 'plitz':
            p[0] = ('plitz', p[3])
        else:
            print("Syntax error in input!")
            
def p_expression_print_string(p):
    'expression : IDENTIFIER LPAREN STRING RPAREN multiline_code'
    if p[1] == 'plitz':
        p[0] = ('plitz', p[3])  # Return the string value directly
    else:
        print("Syntax error in input!")

def p_expression_string(p):
    'expression : STRING'
    p[0] = ('STRING', p[1])
    
def p_expression_print_string(p):
    'expression : PLITZ LPAREN STRING RPAREN'
    p[0] = ('plitz', p[3])  # Return the string value directly



    
def p_expression_return(p):
    'expression : RETURN expression'
    p[0] = ('return', p[2])
    
def p_expression_increment(p):
    'expression : IDENTIFIER INCREMENT'
    p[0] = ('increment', p[1])
    
def p_expression_decrement(p):
    'expression : IDENTIFIER DECREMENT'
    p[0] = ('decrement', p[1])
    
def p_expression_assignment(p):
    'expression : IDENTIFIER ASSIGN expression multiline_code'
    p[0] = ('ASSIGN', p[1], p[3])
    

def octal_number(p):
    'expression : OCTAL_NUMBER'
    p[0] = ('number', p[1])
    
    
    
def p_start(p):
    '''start : expression'''
    p[0] = p[1]
    
def p_statement_expression(p):
    '''
    statement : expression
              | ASSIGN
              | empty
    '''
    p[0] = p[1]
    
# add rule to allow for multiple lines of code separated by newlines
def p_expression_newline(p):
    '''
    expression : NEWLINE expression
    '''
    p[0] = p[2]
    
def p_expression_newline_empty(p):
    '''
    expression : NEWLINE
    '''
    p[0] = None
    
def p_expression_empty(p):
    '''
    expression : empty
    '''
    p[0] = None
    
def p_empty(p):
    'empty :'
    pass
    


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    
    
# Build the parser
parser = yacc.yacc()

# example code to test and/or/not
data = '''
ilf (5>3 && 3<5) { plitz("hello") }
'''
result = parser.parse(data)

print(result)
# Output: ('print', ('number', 5))

