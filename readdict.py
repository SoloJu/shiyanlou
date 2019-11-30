#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
dict_data = {}
with open(sys.argv[1], 'r') as f:
    dict_data = dict(csv.reader(f))

print(dict_data)