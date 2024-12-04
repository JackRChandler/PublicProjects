elves = open("inputs/day1.txt", "r").read().split("\n\n")
totals = []
for elf in elves: 
    totals.append(sum([int(x) for x in elf.split("\n")]))
print("Part 1:", max(totals))
