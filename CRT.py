aoc_input = open('Day10Input.txt', 'r').read().split('\n')


def part1(input):
    new_cycles = len(input)
    cycles = 1
    register = 1
    first_register_cycle = 20
    second_register_cycle = 60
    third_register_cycle = 100
    fourth_register_cycle = 140
    fifth_register_cycle = 180
    sixth_register_cycle = 220
    signal_strength_list = []
    for command in input:
    #    print(command.split(' '))
        if command == "noop":
            cycles += 1
    #        print("cycles add 1")
        else:
            cycles += 2
            instruction = command.split(' ')
    #        print(instruction[1])
            register += int(instruction[1])
    #        print("cycles add 2")

    #    print(cycles)
        if cycles == 20:
    #        print("Hit 20th loop")
            first_register_cycle = 20*register
            signal_strength_list.append(first_register_cycle)

        if cycles == 60:
    #        print("second time")
            second_register_cycle = 60*register
            signal_strength_list.append(second_register_cycle)

        if cycles == 99:
    #        print("third time")
            third_register_cycle = 100*register
            signal_strength_list.append(third_register_cycle)

        if cycles == 139:
    #        print("fourth time")
            fourth_register_cycle = 140*register
            signal_strength_list.append(fourth_register_cycle)

        if cycles == 179:
    #        print("fifth_time")
            fifth_register_cycle = 180*register
            signal_strength_list.append(fifth_register_cycle)

        if cycles == 219:
    #        print("sixth time")
            sixth_register_cycle = 220*register
            signal_strength_list.append(sixth_register_cycle)


    #print(first_register_cycle)
    #print(signal_strength_list)
    print(sum(signal_strength_list))
    #print(register)
    #print(cycles)


part1(aoc_input)
