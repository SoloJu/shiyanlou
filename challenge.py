#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from openpyxl import Workbook
import datetime

def combine():
    wb = load_workbook('courses.xlsx')
    ws = wb['time']
    time_t = tuple(ws.rows)
    print(len(time_t))

if __name__ == '__main__':
    combine()

