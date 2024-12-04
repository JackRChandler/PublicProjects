import re

aoc_input = open('Day11InputExample.txt').read()
#aoc_input = open('Day11Input.txt').read()


def parse(initial_monkeys):
    all_monkeys = []
    for monkey in initial_monkeys.split('\n\n'):
#        print(monkey, "\n")
        items = monkey.split('\n')
#        print(items)
        monkey_name = items[0]
        monkey_name_int = int(monkey_name.strip(':').split(' ')[1])
        starting_items = items[1]
        starting_items_list = starting_items.strip('Starting items:').split(',')
        worry_level = items[2]
        worry_level_todo = worry_level.replace('Operation: new =', '').split()
        monkey_test = items[3]
        monkey_test_todo = re.findall(r'\d+', monkey_test)  # monkey_test[len(monkey_test) - 1]
        monkey_test_todo_int = int(monkey_test_todo[0])
        iftrue_test = items[4]
        iftrue_throw_to = iftrue_test[len(iftrue_test) - 1]
        iffalse_test = items[5]
        iffalse_throw_to = iffalse_test[len(iftrue_test)]


        totals_monkeys = [monkey_name_int, starting_items_list, worry_level_todo, monkey_test_todo_int, iftrue_throw_to,
              iffalse_throw_to]
        all_monkeys.append(totals_monkeys)

    return all_monkeys


def part1(input_aoc):


    monkey0_items = parse(input_aoc)[0][1]
    monkey1_items = parse(input_aoc)[1][1]
    monkey2_items = parse(input_aoc)[2][1]
    print(monkey0_items, monkey1_items, monkey2_items)
    cycle = 0
    while cycle < 20:
        if cycle == 0:
            new_monkeys = parse(input_aoc)
        else:
            new_monkeys = []

#        print(new_monkeys)
        for monkey in new_monkeys:
            for starting_item in monkey[1]:
                print(monkey[2])
                op = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y}
                replace_old = [w.replace('old', starting_item) for w in monkey[2]]
                int1 = int(replace_old[0])
                int2 = int(replace_old[2])
                print(op[replace_old[1]](int1, int2))
                worry_before_divide = op[replace_old[1]](int1, int2)
                worry_after_divide = worry_before_divide//3
                print(worry_after_divide)
                if worry_after_divide % int(monkey[3]) == 0:
                    print("is divisible")
                    
                else:
                    print("Is not divisible")

#        new_monkeys.append(totals_monkeys)
        cycle += 1
#        print(new_monkeys)


part1(aoc_input)
