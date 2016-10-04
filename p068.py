import itertools

def create_magic_5(pattern):
    '''take a list, return '0' if it isn't a magic 5 gon-ring, 
    or the identifier string matching it if it is'''

    sets = [ [[], [], []] for x in range(len(pattern) / 2)]
    current = 0
    while current < len(pattern)/2:
        sets[current][0] = pattern[current]
        current += 1
    while current < len(pattern):
        sets[current - len(pattern)/2][1] = pattern[current]
        sets[current - len(pattern)/2 - 1][2] = pattern[current]
        current += 1
    # Make sure it is a possible magic 5-gon ring
    total = sum(sets[-1])
    for i in range(len(pattern) / 2):
        if sum(sets[i]) != total:
            return "0"

    # Rotate into the correct order
    lowest = 10
    lowest_place = -1
    for i in range(len(sets)):
        if sets[i][0] < lowest:
            lowest = sets[i][0]
            lowest_place = i
    for i in range(lowest_place):
        new_last = sets.pop(0)
        sets.append(new_last)

    # convert to string
    set_string = ""
    for line in sets:
        for digit in line:
            set_string += str(digit)
    return set_string

def p068():
    max_perm = 0
    counter = 0
    for permutation in itertools.permutations([1,2,3,4,5,6,7,8,9,10]):
        set_string = create_magic_5(permutation)
        if len(set_string) > 1:
            print set_string
        if int(set_string) > max_perm and len(set_string) == 16:
            print "New max! Was {}, is now {}.".format(max_perm, set_string)
            max_perm = int(set_string)

        counter += 1
    return max_perm

print p068()


