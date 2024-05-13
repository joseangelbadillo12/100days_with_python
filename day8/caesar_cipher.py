# Part 1: Implement a Caesar cipher that shifts all letters by a fixed number of positions.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'endcode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(text, shift):
#     cipher_text = ""
#     for letters in text:
#         alphabet_index = alphabet.index(letters)
#         new_index = alphabet_index + shift
#         if new_index > 25:
#             new_index -= 26
#         new_letter = alphabet[new_index]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     decrypted_text = ""
#     for letters in text:
#         alphabet_index = alphabet.index(letters)
#         new_index = alphabet_index - shift
#         if new_index < 0:
#             new_index += 26
#         new_letter = alphabet[new_index]
#         decrypted_text += new_letter
#     print(f"The decoded text is {decrypted_text}")

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

def caesar(text, shift, direction):
    answer = ""
    for letters in text:
        alphabet_index = alphabet.index(letters)
        if direction == "decode":
            shift *= -1
        new_index = alphabet_index + shift
        answer += alphabet[new_index]
    print(f"The {direction}d text is {answer}")

caesar(text, shift, direction)