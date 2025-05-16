def decode(encoded_list):
    return ''.join(chr(int(num)) for num in encoded_list)


user_input = input("Enter the numeric codes separated spaces (e.g., 99, 97, 116): ")

try:
    encoded_list = user_input.split(' ')
    decoded_word = decode(encoded_list)
    
    print(f"The decoded word is: {decoded_word}")

except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")