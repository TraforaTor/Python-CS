import itertools

def evaluate_expression(expr, values):
    # Replace variable names with their truth values
    for var, val in values.items():
        expr = expr.replace(var, str(val))
    
    # Replace logical operators with Python's logical operators
    expr = expr.replace('+', ' and ')
    expr = expr.replace('*', ' or ')
    expr = expr.replace('!', ' not ')
    
    try:
        # Evaluate the expression
        return eval(expr)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

def truth_table(expr):
    # Identify unique variables in the expression
    variables = sorted(set(filter(str.isalpha, expr)))
    
    # Generate all combinations of truth values for the variables
    combinations = list(itertools.product([False, True], repeat=len(variables)))
    
    # Print the header of the truth table
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))
    
    # Evaluate the expression for each combination and print the results
    for combo in combinations:
        values = dict(zip(variables, combo))
        result = evaluate_expression(expr, values)
        row = " | ".join(str(int(values[var])) for var in variables) + " | " + str(int(result))
        print(row)

# Example usage
if __name__ == "__main__":
    expression = "(!x+y)*z+(!z*y*k)"  # Change the expression here
    truth_table(expression)
