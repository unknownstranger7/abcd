# Define operator precedence and grammar rules
operators_priority = ["^", "*", "/", "+", "-"]
operators = ["+", "*"]
terminals = ["id", "$"]
non_terminals = ["E", "A"]
total_symbols = ["id", "+", "*", "$"]

grammar = {
    "E": ["id", "EAE"],
    "A": ["+", "*"]
}

# Define the input expression
expression = "id+id*id"

# Function to check precedence between two symbols
def check_precedence(left, right):
    if left in terminals and right in terminals:
        if (left != right and right == "$"):
            return ">"
        elif (left == right):
            return " "
        else:
            return "<"
    elif left in terminals and right in operators:
        if (left == "$"):
            return "<"
        else:
            return ">"
    elif left in operators and right in terminals:
        if (right != "$"):
            return "<"
        else:
            return ">"
    else:
        if (left == right):
            return ">"
        else:
            index_left = operators_priority.index(left)
            index_right = operators_priority.index(right)

            if (index_left >= index_right):
                return "<"
            else:
                return ">"

# Initialize a table to store precedence relations
operators_precedence_table = [['' for _ in range(len(total_symbols))] for _ in range(len(total_symbols))]

# Populate the precedence table using the check_precedence function
for i in range(len(total_symbols)):
    for j in range(len(total_symbols)):
        left_symbol = total_symbols[i]
        right_symbol = total_symbols[j]
        operators_precedence_table[i][j] = check_precedence(left_symbol, right_symbol)

# Print the precedence table
print("Precedence Table:")
print("  " + " ".join(total_symbols))
for i in range(len(total_symbols)):
    print(total_symbols[i] + " " + " ".join(operators_precedence_table[i]))

# Function to check the validity of an expression
def is_valid_expression(expression):
    stack = ["$"]
    expression += "$"
    i = 0

    while i < len(expression):
        if expression[i] in total_symbols:
            precedence = check_precedence(stack[-1], expression[i])

            if precedence == "<" or precedence == "=":
                stack.append(expression[i])
                i += 1
            elif precedence == ">":
                while precedence == ">":
                    if len(stack) < 3:
                        return False
                    else:
                        top = stack[-1]
                        second = stack[-2]
                        third = stack[-3]

                        if third in non_terminals and second in operators and top in non_terminals:
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            stack.append(third)
                        else:
                            return False
                    precedence = check_precedence(stack[-1], expression[i])
        else:
            return False

    return len(stack) == 1 and stack[0] == "$"

# Check if the input expression is valid according to the grammar
if is_valid_expression(expression):
    print("The expression is valid according to the given grammar.")
else:
    print("The expression is not valid according to the given grammar.")
