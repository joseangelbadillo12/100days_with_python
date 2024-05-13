# Part 1: Implement a Caesar cipher that shifts all letters by a fixed number of positions.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'endcode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
new_alphabet = []

def encrypt(text, shift):
    cipher_text = ""
    for letters in text:
        alphabet_index = alphabet.index(letters)
        new_index = alphabet_index + shift
        if new_index > 25:
            new_index -= 26
        new_letter = alphabet[new_index]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(text, shift)