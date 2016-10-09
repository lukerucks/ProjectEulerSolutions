def get_trianlge_number(n):
    return int(0.5*(n)*(n+1))

def make_triangle_numbers(max_number):
    triangle_numbers = {}
    for number in range(1, max_number):
        current = get_trianlge_number(number)
        triangle_numbers[current] = number
    return triangle_numbers


def find_word_value(word):
    letter_values = {'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 
    'I':9, 'J':10, 'K':11, 'L': 12, 'M': 13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18,
    'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z': 26}
    value = 0
    for letter in range(len(word)):
        value += letter_values[word[letter].capitalize()]
    return value

def problem_42():
    triangle_numbers = make_triangle_numbers(600)
    word_list = []
    number_of_triangular_words = 0
    f = open('p042_words.txt', 'r')
    word_list = f.read()
    word_list = word_list.split(',')
    word_list = [word.strip('"') for word in word_list]
    for word in word_list:
        if find_word_value(word) in triangle_numbers:
            number_of_triangular_words += 1
    print number_of_triangular_words
    return number_of_triangular_words



problem_42()
