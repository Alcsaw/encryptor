import sys
from collections import UserList


# A circular list is needed in order to handle a shift of the later letters of the alphabet
class CircularList(UserList):

    def __getitem__(self, index):
        real_index = index % len(self.data)
        return super().__getitem__(real_index)


ALPHABET = CircularList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


def vigenere(plain_text, key):

    cipher_text = ''
    # Ensure the key is at least as long as the ciphertext by cat'ing it
    while len(key) < len(plain_text):
        key = key + key

    key = key[0:len(plain_text)]
    print(key)

    for pointer, plain_text_char in enumerate(plain_text):
        # Locates que index of the current plain text char horizontally on the tabula recta
        top_letter_index = ALPHABET.index(plain_text_char)
        # Locates que index of the current key char vertically on the tabula recta
        left_letter_index = ALPHABET.index(key[pointer])

        # Debug trash
        # print(ALPHABET[ALPHABET.index(plain_text_char)])
        # print(ALPHABET[ALPHABET.index(key[pointer])])
        # print(ALPHABET[top_letter_index + left_letter_index])
        cipher_text += ALPHABET[top_letter_index + left_letter_index]

    return cipher_text


plain_text = 'ATTACKATDAWN'.lower()
key = 'LEMON'.lower()

print('ENCRYPTED:')
print(vigenere(plain_text, key))
