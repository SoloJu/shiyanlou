#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ = '__main__'
    if len(sys.argv) != 2:
        print('Parameter Error')
        sys.exit()

    try:
        income = int(sys.argv[1])
    except ValueError:
        print('Parameter Error')
        sys.exit()

    value = income - 5000

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
    elif valut <= 80000:
        result = value * 0.35 - 7160))
    else:
        result = value * 0.45 - 15160))

    print(format(result, '.2f'))

