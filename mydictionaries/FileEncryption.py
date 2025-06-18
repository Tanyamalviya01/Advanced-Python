# encryption codes
codes = {'A': '%', 'B': '@', 'C': '!', 'D': '&', 'E': '*', 'F': '^', 
    'G': '(', 'H': ')', 'I': '_', 'J': '+', 'K': '{', 'L': '}',
    'M': '|', 'N': ':', 'O': '"', 'P': '<', 'Q': '>', 'R': '?',
    'S': '~', 'T': '1', 'U': '2', 'V': '3', 'W': '4', 'X': '5',
    'Y': '6', 'Z': '7', 'a': '9', 'b': '#', 'c': '0', 'd': '8', 
    'e': '[', 'f': ']', 'g': ';', 'h': "'", 'i': ',', 'j': '.',
    'k': '/', 'l': '-', 'm': '=', 'n': '\\', 'o': '`', 'p': '$',
    'q': '%', 'r': '@', 's': '!', 't': '&', 'u': '*', 'v': '^', 
    'w': '(', 'x': ')', 'y': '_', 'z': '+', ' ': ' '}

file = open('info_security.txt', 'r') # open info_security.txt file
text = file.read() # read file content of the file
file.close() # close input file

encrypted_text = '' # string to store encrypted text

for char in text: # encrypt each character
    if char in codes:
        encrypted_text = encrypted_text + codes[char]
    else:
        encrypted_text = encrypted_text + char

output_file = open('encrypted.txt', 'w') # open file to write to
output_file.write(encrypted_text) # write the encrypted content to file
output_file.close() # close the output file