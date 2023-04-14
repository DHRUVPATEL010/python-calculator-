
def evaluate_statement(statement):
    try:
        result = eval(statement)
        print("Result:", result)
    except (SyntaxError, TypeError):
        print("Invalid statement. Please try again.")

statement = input("Enter a statement to evaluate: ")
evaluate_statement(statement)