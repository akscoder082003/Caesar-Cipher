"""
This function decrypts a ciphertext using a caesar cipher.
Parameters:
        ciphertext: The ciphertext to be decrypted.
Returns:
        shift: The number of positions to shift the letters in the ciphertext.
"""
def decrypt(ciphertext, shift):
# Create a blank string to store the plaintext.
    plaintext = ""
# Loop through each character in the ciphertext.
    for char in ciphertext:
# Check if the character is uppercase.
        if(char.isupper()):
# Decrypt the character by shifting it by the specified number of positions.
            plaintext += chr((ord(char) - shift-65) %26 + 65)
# Check if the character is lowercase.
        else:
# Decrypt the character by shifting it by the specified number of positions.
            plaintext += chr((ord(char) - shift-97) %26 + 97)
# Return the plaintext.
    return plaintext
# Get the ciphertext from the user.
ciphertext = input("Enter the Ciphertext: ")
# Get the shift value from the user.
shift = int(input("Enter the Shift value: "))
# Decrypt the ciphertext and print the plaintext.
print("Plaintext : ", decrypt(ciphertext, shift))