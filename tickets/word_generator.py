########################################
# 1. Take in two arguments number of bits and plain DATABASESt
# 2. Returns a string based on input argument max_length
#
# Written by James jchen
# Date: 2019-08-30
########################################

from datetime import datetime
import string


class Word():
    def select_character(chr):
        characters = string
        printable = characters.printable
        print(printable[0:94])
        i = 0
        while (i < len(printable)):
            print(i)
            i = i + 1
            """
            if chr == printable[i+1:i+2]:
                print(printable[i-1:i])
                print(i)
                print(len(printable))
            i = i + 1
            """
        return printable[62:63]

    def generator(letter):
        formatter = ''
        non = str(datetime.now().__getattribute__('microsecond'))
        key = 'jami'
        filler = 'hell'
        initial = 'jc'

        characters = string
        printable = characters.printable
        letters = printable[61:62]
        print(letters)
        print(printable[0:94])

        # 62 numeric, lowercase, uppercase
        words = [non, key, non, filler, non, filler, initial]
        word = formatter.join(words)
        chr = 'A'
        text = Word.select_character(chr)
        print(text)
        # select(chr)
        return word

        # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c

# 0123456789
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# a character at a time; cycle through prinatable characers for
# for example 'A' is the first row and divisible by value x if so
# Y would be represented by the fifth row if every row has five characters
# initial acts as a key
#
# expand is used to build a higher number of bits for word
# since the resultant word will always be a power of 2.
# example would be for every character there exist
# for every 8 bits there is a byte
# 643923jami643923hell643923helljc

w = Word()
end = w.generator()
print(end)
