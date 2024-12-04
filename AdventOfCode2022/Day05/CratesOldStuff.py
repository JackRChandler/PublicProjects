
#from astropy.io import ascii
import astropy.io.ascii
import re
from astropy.table import Table
import numpy as np
#astropy.test()

table = open('InputStacksDay05Example.txt').read().split('\n')

moves = open('InputMovesDay05Example.txt').read().split('\n')

data = astropy.io.ascii.read(table, delimiter='-')

for move in moves:
    amount1 = re.findall(r'((?<=move )\d)', move)
    from1 = re.findall(r'((?<=from )\d)', move)
    to1 = re.findall(r'((?<=to )\d)', move)

    if amount1 == ['1']:
        print("Move 1")
        if from1 == ['1']:
            print("Move from column 1")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
        elif from1 == ['2']:
            print("Move from column 2")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
        elif from1 == ['3']:
            print("Move from column 3")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
    elif amount1 == ['2']:
        print("Move 2")
        if from1 == ['1']:
            print("Move from column 1")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
        elif from1 == ['2']:
            print("Move from column 2")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
        elif from1 == ['3']:
            print("Move from column 3")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
    elif amount1 == ['3']:
        print("Move 3")
        if from1 == ['1']:
            print("Move from column 1")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
        elif from1 == ['2']:
            print("Move from column 2")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")
        elif from1 == ['3']:
            print("Move from column 3")
            if to1 == ['1']:
                print("Move to column 1")
            elif to1 == ['2']:
                print("Move to column 2")
            elif to1 == ['3']:
                print("Move to column 3")

#print(data['2'])

for item in data['3']:
    print(item)

print(data)

# for row in table:
#     print(row)
#
# for move in moves:
#     print(move)
