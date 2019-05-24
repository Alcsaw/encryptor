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
    try:
        if len(keyword):
            return plaintext.replace(" ", "").lower(), keyword.replace(" ", "").lower()
        return False
    except TypeError as e:
        print("TypeError in verify_input:", e)
        raise


def find_index(table, element):
    # Returns the 2 dimensional index of an element on a given table

    if element == 'j':
        # J is omitted, instead, this letter is considered in the same space of I in the table
        element = 'i'

    column = None
    for row, row_list in enumerate(table):
        try:
            column = row_list.index(element)
            break
        except ValueError:
            continue

    if row is not None and column is not None:
        return row, column
    else:
        return False


def playfair_cipher(text_in_pairs, key_table):

    cipher_in_pairs = []
    # TODO: Since the text_in_pairs object gets changed by reference, this function could simply return it instead of
    # creating a new object
    for pair in text_in_pairs:
        first_element_indexes = find_index(key_table, pair[0])
        second_element_indexes = find_index(key_table, pair[1])

        if not (first_element_indexes and second_element_indexes):
            print("ERROR: On function", playfair_cipher.__name__, end=". ")
            print("Couldn't find the an element of the pair", pair, "on the Key Table")
            return False

        if first_element_indexes[0] == second_element_indexes[0]:
            pair = row_rule(pair, key_table, first_element_indexes, second_element_indexes)
            if not pair:
                return False
            cipher_in_pairs.append(pair)
            #continue

        elif first_element_indexes[1] == second_element_indexes[1]:
            pair = column_rule(pair, key_table, first_element_indexes, second_element_indexes)
            if not pair:
                return False
            cipher_in_pairs.append(pair)
            #continue

        else:
            pair = rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes)
            if not pair:
                return False
            cipher_in_pairs.append(pair)

    return cipher_in_pairs


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

                    # J is omitted so the whole alphabet can fit in the table
                    if not (repeated_char or current_char_key == 'j'):
                        row.append(current_char_key)
                        finished = True

                else:
                    current_char_alphabet = ALPHABET[pointer_alphabet]
                    pointer_alphabet += 1

                    # J is omitted so the whole alphabet can fit in the table
                    if current_char_alphabet == 'j':
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
    # ideia: transformar a strign em lista e add o Q na lista tbm
    pointer = 0
    list_plaintext = list(plaintext)

    '''
     for i in range(0, len(plaintext), 2):
        current_pair = plaintext[i:i + 2]
        if current_pair[0] == current_pair[1]:
            current_pair[1] = 'q'

    for i in range(len(plaintext)/2):
        pairs[i].append(plaintext[i])
        if plaintext[i+1] == plaintext[i]:
            pairs[i].append('q')
        else:
            pairs[i].append(plaintext[i+1])
            #nope
    '''

    #while pointer+1 < len(list_plaintext):
    while len(list_plaintext) > 1:
        #print(list_plaintext)
        #if plaintext[pointer] == plaintext[pointer+1]:
        if list_plaintext[0] == list_plaintext[1]:
            # current_pair = [plaintext[pointer], 'q']
            current_pair = [list_plaintext.pop(0), 'q']
            #pointer += 1

        else:
            # current_pair = plaintext[pointer:pointer + 2]
            #current_pair = [list_plaintext.pop(pointer), list_plaintext.pop(pointer)]
            current_pair = [list_plaintext.pop(0), list_plaintext.pop(0)]
            #pointer += 2

        pairs.append(current_pair)
        #print(pairs)

    if len(list_plaintext):
        pairs.append([list_plaintext.pop(0), 'q'])

    return pairs


def row_rule(pair, key_table, first_element_indexes, second_element_indexes):
    # If the letters appear on the same row of your table, replace them with the letters to their immediate right
    # respectively (wrapping around to the left side of the row if a letter in the original pair was on the right
    # side of the row)
    row = first_element_indexes[0]

    if first_element_indexes[1] == 4:
        # last element on the row -> wrap around
        column_first = 0
    else:
        column_first = first_element_indexes[1] + 1

    if second_element_indexes[1] == 4:
        # last element on the row -> wrap around
        column_second = 0
    else:
        column_second = second_element_indexes[1] + 1

    # print(key_table[row][column_first])
    pair[0] = key_table[row][column_first]
    pair[1] = key_table[row][column_second]

    # How to check for errors?
    # print("ERROR: On function", row_rule.__name__, end=". ")
    # print("Couldn't encrypt the pair", pair, end=".\n")
    # return False

    return pair


def column_rule(pair, key_table, first_element_indexes, second_element_indexes):
    # If the letters appear on the same column of your table, replace them with the letters immediately below
    # respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom
    # side of the column).
    column = first_element_indexes[1]

    if first_element_indexes[0] == 4:
        # last element on the column -> wrap around
        row_first = 0
    else:
        row_first = first_element_indexes[0] + 1

    if second_element_indexes[0] == 4:
        # last element on the row -> wrap around
        row_second = 0
    else:
        row_second = second_element_indexes[0] + 1

    pair[0] = key_table[row_first][column]
    pair[1] = key_table[row_second][column]
    # Errors?
    # print("ERROR: On function", column_rule.__name__, end=". ")
    # print("Couldn't encrypt the pair", pair, end=".\n")
    # return False

    return pair


def rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes):
    # If the letters are not on the same row or column, replace them with the letters on the same row respectively,
    # but at the other pair of corners of the rectangle defined by the original pair. The order is important!
    # The first letter of the encrypted pair is the one that lies on the same row as the first letter of the
    # plaintext pair.

    row_first = first_element_indexes[0]
    column_first = second_element_indexes[1]

    row_second = second_element_indexes[0]
    column_second = first_element_indexes[1]

    pair[0] = key_table[row_first][column_first]
    pair[1] = key_table[row_second][column_second]

    return pair


def playfair_encrypt(plaintext, key):
    try:
        plaintext, key = verify_input(plaintext, key)
    except TypeError as e:
        print("TypeError in", playfair_encrypt.__name__, ":", e)
        raise
    else:
        plaintext_pairs = make_pairs(plaintext)
        key_table = make_key_table(key)

        ciphertext_pairs = playfair_cipher(plaintext_pairs, key_table)
        print("CIPHERTEXT PAIRS:", ciphertext_pairs)

        ciphertext = ""
        for pair in ciphertext_pairs:
            print(pair)
            ciphertext += "".join(pair)

        return ciphertext


def playfair_decrypt(ciphertext, key):
    pass


def main():
    if argv[1] == '-h':
        print("HELP!")
        plaintext = "tttest with some words TEST  "
        key = "ChuCHU COM BaNaNa"

        expected_answer = 'LXFOPVEFRNHR'

        print("Plain Text: ", plaintext)
        print("Key: ", key)
        print("Expected Answer: ", expected_answer)

        print("The actual answer:", playfair_cipher(plaintext, key))

    else:
        try:
            plaintext = argv[1]
            key = argv[2]

        except:
            e = exc_info()[0]
            print("ERROR: ", e)
            print("ARGS: ", argv)
        else:
            print('ENCRYPTED:')
            print(playfair_cipher(plaintext, key))


if __name__ == '__main__':
    main()
