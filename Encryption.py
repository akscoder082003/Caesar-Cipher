def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Get user input
ciphertext = input("Enter the Plaintext: ")
shift = int(input("Enter the shift value: "))

# Call the decryption function
plaintext = caesar_decrypt(ciphertext, shift)

# Display the decrypted plaintext
print("Incrypted plaintext:", plaintext)
