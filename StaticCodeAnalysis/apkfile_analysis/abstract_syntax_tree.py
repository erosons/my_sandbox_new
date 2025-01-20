import ast
import inspect

def example_function(a, b):
    result = a + b
    
    return result

# Get the source code of the function
source_code = inspect.getsource(example_function)

# Parse the source code into an abstract syntax tree (AST)
parsed_ast = ast.parse(source_code)

# Display the AST
print(ast.dump(parsed_ast))
