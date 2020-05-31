# Python3
# Here is my code:

# Imports 
import csv


# Morse code Dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

# Encryption:
def encryption(message):
    my_cipher = ''
    for my_letter in message:
        if my_letter != ' ':
            my_cipher += MORSE_CODE_DICT[my_letter] + ' '
        else:
            my_cipher += ' / '    
    return my_cipher

user_input = input("Enter Anything: ")

encrypted_output = encryption(user_input.upper()) 
print (encrypted_output)
