from parser import parser
from lexer import lexer

while True:
    try:
        expression = input("Enter an expression: ")
        if expression.lower() == 'exit':
            break

        # Tokenize the input string
        lexer.input(expression)
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            print(tok)

        # Parse the input string
        result = parser.parse(expression)
        print(result)
    except EOFError:
        break
    except Exception as e:
        print("Error:", e)
        continue  # Continue to next iteration
