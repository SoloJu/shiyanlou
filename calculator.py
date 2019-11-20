#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def taxed(income):
    value = income - 5000 - income * 0.165

    if value <= 0:
        result = 0
    elif value <= 3000:
        result = value * 0.03 - 0
    elif value <= 12000:
        result = value * 0.1 - 210
    elif value <= 25000:
        reslult = value * 0.2 - 1410
    elif value <= 35000:
        result = value * 0.25 -2660
    elif value <= 55000:
        result = value * 0.30 - 4410
    elif value <= 80000:
        result = value * 0.35 - 7160
    else:
        result = value * 0.45 - 15160
    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Parameter Error')
        sys.exit()

    person_dict = {}
    for items in sys.argv[1:]:
        each_person = items.split(':')
        person_nu = each_person[0]
        try:
            person_income = int(each_person[1])
        except ValueError:
            print('Parameter Error')
            sys.exit()
        person_tax = taxed(person_income)
        person_dict[person_nu] = person_income - person_tax
    print(person_dict)
#    for key, value in person_dict:
#        print('{}:{.2f}'.format(key, value))

