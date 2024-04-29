from lexer import lexer
from parser import parser

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        # Split the code into lines
        lines = code.split('\n')
        result = None
        # Interpret each line individually
        for line in lines:
            # Tokenize the code
            lexer.input(line)
            # Parse the code and generate AST
            ast = parser.parse(input=line)
            # Execute the AST and store the result
            if ast:
                result = self.execute(ast)
        return result

        
    def execute(self, node):
        if isinstance(node, tuple):
            if node[0] == 'number':
                # If the number is in base 10, convert it to base 8
                return self.to_octal(node[1])
            elif node[0] in ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'GREATER_THAN', 'GREATER_THAN_EQUAL',
                            'LESS_THAN', 'LESS_THAN_EQUAL', 'EQUAL_TO', 'NOT_EQUAL_TO']:
                # Perform arithmetic operations in base 10 and then convert the result to base 8
                left_value = self.execute(node[1])
                right_value = self.execute(node[2])
                result = self.perform_operation(node[0], left_value, right_value)
                return self.to_octal(result)
            elif node[0] == 'IDENTIFIER':
                return self.variables.get(node[1], None)
            elif node[0] == 'plitz':
                if isinstance(node[1], tuple) and node[1][0] == 'STRING':
                    return node[1][1]  # Return the string value directly
                else:
                    return self.execute(node[1])
            elif node[0] == 'return':
                return self.execute(node[1])
            elif node[0] == 'florp':
                self.variables[node[1]] = (node[2], node[3])  # (parameter_list, function_body)
                return "florp created successfully."
            elif node[0] == 'florp_call':
                function_name = node[1]
                arguments = node[2]
                parameter_list, function_body = self.variables.get(function_name, (None, None))
                if parameter_list and function_body:
                    for param, arg in zip(parameter_list, arguments):
                        self.variables[param] = self.execute(arg)
                    return self.execute(function_body)
                else:
                    print("Error: Florp '{}' is not defined.".format(function_name))
            elif node[0] == 'PLUS':
                return self.execute(node[1]) + self.execute(node[2])
            elif node[0] == 'MINUS':
                return self.execute(node[1]) - self.execute(node[2])
            elif node[0] == 'TIMES':
                return self.execute(node[1]) * self.execute(node[2])
            elif node[0] == 'DIVIDE':
                return self.execute(node[1]) / self.execute(node[2])
            elif node[0] == 'GREATER_THAN':
                return self.execute(node[1]) > self.execute(node[2])
            elif node[0] == 'GREATER_THAN_EQUAL':
                return self.execute(node[1]) >= self.execute(node[2])
            elif node[0] == 'LESS_THAN':
                return self.execute(node[1]) < self.execute(node[2])
            elif node[0] == 'LESS_THAN_EQUAL':
                return self.execute(node[1]) <= self.execute(node[2])
            elif node[0] == 'EQUAL_TO':
                return self.execute(node[1]) == self.execute(node[2])
            elif node[0] == 'NOT_EQUAL_TO':
                return self.execute(node[1]) != self.execute(node[2])
            elif node[0] == 'frz':
                self.variables[node[1]] = self.execute(node[2])
                condition = node[3]
                block = node[4]
                result = None
                while self.execute(condition):
                    result = self.execute(block)
                return result
            elif node[0] == 'whilk':
                condition = node[1]
                block = node[2]
                result = None
                while self.execute(condition):
                    result = self.execute(block)
                return result
            elif node[0] == 'ASSIGN':
                self.variables[node[1]] = self.execute(node[2])
                return self.variables[node[1]]
            elif node[0] == 'increment':
                self.variables[node[1]] += 1
                return self.variables[node[1]]
            elif node[0] == 'decrement':
                self.variables[node[1]] -= 1
                return self.variables[node[1]]
            elif node[0] == 'ilf':
                if self.execute(node[1]):
                    return self.execute(node[2])
            elif node[0] == 'ilf-elz':
                if self.execute(node[1]):
                    return self.execute(node[2])
                else:
                    return self.execute(node[3])
            elif node[0] == 'ilf-elil-elz':
                for condition, block in node[1]:
                    if self.execute(condition):
                        return self.execute(block)
                return self.execute(node[2])
            elif node[0] == '&&':
                return self.execute(node[1]) and self.execute(node[2])
            elif node[0] == '||':
                return self.execute(node[1]) or self.execute(node[2])

        elif isinstance(node, str):
            return self.variables.get(node, None)
        return node


    
    def to_octal(self, number):
        # Return the number as is without converting to octal
        var = oct(number)[2:]
        x = int(var)
        return x

    def perform_operation(self, operator, left, right):
        # Perform arithmetic and comparison operations in base 10
        if operator == 'PLUS':
            return left + right
        elif operator == 'MINUS':
            return left - right
        elif operator == 'TIMES':
            return left * right
        elif operator == 'DIVIDE':
            return left / right
        elif operator == 'GREATER_THAN':
            return left > right
        elif operator == 'GREATER_THAN_EQUAL':
            return left >= right
        elif operator == 'LESS_THAN':
            return left < right
        elif operator == 'LESS_THAN_EQUAL':
            return left <= right
        elif operator == 'EQUAL_TO':
            return left == right
        elif operator == 'NOT_EQUAL_TO':
            return left != right



# Instantiate the interpreter
interpreter = Interpreter()

# Main loop to accept code input and interpret it
code_lines = []
multiline_input = False  # Flag to track multiline input
multiline_code = []     # List to store multiline code
print("Enter your code line by line. Enter 'exit' on a new line to finish.")
while True:
    try:
        line = input(">>> ")
        if line.lower() == 'exit':
            break
        if line.endswith("{") or multiline_input:
            multiline_input = True
            multiline_code.append(line)
            if line.endswith("}"):
                code_lines.append(" ".join(multiline_code))  # Join multiline code
                multiline_code = []  # Reset multiline code
                multiline_input = False  # Reset multiline input flag
        else:
            code_lines.append(line)
    except Exception as e:
        print("Error:", e)
        continue

# Concatenate the code lines into a single string
code = '\n'.join(code_lines)

# Interpret the code
result = interpreter.interpret(code)
print("Result:", result)
