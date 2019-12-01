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
user_data = []
user_salary_list = []

def load_social_insurance_rate(file):
    with open(file, 'r') as temp_file:
        for line in temp_file:
            line_list = line.split(' ')
            SOCIAL_INSURANCE_MONEY_RATE[line_list[0]] = float(line_list[2].strip('\n'))

def load_user_income(file):
    with open(file, 'r') as temp_file:
        #下面要显式声明全局变量，否则无法改变这个全局变量的值。
        global user_data
        user_data = list(csv.reader(temp_file))
        #下面要把收入部分变成整数，否则在calc_income_tax_and_remain()函数中无法数字比较。
        for i in range(len(user_data)):
            user_data[i][1] = int(user_data[i][1])

def write_user_salary(file, data):
    with open(file, 'w') as temp_file:
        csv.writer(temp_file).writerows(data)


def calc_income_tax_and_remain(income):
    if income < SOCIAL_INSURANCE_MONEY_RATE['JiShuL']:
        income_jishu = SOCIAL_INSURANCE_MONEY_RATE['JiShuL']
    elif income > SOCIAL_INSURANCE_MONEY_RATE['JiShuH']:
        income_jishu = SOCIAL_INSURANCE_MONEY_RATE['JiShuH']
    else:
        income_jishu = income
    social_insurance_money = income_jishu * (sum(SOCIAL_INSURANCE_MONEY_RATE.values())-SOCIAL_INSURANCE_MONEY_RATE['JiShuL']-SOCIAL_INSURANCE_MONEY_RATE['JiShuH'])
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(social_insurance_money), '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)
    return '{:.2f}'.format(social_insurance_money), '0.00', '{:.2f}'.format(real_income)

def main():
    exist_c = 0
    exist_d = 0
    exist_o = 0
    for i in range(1, 7, 2):
        if sys.argv[i] == '-c' and exist_c == 0:
            exist_c = i
        elif sys.argv[i] == '-d' and exist_d == 0:
            exist_d = i
        elif sys.argv[i] == '-o' and exist_o == 0:
            exist_o = i
        else:
            print('Parameter Error!')
            exit(-1)
    load_social_insurance_rate(sys.argv[exist_c+1])
    load_user_income(sys.argv[exist_d+1])

    for item in user_data:
        employee_id, income = item
        social_insurance_money, tax, remain = calc_income_tax_and_remain(income)
        each_person = [employee_id, str(income), social_insurance_money, tax, remain]
        #上面要把income变回成字符串，否则写入csv文件出错。
        user_salary_list.append(each_person)

    write_user_salary(sys.argv[exist_o+1], user_salary_list)


if __name__ == '__main__':
    main()