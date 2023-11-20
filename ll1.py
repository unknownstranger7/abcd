# Define a function named 'find_first' that takes a 'grammar' dictionary as input
def find_first(grammar):
    # Initialize an empty dictionary to store FIRST sets for symbols
    first = {}

    # Define a nested function 'calculate_first' for recursive FIRST set calculation
    def calculate_first(symbol):
        # If the FIRST set for the symbol is already calculated, return it
        if symbol in first:
            return first[symbol]

        # If the symbol is a lowercase letter or a terminal symbol, return it as a set
        if symbol.islower() or not grammar.get(symbol):
            return {symbol}

        # Initialize an empty set for the FIRST set of the symbol
        first_set = set()

        # Iterate through each production for the symbol
        for production in grammar[symbol]:
            for symbol in production:
                # Calculate the FIRST set for the current symbol in the production
                first_of_production = calculate_first(symbol)
                # Update the FIRST set for the symbol with the FIRST set of the current symbol
                first_set.update(first_of_production)

                # If epsilon is not in the FIRST set, exit the loop
                if '' not in first_set:
                    break

            # If all symbols in the production can produce epsilon, add epsilon to the FIRST set
            if all('' in calculate_first(symbol) for symbol in production):
                first_set.add('')

        return first_set  # Return the calculated FIRST set

    # Calculate FIRST sets for all non-terminals in the grammar
    for non_terminal in grammar.keys():
        first[non_terminal] = calculate_first(non_terminal)

    return first  # Return the dictionary of FIRST sets

# Define a function named 'find_follow' that takes 'grammar' and 'start_symbol' as inputs
def find_follow(grammar, start_symbol):
    # Initialize an empty dictionary to store FOLLOW sets for symbols
    follow = {non_terminal: set() for non_terminal in grammar.keys()}
    # Add '$' to the FOLLOW set of the start symbol
    follow[start_symbol].add('$')

    # Calculate FIRST sets for the grammar
    first_sets = find_first(grammar)

    # Define a nested function 'calculate_follow' for recursive FOLLOW set calculation
    def calculate_follow(symbol):
        # Iterate through the non-terminals in the grammar
        for non_terminal, productions in grammar.items():
            for production in productions:
                if symbol in production:
                    symbol_index = production.index(symbol)

                    # Traverse the symbols to the right of the current symbol in the production
                    while symbol_index < len(production) - 1:
                        symbol_index += 1
                        next_symbol = production[symbol_index]

                        # Calculate the FIRST set for the next symbol
                        follow_of_next_symbol = first_sets[next_symbol]
                        # Update the FOLLOW set for the current symbol with the FIRST set of the next symbol
                        follow[symbol].update(follow_of_next_symbol)

                        # If epsilon is not in the FIRST set of the next symbol, exit the loop
                        if '' not in follow_of_next_symbol:
                            break
                    else:
                        # If there is no break (epsilon in all FIRST sets), update FOLLOW with FOLLOW of non-terminal
                        if non_terminal != symbol and '' in first_sets[symbol]:
                            follow[symbol].update(follow[non_terminal])

                    # Remove epsilon from the FOLLOW set
                    follow[symbol].discard('')

    # Calculate FOLLOW sets for all non-terminals in the grammar
    for non_terminal in grammar.keys():
        calculate_follow(non_terminal)

    return follow  # Return the dictionary of FOLLOW sets

if __name__ == "__main__":
    # Define your grammar as a dictionary
    grammar = {
        'S': ['aBDH'],
        'B' : ['cC'],
        'C' : ['bC', ''],
        'D' : ['EF'],
        'E' : ['g', ''],
        'F' : ['f', ''],
        'H' : ['i']
    }

    start_symbol = 'S'  # Define the start symbol of the grammar

    first_sets = find_first(grammar)  # Calculate FIRST sets for the grammar
    follow_sets = find_follow(grammar, start_symbol)  # Calculate FOLLOW sets for the grammar

    # Print FIRST Sets
    print("First Sets:")
    for non_terminal, first_set in first_sets.items():
        print(f"First({non_terminal}) = {first_set}")

    # Print FOLLOW Sets
    print("\nFollow Sets:")
    for non_terminal, follow_set in follow_sets.items():
        print(f"Follow({non_terminal}) = {follow_set}")
