#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 5000

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 15160),
    IncomeTaxQuickLookupItem(55000, 0.35, 7160),
    IncomeTaxQuickLookupItem(35000, 0.30, 4410),
    IncomeTaxQuickLookupItem(25000, 0.25, 2660),
    IncomeTaxQuickLookupItem(12000, 0.2, 1410),
    IncomeTaxQuickLookupItem(3000, 0.1, 210),
    IncomeTaxQuickLookupItem(0.00, 0.03, 0)
]

SOCIAL_INSURANCE_MONEY_RATE = {}

def load_social_insurance_rate(file):
    with open(file, 'r') as temp_file:
        SOCIAL_INSURANCE_MONEY_RATE = dict(csv.reader(temp_file))

def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)
    return '0.00', '{:.2f}'.format(real_income)
    # 函数可以返回两个数值

def main():
    for item in sys.argv[1:]:
        employee_id, income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Paramenter Error')
            continue

        _, remain = calc_income_tax_and_remain(income)
        # 此处的_, 是接收传出来的第一个结果，但是这个值没有用，以后也不会用到，所以就给_
        print('{}:{}'.format(employee_id, remain))


if __name__ == '__main__':
    main()