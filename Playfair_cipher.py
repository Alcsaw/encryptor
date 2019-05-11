from sys import argv
from sys import exc_info

'''
https://en.wikipedia.org/wiki/Playfair_cipher

To perform the substitution, apply the following 4 rules, in order, to each pair of letters in the plaintext:

1. If both letters are the same (or only one letter is left), add an "X" after the first letter. Encrypt the new pair
    and continue. Some variants of Playfair use "Q" instead of "X", but any letter, itself uncommon as a repeated pair,
    will do. -> make_pairs()
2. If the letters appear on the same row of your table, replace them with the letters to their immediate right
    respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of
    the row). row_rule()
3. If the letters appear on the same column of your table, replace them with the letters immediately below respectively
    (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column).
    -> column_rule()
4. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at
    the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter
    of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.
    -> rectangle_rule()
'''

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def verify_input(plaintext, keyword):
    # Currently only lower case letters are supported. The keyword must be, at least 1 character long.
    if len(keyword):
        return plaintext.replace(" ", "").lower(), keyword.replace(" ", "").lower()
    return False


def playfair_cipher(plaintext, key_table):
    pass


def make_key_table(key):
    # To generate the key table, one would first fill in the spaces in the table with the letters of the keyword,
    # dropping any duplicate letters, then fill the remaining spaces with the rest of the letters of the alphabet, in
    # order, and usually omitting "J" (or "Q") to reduce the alphabet to fit (some other versions put both "I" and "J"
    # in the same space).
    # The key is written in the top rows of the table, from left to right (although it can be in some other pattern,
    # such as a spiral beginning in the upper-left-hand corner and ending in the center). The keyword together with the
    # conventions for filling in the 5 by 5 table constitute the cipher key.

    table = []
    pointer_key = 0
    pointer_alphabet = 0

    for i in range(5):
        #print(table)
        row = []
        for j in range(5):
            # print(table)

            finished = False
            while not finished:
                repeated_char = False
# list(dict.fromkeys(mylist)) # Removes duplicates, use it instead of the current implementation for filling the key
                if pointer_key < len(key):
                    current_char_key = key[pointer_key]
                    pointer_key += 1

                    if current_char_key in row:
                        repeated_char = True
                    else:
                        for table_row in table:
                            if current_char_key in table_row:
                                repeated_char = True

                    if not repeated_char:
                        row.append(current_char_key)
                        finished = True

                else:
                    current_char_alphabet = ALPHABET[pointer_alphabet]
                    pointer_alphabet += 1

                    # Q is omitted so the whole alphabet can fit in the table
                    if current_char_alphabet == 'q':
                        repeated_char = True

                    if current_char_alphabet in row:
                        repeated_char = True

                    for table_row in table:
                        if current_char_alphabet in table_row:
                            repeated_char = True

                    if not repeated_char:
                        row.append(current_char_alphabet)
                        finished = True
        # print("ROW", row)
        table.insert(i, row)
    return table


def make_pairs(plaintext):
    # The inputted plaintext must be reorganized into tuples of 2 characters. If both letters of a tuple are equal, an
    # extra letter 'q' must be added after the first.
    pairs = []
    # transformar a strign em lista e add o Q na lista tbm
    pointer = 0
    for i in range(0, len(list_plaintext), 2):
        current_pair = plaintext[i:i + 2]
        if current_pair[0] == current_pair[1]:
            current_pair[1] = 'q'


def row_rule():
    # test
    pass


def column_rule():
    # test
    pass


def rectangle_rule():
    # test
    pass


def main():
    if argv[1] == '-h':
        print("HELP!")
        plaintext = 'ATTACKATDAWN'.lower()
        key = 'LEMON'.lower()
        expected_answer = 'LXFOPVEFRNHR'

        print("Plain Text: ", plaintext)
        print("Key: ", key)
        print("Expected Answer: ", expected_answer)

        print("The actual answer:", playfair_cipher(plaintext, key))

    else:
        try:
            plaintext = argv[1]
            key = argv[2]
            print('ENCRYPTED:')
            print(playfair_cipher(plaintext, key))
        except:
            e = exc_info()[0]
            print("ERROR: ", e)
            print("ARGS: ", argv)


if __name__ == '__main__':
    main()
