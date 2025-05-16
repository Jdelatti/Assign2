import os
import ast

def encode(word):
    return [ord(char) for char in word.lower()]

def decode(encoded_list):
    return ''.join(chr(num) for num in encoded_list)

env1 = os.getenv('ENV1')
env2 = os.getenv('ENV2')

if env1 is None or env2 is None:
    raise ValueError("Environment variables must be set.")

number1 = ast.literal_eval(env1)
number2 = ast.literal_eval(env2)

print('''
The secret animal can be found in files in subfolders 1-6 of folders 1 and 2.
The letters of this secret animal are inside of files that start with the letters
of the word 'findme'. Put the letters of the animal together and enter it.
'''.strip())
print("")
user_word = input("Enter the secret animal: ")

# Encode the user's word
user_encoded = encode(user_word)

# Check if the encoded words match
if user_encoded == number1:
    print()
    print("That is right!!!")
    print()
    print(f"The super-duper-secret animal is: {decode(number2)}" )
    print()
else:
    print()
    print("Sorry, that's not the secret animal.")
    print()
