import numpy as np
# import itertools

def generate_type(func):
    array = np.zeros(10000)
    current = 1
    answer = 1
    while answer < 10000:
        array[answer] = 1
        current += 1
        answer = func(current)
    return array


def triangle(n):
    return n*(n+1) / 2

def square(n):
    return n * n

def pentagonal(n):
    return n * (3*n - 1) / 2

def hexagonal(n):
    return n * (2*n - 1)

def heptagonal(n):
    return n * (5*n - 3) / 2

def octagonal(n):
    return n * (3*n - 2)

def array_to_list(array):
    l = []
    for item in range(len(array)):
        if array[item] and item > 999:
            l.append(item)
    return l


triangle_array = generate_type(triangle)
square_array = generate_type(square)
pentagonal_array = generate_type(pentagonal)
hexagonal_array = generate_type(hexagonal)
heptagonal_array = generate_type(heptagonal)
octagonal_array = generate_type(octagonal)

triangle_list = array_to_list(triangle_array)
square_list = array_to_list(square_array)
pentagonal_list = array_to_list(pentagonal_array)
hexagonal_list = array_to_list(hexagonal_array)
heptagonal_list = array_to_list(heptagonal_array)
octagonal_list = array_to_list(octagonal_array)


def num_type(n):
    '''checks to see if a number is a triangle, square,
    pentagonal, hexagonal, heptagonal, or octagonal number.
    Returns set of all types that it is.'''
    types = []
    for array, code in [(triangle_array, 'tri'),
                        (square_array, 'sq'),
                        (pentagonal_array, 'pent'),
                        (hexagonal_array, 'hex'),
                        (heptagonal_array, 'hep'),
                        (octagonal_array, 'oct')]:
        if array[n]:
            types.append(code)
    return types


type_array = np.zeros(10000, dtype=list)
for n in range(1, 10000):
    type_array[n] = num_type(n)


def is_set_polygonal(number_set):
    '''see if set contains each polygonal type in unique numbers'''
    # first check to see that all of the polygon types are here
    contains = {'tri':[], 'sq':[], 'pent':[], 'hex':[], 'hep':[], 'oct':[]}
    for num in number_set:
        if not type_array[num]:
            return False
        for n_type in type_array[num]:
            contains[n_type].append(num)
    for entry in contains:
        if not contains[entry]:
            return False

    # now check to see if we can find a combination that works
    values = {}
    decided = {x: False for x in contains}
    has_changed = True
    set_random_assignment = False
    current_height = 2
    while has_changed:
        has_changed = False
        for entry in contains:
            if len(contains[entry]) == 1 and not decided[entry]:
                values[contains[entry][0]] = entry
                decided[entry] = True
                remove_from_set(contains, contains[entry][0])
                has_changed = True
            elif len(contains[entry]) == 0 and not decided[entry]:
                return False

        # We'll randomly assign if we have no automatic assignments
        if not has_changed and not set_random_assignment:
            set_random_assignment = True
            for entry in contains:
                if len(contains[entry]) == current_height:
                    values[contains[entry][0]] = entry
                    decided[entry] = True
                    remove_from_set(contains, contains[entry][0])
                    has_changed = True
                    set_random_assignment = False
            if set_random_assignment:
                current_height += 1
                if current_height <= len(contains):
                    set_random_assignment = False

    # check to see if all numbers are given a polygonal assignment
    for assignment in values:
        if not values[assignment]:
            return False
    return True


def remove_from_set(s, to_be_removed):
    for l in s:
        if to_be_removed in s[l]:
            loc = s[l].index(to_be_removed)
            s[l] = s[l][0:loc] + s[l][loc+1:]


def is_cyclical(s):
    '''see if a set is cyclical'''
    for item in range(len(s)):
        if str(s[item])[0:2] != str(s[item-1])[2:]:
            return False
    return True


def get_possible_next(n):
    '''get possible cyclical next numbers'''
    assert n >= 1000
    x = int(str(n)[2:]) * 100
    return range(x+10, x + 100)


def p061():
    answers = []
    for lvl_1 in triangle_list:
        if int(str(lvl_1)[2:]) < 10:
            continue
        for lvl_2 in get_possible_next(lvl_1):
            if not type_array[lvl_2]:
                continue
            for lvl_3 in get_possible_next(lvl_2):
                if not type_array[lvl_3]:
                    continue
                for lvl_4 in get_possible_next(lvl_3):
                    if not type_array[lvl_4]:
                        continue
                    for lvl_5 in get_possible_next(lvl_4):
                        if not type_array[lvl_5]:
                            continue
                        for lvl_6 in get_possible_next(lvl_5):
                            if not type_array[lvl_6] or str(lvl_6)[2:] != str(lvl_1)[0:2]:
                                continue
                            if is_set_polygonal([lvl_1, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6]):
                                return [lvl_1, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6]
                            
# print len(triangle_list) * len(square_list) * len(hexagonal_list) * len(heptagonal_list) * len(octagonal_list)*len([x for x in itertools.permutations([1,2,3,4,5,6])])
# print 90**6
answer = p061()
print answer
print sum(answer)
