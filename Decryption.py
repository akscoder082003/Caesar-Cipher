def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if(char.isupper()):
            plaintext += chr((ord(char) - shift-65) %26 + 65)
        else:
            plaintext += chr((ord(char) - shift-97) %26 + 97)
    return plaintext
ciphertext = input("Enter the Ciphertext: ")
shift = int(input("Enter the Shift value: "))
print("Plaintext : ", decrypt(ciphertext, shift))