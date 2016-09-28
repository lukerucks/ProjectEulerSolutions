# from itertools import permutations


def p062():
    cubes = set()
    min_n = 1
    max_n = 50000
    for i in xrange(min_n, max_n):
        cubes.add(i**3)
    for i in xrange(min_n, max_n):
        cube = i**3
        # want the bottom permutation
        ii = i + 1
        max_cube_with_same_len = ii**3
        possible_permutations = []
        while len(str(max_cube_with_same_len)) == len(str(cube)):
            possible_permutations.append(max_cube_with_same_len)
            ii += 1
            max_cube_with_same_len = ii**3
        cube_permutations = [i**3]
        for p in possible_permutations:
            if is_permutation(cube, p):
                cube_permutations.append(p)
        if len(cube_permutations) == 5:
            return i, cube, cube_permutations
        elif len(cube_permutations) >= 3:
            print "FOUND SMALLER ONE!", i, cube_permutations


def is_permutation(n, m):
    return sorted([int(x) for x in str(n)]) == sorted([int(x) for x in str(m)])


print p062()
# (5027, 127035954683, [127035954683, 352045367981, 373559126408, 569310543872, 589323567104])
# [Finished in 220.3s]

# def get_permutations(n):
#     "take in number n, return list of permutations of n"
#     n_list = []
#     for char in str(n):
#         n_list.append(int(char))
#     all_perms = set()
#     for perm in permutations(n_list):
#         if perm[0] == 0:
#             continue
#         else:
#             all_perms.add(make_int_from_list(perm))
#     return all_perms


# def make_int_from_list(l):
#     answer = ""
#     for num in l:
#         answer += str(num)
#     return int(answer)

# print len(get_permutations(499**3))

