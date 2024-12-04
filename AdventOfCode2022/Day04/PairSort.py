### Part 1

pairs = open('InputDay4.txt', 'r').read().split('\n')

contained_assignments = 0
contained_assignments_any = 0

for pair in pairs:
    keep_pairs = []
    for elf in pair.split(','):
        lower, higher = elf.split('-')
        lower_int = int(lower)
        higher_int = int(higher)
        assignment_range = range(lower_int, higher_int+1, 1)
        elf_assign = []
        for assignment in assignment_range:
            elf_assign.append(assignment)
        keep_pairs.append(elf_assign)

    for pair1, pair2 in zip(keep_pairs[:1], keep_pairs[1:]):
        pair1_set = set(pair1)
        pair2_set = set(pair2)
        if pair1_set.issubset(pair2_set) or pair2_set.issubset(pair1_set):
            contained_assignments += 1
        ### Part 2
        if pair1_set & pair2_set:
            contained_assignments_any += 1

print(contained_assignments)
print(contained_assignments_any)




