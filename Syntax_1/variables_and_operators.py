# Comments in python begin with a single hashtag

x = 10 # Variables are declared and initialized without type keywords 
print(x) # A value can be printed out using the print function

x = 23 # Variables can be reassigned 
print(x)

y = None # Variables can be declared but not assigned to a value 
# by using the keyword "None" (null doesn't exist in python)
print(y)

y = 2

z = ( x + y)/x + (78%3) #usual mathematical operations supported 
print(z)

letter= 'c'
print(letter) # The type of a variable can be checked
letter = ord(letter)
print(f'the ascii value of {chr(letter)} is {letter}') # ord() function returns the
letter = letter + 2
print(f'after adding 2 to the character, its new value is {letter} which corresponds to {chr(letter)}') # ascii value and chr() converts it back

string = "hello world"
print(string) # Strings can be
string = bytes(string, 'utf-8')
print (f'when the string is converted to bytes: {string} and its type is {type(string)}') # converted to bytes
print(chr(string[0])) # individual characters in a byte string can be accessed
print(chr(string[0]-32)) # and manipulated