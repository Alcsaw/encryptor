import sys
from collections import UserList
import secrets


# A circular list is needed in order to handle a shift of the later letters of the alphabet
class CircularList(UserList):

    def __getitem__(self, index):
        real_index = index % len(self.data)
        return super().__getitem__(real_index)


ALPHABET = CircularList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


def get_key(plaintext):

    # The key must to be as long as the plaintext and composed with random characters

    key = [secrets.choice(ALPHABET) for i in range(len(plaintext))]
    print("KEY: ", key)
    return key


def onetime_pad(plaintext):

    ciphertext = ''
    key = get_key(plaintext)
    # print(key)

    for pointer, plain_text_char in enumerate(plaintext):
        # Locates que index of the current plain text char
        plain_text_char_index = ALPHABET.index(plain_text_char)
        # Locates que index of the current key char
        key_char_index = ALPHABET.index(key[pointer])

        # Debug trash
        # print(ALPHABET[ALPHABET.index(plain_text_char)])
        # print(ALPHABET[ALPHABET.index(key[pointer])])
        # print(ALPHABET[top_letter_index + left_letter_index])
        ciphertext += ALPHABET[plain_text_char_index + key_char_index]

    return ciphertext


if sys.argv[1] == '-h':
    print("HELP!")
    plaintext = 'ATTACKATDAWN'.lower()
    # key = 'LEMON'.lower()
    expected_answer = 'LXFOPVEFRNHR'

    print("Plain Text: ", plaintext)
    print("Key: ", key)
    print("Expected Answer: ", expected_answer)

    print("The actual answer:", onetime_pad(plaintext))

else:
    try:
        plaintext = sys.argv[1]
        # key = sys.argv[2]
        print('ENCRYPTED:')
        print(onetime_pad(plaintext))
    except:
        e = sys.exc_info()#[0]
        print("ERROR: ", e)
        print("ARGS: ", sys.argv)


