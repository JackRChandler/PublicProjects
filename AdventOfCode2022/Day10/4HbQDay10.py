# X, part1, part2 = 1, 0, '\n'
# for cycle, value in enumerate(open('Day10Input.txt').read().split(), 1):
#     part1 += cycle * X  if cycle%40==20              else 0
#     part2 += '#'        if abs((cycle-1)%40 - X) < 2 else ' '
#     X     += int(value) if value[-1].isdigit()       else 0
# print(part1, *part2)

from itertools import accumulate

# f = lambda x: int(x) if x[-1].isdigit() else 0
# xs = [*map(f, open('Day10Input.txt').read().split())]
#
# part1, part2 = 0, '\n'
# for i, x in enumerate(accumulate([1]+xs), 1):
#     part1 += i*x if i%40==20 else 0
#     part2 += '#' if (i-1)%40-x in [-1,0,1] else ' '
#
# print(part1, *part2)

import itertools as it
import sys

instructions = (
    instruction.split() for instruction in open('Day10Input.txt').read().strip().split("\n")
)

X, x = 1, None

S = 0
crt = [[" "] * 40 for _ in range(6)]
for cycle in it.count(1):
    if cycle in (20, 60, 100, 140, 180, 220):
        S = S + cycle * X

    k = cycle - 1
    if abs((k % 40) - X) <= 1:
        crt[k // 40][k % 40] = "#"

    # Now, we can handle the instruction.
    if x is not None:
        X, x = X + x, None
    else:
        try:
            op, *args = next(instructions)
        except StopIteration:
            break

        x = int(args[0]) if op == "addx" else None

print("Part 1:", S)
print("Part 2:")
print("\n".join("".join(ln) for ln in crt))