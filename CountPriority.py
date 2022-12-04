#### Part 1
import string

LetterVals = dict()
for index, letter in enumerate(string.ascii_letters):
    LetterVals[letter] = index + 1

# print(LetterVals['A'])

rucksacks = open('InputDay3.txt', 'r').read().split('\n')
CompartmentValue = []
for rucksack in rucksacks:
    compartment1 = slice(0,len(rucksack)//2)
    compartment2 = slice(len(rucksack)//2, len(rucksack))
    print(rucksack[compartment1], rucksack[compartment2])
    for char in rucksack[compartment1]:
        if char in rucksack[compartment2]:
            #print(LetterVals[char])
            CompartmentValue.append(LetterVals[char])
            break

print(sum(CompartmentValue))
# print(rucksacks)

#### Part 2

LetterVals = dict()
for index, letter in enumerate(string.ascii_letters):
    LetterVals[tuple(letter)] = index + 1

rucksacks = open('InputDay3.txt', 'r').read().split('\n')
newrucksacks = []
badgegroupsize = 3
for rucksack in range(0, len(rucksacks), badgegroupsize):
    newrucksacks.append(rucksacks[rucksack:rucksack+badgegroupsize])

badgesTotal = []
for badgegroup in newrucksacks:
    badge = set.intersection(*map(set, badgegroup))
#    print(LetterVals[tuple(badge)])
    badgesTotal.append(LetterVals[tuple(badge)])

print(sum(badgesTotal))
