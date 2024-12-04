import string

aoc_input = open('Day12Input.txt', 'r').read()

LetterVals = dict()
for index, letter in enumerate(string.ascii_letters):
    LetterVals[letter] = index + 1



print(LetterVals['a'])

def part1(input_aoc):
    totallist = []
    for letter in input_aoc.split():
        newline = []

        for individual in list(letter):

            if individual != 'S' and individual != 'E':
                newline.append(LetterVals[individual])
            elif individual == 'S':
                newline.append("St")
            elif individual == 'E':
                newline.append('En')
#            print(newline)
        totallist.append(newline)

    for line in totallist:
        print(line)
#    print(totallist)
 #       print(letter)


part1(aoc_input)
