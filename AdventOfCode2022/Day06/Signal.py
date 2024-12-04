input = open('Day06Input.txt', 'r').read()


def hasRepeatedChars(s, start, end):
    input_check = input[start:end]
    for i in range(len(input_check)):
        if i != s.rfind(s[i]):
            return True
    return False


def part1(datastream):
    end = 4
    start = 0
    has_repeated = 0
    while len(datastream) > end:
        input_check = datastream[start:end]
        if hasRepeatedChars(input_check, start, end):
#            print(input_check, " has repeated characters")
            has_repeated += 1
        else:
#            print(input_check, " has no repeated characters")
            print(end, "Part 1")
            break
    #    print(input[start:end])
    #    print(input[start:end])
        end += 1
        start += 1

#    print(has_repeated)

def part2(datastream):
    end = 14
    start = 0
    has_repeated = 0
    while len(datastream) > end:
        input_check = datastream[start:end]
        if hasRepeatedChars(input_check, start, end):
#            print(input_check, " has repeated characters")
            has_repeated += 1
        else:
#            print(input_check, " has no repeated characters")
            print(end, " Part 2")
            break
    #    print(input[start:end])
    #    print(input[start:end])
        end += 1
        start += 1

#    print(has_repeated)

part1(input)

part2(input)



