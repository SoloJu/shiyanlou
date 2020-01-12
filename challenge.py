#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
import datetime


def combine():
    wb = load_workbook('courses.xlsx')
    ws_name = wb.sheetnames
    sheet_1 = wb[ws_name[0]]
    sheet_2 = wb[ws_name[1]]
    sheet_3 = wb.create_sheet(title='combine')
    row_list = []
    for x in range(len(sheet_1['B'])):
        for y in range(len(sheet_2['B'])):
            if sheet_1['B'][x].value == sheet_2['B'][y].value:
                row_list = [sheet_1['A'][x].value, sheet_1['B'][x].value,
                            sheet_1['C'][x].value, sheet_2['C'][x].value]
                sheet_3.append(row_list)
    wb.save('courses.xlsx')


if __name__ == '__main__':
    combine()
