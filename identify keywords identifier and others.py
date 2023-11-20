import re   # re for regular expressions

# Define lists of keywords and other symbols
keywords = ["int", "void", "char", "#include", "main()", "stdio.h", "printf", "scanf"]
other_symbols = list("!@#$%^&*_;:=()\[\]{}.,/\\`~<>")

# Initialize counters
identifiers = 0
keywords_count = 0
other_count = 0

# Open the input file for reading
with open("index.txt", 'r') as file:
    content = file.read()

    # Define a regular expression pattern to match quoted strings
    pattern = r'"(?:\\.|[^\\"])*"'
    
    # Find all quoted strings in the content
    quoted_strings = re.findall(pattern, content)

    # Replace quoted strings with a placeholder ("<QUOTED_STRING>") in the content
    content_without_quoted_strings = re.sub(pattern, "<QUOTED_STRING>", content)

    # Split the content into individual words and remove empty strings
    words = [word.strip() for word in content_without_quoted_strings.split() if word.strip()]

    # Replace the "<QUOTED_STRING>" placeholder with the actual quoted strings
    for i, word in enumerate(words):
        if word == "<QUOTED_STRING>":
            words[i] = quoted_strings.pop(0)

    # Iterate through each word in the content
    for word in words:
        if word in keywords:
            print(f"{word} is a keyword")
            keywords_count += 1
        elif word in other_symbols:
            print(f"{word} is a symbol")
            other_count += 1
        elif word.isnumeric():
            print(f"{word} is a number")
        else:
            print(f"{word} is an identifier")
            identifiers += 1

    # Print the counts of keywords, symbols, and identifiers
    print(f"Number of keywords: {keywords_count}, symbols: {other_count}, identifiers: {identifiers}")


