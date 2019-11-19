#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

my_income = sys.argv[1]

# check the entery is a normal salary.

def check_input(arg1):
    if isinstance(int(arg1), int):
        return int(arg1)
    else:
        raise Exception('The input is not an int!')

def calu_tax(salary):
    excess = salary - 5000
    if excess <= 0:
        print('{:.2f}'.format(0))
    elif excess > 0 and excess <= 3000:
        print('{:.2f}'.format(excess * 0.03 - 0))
    elif excess > 3000 and excess <= 12000:
        print('{:.2f}'.format(excess * 0.1 - 210))
    elif excess > 12000 and excess <= 25000:
        print('{:.2f}'.format(excess * 0.2 - 1410))
    elif excess > 25000 and excess <= 35000:
        print('{:.2f}'.format(excess * 0.25 -2660))
    elif excess > 35000 and excess <= 55000:
        print('{:.2f}'.format(excess * 0.30 - 4410))
    elif excess > 55000 and excess <= 80000:
        print('{:.2f}'.format(excess * 0.35 - 7160))
    else:
        print('{:.2f}'.format(excess * 0.45 - 15160))

try:
    my_income_num = check_input(my_income)
    print(calu_tax(my_income_num))
except:
    print("Unexpected error:", sys.exc_info()[0])

