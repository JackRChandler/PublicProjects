from collections import deque

input_data = open("InputMovesDay05Example.txt").read()
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]

crates = []
for stack in stackt:
    crates.append(deque(stack))


print(stackt)
print(instructions)
print(crates)
