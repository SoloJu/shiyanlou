#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from openpyxl import Workbook
import datetime

def combine():
    wb = load_workbook('courses.xlsx')
    ws_name = wb.sheetnames
    print(ws_name)
    #for i in range(1,count_t+1):


if __name__ == '__main__':
    combine()


		