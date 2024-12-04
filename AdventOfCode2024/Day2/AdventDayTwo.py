
def partone(puzzleinput):
    safereports = 0
    levels = puzzleinput.split('\n')
    for level in levels:
        level = [int(x) for x in level.split()]
        issafe = True
        direction = None
        for priority in range(len(level) - 1):
            diff = abs(level[priority] - level[priority + 1])
            if not 1 <= diff <= 3:
                # print("diff is safe")
                issafe = False

            if level[priority] < level[priority + 1]:  # Increasing
                if direction == 'decreasing':
                    issafe = False
                direction = 'increasing'
            elif level[priority] > level[priority + 1]:  # Decreasing
                # print(direction)
                if direction == 'increasing':
                    issafe = False
                direction = 'decreasing'

        if len(level) < 2:
            issafe = True

        if issafe:
            # print("level is safe", level)
            safereports += 1
        # else:
            # print("level is NOT safe", level)
    print(safereports)


def check_valid(level):
    direction = None
    for priority in range(len(level) - 1):
        diff = abs(level[priority] - level[priority + 1])
        if not 1 <= diff <= 3:
            return False

        if level[priority] < level[priority + 1]:  # Increasing
            if direction == 'decreasing':
                return False
            direction = 'increasing'
        elif level[priority] > level[priority + 1]:  # Decreasing
            if direction == 'increasing':
                return False
            direction = 'decreasing'
    return True


def is_valid_with_removal(puzzleinput):
    safereports = 0
    levels = puzzleinput.split('\n')
    for level in levels:
        level = [int(x) for x in level.split()]
        already_valid = False
        if check_valid(level):
            safereports += 1
            already_valid = True

        for data in range(len(level)):
            temp_level = level[:data] + level[data + 1:]
            if check_valid(temp_level) and not already_valid:
                safereports += 1
                break
    print(safereports)

def parttwo(puzzleinput):
    is_valid_with_removal(puzzleinput)


def main():
    puzzleinput = open('input.txt', 'r').read()
    partone(puzzleinput)
    parttwo(puzzleinput)


if __name__ == "__main__":
    main()
