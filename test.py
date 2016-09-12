import itertools
lst = ['Under', 'the', 'Dome', 'King']
combinatorics = itertools.product([True, False], repeat=len(lst) - 1)

solution = []
for combination in combinatorics:
    i = 0
    one_such_combination = [lst[i]]
    for slab in combination:
        i += 1
        if not slab: # there is a join
            one_such_combination[-1] +=' '+lst[i]
        else:
            one_such_combination += [lst[i]]
    solution.append(one_such_combination)

print solution