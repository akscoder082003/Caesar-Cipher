# Caesar-Cipher


Code explained here:
caesar_decrypt is a function that takes two arguments: a ciphertext and a shift value. The ciphertext is the encrypted message, and the shift value is the number of positions that each letter in the ciphertext should be shifted to decrypt it.

The function works by first creating a new string called plaintext. Then, it iterates through each character in the ciphertext string. For each character, it checks if the character is a letter. If it is, the function then converts the character to its ASCII code. Then, it adds the shift value to the ASCII code and performs a modulo operation on the result to get a value between 0 and 25. Finally, it converts the resulting value back to a letter and adds it to the plaintext string.

If the character is not a letter, the function simply adds it to the plaintext string without any changes.

Once the function has iterated through all of the characters in the ciphertext string, it returns the plaintext string.

Output:
