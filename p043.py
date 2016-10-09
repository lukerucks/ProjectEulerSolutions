def get_number_from_list(n):
    tens = 0
    number = 0
    n.reverse()
    for each in n:
        number += each*(10**tens)
        tens += 1
    return number


def is_pandigital(n):
    compare = [0,1,2,3,4,5,6,7,8,9]
    for each in compare:
        if each not in n:
            return False
    return True


def is_pandigital_with_substring_divisibility(n):
    '''n is a list of 10 numbers, here'''
    if len(n) != 10:
        return False
    x = n[3]
    #Check for even-ness of d2d3d4
    if x != 0 and x != 2 and x != 4 and x != 6 and x!=8:
        return False
    #Check divisible by 3 of d3d4d5
    x = n[2] + n[3] + n[4]
    while x > 10:
       x = str(x)
       x = int(x[0]) + int(x[1])
    if x != 3 and x != 6 and x != 9:
        return False
    #Check divisibility by 5 of d4d5d6
    if n[6] != 0 and n[6] != 5:
        return False
    #Check divisibility by 7 of d5d6d7
    x = get_number_from_list([n[4], n[5], n[6]])
    if x % 7 !=0:
        return False
    #Check divisibility by 11 of d6d7d8
    x = get_number_from_list([n[5], n[6], n[7]])
    if x % 11 !=0:
        return False
    #Check divisibility by 13 of d7d8d9
    x = get_number_from_list([n[6], n[7], n[8]])
    if x % 13 !=0:
        return False
    #Check divisibility by 17 of d8d9d10
    x = get_number_from_list([n[7], n[8], n[9]])
    if x % 17 !=0:
        return False
    if not is_pandigital(n):
        return False
    return True


def problem_43():
    possibles = [[1,2,3,4,5,6,7,8,9], 
                [0,1,2,3,4,5,6,7,8,9],
                [0,2,4,6,8],
                [1,2,3,4,5,6,7,8,9],  #can't be 0 from divisible by 11
                [0,5],
                [0,1,2,3,4,5,6,7,8,9],
                [0,1,2,3,4,5,6,7,8,9],
                [0,1,2,3,4,5,6,7,8,9],
                [0,1,2,3,4,5,6,7,8,9],
                [0,1,2,3,4,5,6,7,8,9]]
    current = possibles[0][0]
    while current:
        pass
        

