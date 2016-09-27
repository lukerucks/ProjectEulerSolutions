# bitwise xor is ^

# print  chr((ord('b') ^ ord('A')))
import string
import enchant
import re


d = enchant.Dict("en_US")


def p59():
    possible_keys = string.ascii_lowercase
    f = open('p059_cipher.txt', 'r')
    for line in f:
        line = line.strip('\n')
        line = line.split(',')
        for key_1 in possible_keys:
            for key_2 in possible_keys:
                for key_3 in possible_keys:
                    total_line = ""
                    keys = [key_1, key_2, key_3]
                    key_num = 0
                    for char in line:
                        encrypted_char = int(char)
                        real_char = ord(keys[key_num % 3]) ^ encrypted_char
                        total_line += chr(real_char)
                        key_num += 1
                    words_in_english = 0
                    total_words = 0
                    words = re.split(r'[(;,.!?:\s)]s*', total_line)
                    for word in words:
                        if word and d.check(word):
                            words_in_english += 1
                        total_words += 1
                    if float(words_in_english) / total_words > 0.8:
                        print 'Solution!'
                        print words
                        print '\n'
                        print total_line
                        print keys
                        return total_line
                    # elif words_in_english > 10:
                    #     print 'PARTIAL:'
                    #     print words
                    #     print ""
                    #     print total_line
                    #     print 'END'




text = p59()
total = 0
for char in text:
    total += ord(char)
print total
