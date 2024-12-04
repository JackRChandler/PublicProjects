from collections import deque
import re

aoc_input = open('Day10Input.txt', 'r').read().split('\n')

def part1(input):
    new_cycles = len(input)
    cycles = 1
    register = 1
    # first_register_cycle = 20
    # second_register_cycle = 60
    # third_register_cycle = 100
    # fourth_register_cycle = 140
    # fifth_register_cycle = 180
    # sixth_register_cycle = 220
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


def part1_rewrite1(input):

    pixel_draw = "#"
    cycles = 1
    register = 1
    signal_strength_list = []
    for command in input:
        if command == "noop":
            cycles += 1
            if register < cycles or register > cycles + 3:
                if cycles <= 40:
                    pixel_draw = ''.join((pixel_draw, '.'))
            else:
                if cycles <= 40:
                    pixel_draw = ''.join((pixel_draw, '#'))
            if cycles == 20:
                print("Hit 20th loop")
                first_register_cycle = 20 * register
                signal_strength_list.append(first_register_cycle)

            if cycles == 60:
                print("second time")
                second_register_cycle = 60 * register
                signal_strength_list.append(second_register_cycle)

            if cycles == 100:
                print("third time")
                third_register_cycle = 100 * register
                signal_strength_list.append(third_register_cycle)

            if cycles == 140:
                print("fourth time")
                fourth_register_cycle = 140 * register
                signal_strength_list.append(fourth_register_cycle)

            if cycles == 180:
                print("fifth_time")
                fifth_register_cycle = 180 * register
                signal_strength_list.append(fifth_register_cycle)

            if cycles == 220:
                print("sixth time")
                sixth_register_cycle = 220 * register
                signal_strength_list.append(sixth_register_cycle)
        #        print("cycles add 1")
        else:
            instruction = command.split(' ')
#            register += int(instruction[1])
            for slice in command.split(' '):
                cycles += 1
                if register < cycles or register > cycles + 3:
                    if cycles <= 40:
                        pixel_draw = ''.join((pixel_draw, '.'))
                else:
                    if cycles <= 40:
                        pixel_draw = ''.join((pixel_draw, '#'))

                if slice.lstrip('-').isdigit():
                    register += int(slice)
 #                   print(slice)
                if cycles == 20:
                    print("Hit 20th loop in else")
                    first_register_cycle = 20 * register
                    signal_strength_list.append(first_register_cycle)

                if cycles == 60:
                    print("second time in else")
                    second_register_cycle = 60 * register
                    signal_strength_list.append(second_register_cycle)

                if cycles == 100:
                    print("third time in else")
                    third_register_cycle = 100 * register
                    signal_strength_list.append(third_register_cycle)

                if cycles == 140:
                    print("fourth time in else")
                    fourth_register_cycle = 140 * register
                    signal_strength_list.append(fourth_register_cycle)

                if cycles == 180:
                    print("fifth_time in else")
                    fifth_register_cycle = 180 * register
                    signal_strength_list.append(fifth_register_cycle)

                if cycles == 220:
                    print("sixth time in else")
                    sixth_register_cycle = 220 * register
                    signal_strength_list.append(sixth_register_cycle)

    print(pixel_draw)
    print(sum(signal_strength_list))


def cycles_check(cycles, register):
    register_cycle_outcome = 0
    if cycles == 20:
        print("Hit 20th loop in else")
        register_cycle_outcome = 20 * register

    if cycles == 60:
        print("second time in else")
        register_cycle_outcome = 60 * register

    if cycles == 100:
        print("third time in else")
        register_cycle_outcome = 100 * register

    if cycles == 140:
        print("fourth time in else")
        register_cycle_outcome = 140 * register

    if cycles == 180:
        print("fifth_time in else")
        register_cycle_outcome = 180 * register

    if cycles == 220:
        print("sixth time in else")
        register_cycle_outcome = 220 * register

    return register_cycle_outcome


def part1_rewrite2():

    input = open('Day10InputExample.txt').read()
    instructions = re.split(r'\n| ', input)
    cycles = 1
    register = 1
    signal_strength_list = []
    signal_line = ''
    for command in instructions:
        print("Cycle is:", cycles)

        if command == 'noop':
            print("In noop")
            cycles += 1
            signal_strength_list.append(cycles_check(cycles, register))
            if register >= cycles + 3 or register < cycles:
                print("Register is ifstatement:", register)
                if cycles < 40:
                    signal_line += '.'
                    print(signal_line)
            else:
                print("Register iselsestatement:", register)
                if cycles < 40:
                    signal_line += '#'
                    print(signal_line)
        elif command == 'addx':
            print("In addx")
            cycles += 1
            signal_strength_list.append(cycles_check(cycles, register))
            if register >= cycles + 3 or register < cycles:
                print("Register is ifstatement:", register)
                if cycles < 40:
                    signal_line += '.'
                    print(signal_line)
            else:
                print("Register iselsestatement:", register)
                if cycles < 40:
                    signal_line += '#'
                    print(signal_line)
        elif command.lstrip('-').isdigit():
            print("In digit portion")
#            print(command)
            cycles += 1
            signal_strength_list.append(cycles_check(cycles, register))
            if register > (cycles + 3) or register < cycles:
                print("Register is ifstatement:", register)
                if cycles < 40:
                    signal_line += '.'
                    print(signal_line)
            else:
                print("Register iselsestatement:", register)
                if cycles < 40:
                    signal_line += '#'
                    print(signal_line)

            register += int(command)





    print(signal_line)
    print(sum(signal_strength_list))
    print(cycles)
    print(register)

#    while(cycle := cycle +1) < 1000 and ( signals or timer ):

#part1(aoc_input)

#part1_rewrite1(aoc_input)

part1_rewrite2()
