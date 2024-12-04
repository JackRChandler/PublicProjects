import re

def partone(puzzleinput):
    #print(puzzleinput)
    stripedlines = []
    lines = puzzleinput.split('\n')
    for line in lines:
        numbers = re.findall(r'\d', line)
        #print(numbers[0], numbers[-1])
        newlist = [numbers[0] + numbers[-1]]
        stripedlines.append(newlist)
    total = sum([int(number) for sublist in stripedlines for number in sublist])
    print(total)

def parttwo(puzzleinput):
    stripedlines = []
    lines = puzzleinput.split('\n')
    for line in lines:
        newline = (line.replace("one", "one1one")
                .replace("two", "two2two")
                .replace("three", "three3three")
                .replace("four", "four4four")
                .replace("five", "five5five")
                .replace("six", "six6six")
                .replace("seven", "seven7seven")
                .replace("eight", "eight8eight")
                .replace("nine", "nine9nine"))
        numbers = re.findall(r'\d', newline)
        # print(numbers[0], numbers[-1])
        newlist = [numbers[0] + numbers[-1]]
        stripedlines.append(newlist)
    total = sum([int(number) for sublist in stripedlines for number in sublist])
    print(total)

def main():
    puzzleinput = open('input.txt', 'r').read()
    partone(puzzleinput)
    parttwo(puzzleinput)


if __name__ == "__main__":
    main()
