from parser import parser

# Input expression
expression = "3 + 4 * (5 - 2)"

# Parse the expression
result = parser.parse(expression)

# Print the resulting AST
print(result)
