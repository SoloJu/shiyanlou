#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import re


def repl(filename):

    with open(filename, encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    imgs = soup.find_all('img')

    for i in range(len(imgs)):
        if imgs[i]['src'].find('https://docs.tapdata.io') != -1:
            imgs[i]['src'] = imgs[i]['src'].replace(
                'https://docs.tapdata.io', 'http://doc.tapdata.io')

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


def show():
    dir_list = os.listdir('.')
    for i in range(len(dir_list)):
        m = re.match('.*-cn\.html$', dir_list[i])
        n = re.match('.*\.html$', dir_list[i])
        if (not m) and n:
            repl(dir_list[i])


if __name__ == '__main__':
    show()
