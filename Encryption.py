"""
This function encrypts a message using a Caesar cipher.
Args:
    plaintext (str): The message to be encrypted.
    shift (int): The number of letters to shift in the plaintext by.
Returns:
    The encrypted message.
"""
def encrypt(plaintext, shift):
# Create an empty string to store the encrypted message.
    ciphertext = ""
# Iterate over each character in the plaintext.
    for char in plaintext:
# Check if the character in uppercase.
        if(char.isupper()):
# Add the encrypted version of the character to the ciphertext.
            ciphertext += chr((ord(char) + shift-65) %26 + 65)
# Check if the character is lowercase.
        else:
# Add the encrypted version of the character to the ciphertext.
            ciphertext += chr((ord(char) + shift-97) %26 + 97)
# Return the encrypted message.
    return ciphertext

def main():
    # Get the plaintext from the user.
    plaintext = input("Enter the Plaintext: ")
    # Get the shift value from the user.
    shift = int(input("Enter the Shift value: "))
    # Encrypt the plaintexr and print the ciphertext.
    print("Ciphertext : ", encrypt(plaintext, shift))
    
if __name__ == "__main__":
    main()