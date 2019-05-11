from Playfair_cipher import *


# Playfair Cipher Tests:

def test_verify_input(plaintext, key):
    returned_values = verify_input(plaintext, key)

    if not returned_values:
        print("Error (keyword is missing) in", verify_input.__name__)
        return False

    for value in returned_values:
        for char in value:
            if char.isspace() or char.isupper():
                print(verify_input.__name__, "function returned a character that is not supported. Value with error:",
                                             char)
                print("Returned values:", returned_values)
                return False
    return True


def test_playfair_cipher(plaintext, key_table):
    pass


def test_make_key_table(key):
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    table = make_key_table(key)
    #print(table)
    # The table must be 5x5 and contain only lower cases letters
    if len(table) != 5:
        print(make_key_table.__name__, "function is returning a list that is not 5x5 in size.")
        return False

    for row in table:
        if len(row) != 5:
            print(make_key_table.__name__, "function is returning a list that is not 5x5 in size.")
            return False
        for char in row:
            if not char.isalpha() or not char.islower():
                print(make_key_table.__name__, "function is returning a non letter character of an upper case letter."
                                               "Value with error:", row)
                return False

            try:
                ALPHABET.remove(char)
            except ValueError:
                print("ERROR in function", make_key_table.__name__, "\nThe letter", char, "appeared more than once.")
                print("Table:")
                for i in table:
                    print(i)
                return False

    if len(ALPHABET) == 0 or not (len(ALPHABET) == 1 and ALPHABET[0] == 'q'):
        print(ALPHABET)
        print("ERROR: The table returned from the", make_key_table.__name__, "function doesn't fit the whole alphabet.")
        return False

    # Also, the table must contain every character of the key
    # I've seen this code for the same purpose and I want to test it later:
    # result = all(elem in list1 for elem in list2)
    for char in key:
        found = False

        for row in table:
            if char in row:
                found = True
        if not found:
            print("ERROR:", make_key_table.__name__, "function is returning a table that doesn't contain every letter"
                                                     "of the key. Missing character:", char)
            print("Table:")
            for row in table:
                print(row)
            return False
    return True


def test_make_pairs(plaintext):
    pairs = make_pairs(plaintext)

    for pair in pairs:
        # The plaintext must be separated into pair, always
        if len(pair) != 2:
            print(make_pairs.__name__, "function is returning something other than a pair. Value with error:", pair)
            return False
        # And the pair cannot have the same letter twice
        if pair[0] == pair[1]:
            # But if the repeated letter is the special inserted, there's no much to do...
            # This is, for example, if we have a word that (for some reason) ends up with Q and have an even length
            # In this case the algorithm would make a pair of QQ.
            if pair[0] != 'q':
                print(make_pairs.__name__, "function is returning a pair with repeated letters. Value with error:", pair)
                return False


def test_row_rule():
    # test
    pass


def test_column_rule():
    # test
    pass


def test_rectangle_rule():
    # test
    pass


plaintext = "test test test TEST  "
key = "ChuCHU COM BaNaNa"

print(test_verify_input.__name__, "|", test_verify_input(plaintext, key))
#print(test_playfair_cipher.__name__, "|", test_playfair_cipher(plaintext, key_table))
key = "chuchucombanana"
print(test_make_key_table.__name__, "|", test_make_key_table(key))
#print(make_pairs.__name__, "|", test_make_pairs(plaintext))
