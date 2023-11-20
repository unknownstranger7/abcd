# Initialize global variables
global l
global li
global i  # Added to track the current index in the input

li = 'i+i$'
l = li[0]
i = 0  # Initialize i to 0 to keep track of the current index

def next_token():
    global i
    i += 1
    return li[i]

def match(t):
    global l
    if l == t:
        l = next_token()
    else:
        print('Error')

def e():
    global l
    if l == 'i':
        match('i')
        edash()

def edash():
    global l
    if l == '+':
        match('+')
        match('i')
        edash()
    # You can leave it as it is if the recursion doesn't return anything

def main():
    global l
    e()
    if l == '$':
        print('Parsing Successful')
    else:
        print('Parsing Unsuccessful')

main()
