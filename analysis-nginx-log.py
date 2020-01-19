#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime
from collections import Counter


def open_parser(filename):
    with open(filename) as logfile:
        # 使用正则表达式解析日志文件
        pattern = (
            r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
            r'\[(.+)\]\s'  # 时间
            r'"GET\s(.+)\s\w+/.+"\s'  # 请求路径
            r'(\d+)\s'  # 状态码
            r'(\d+)\s'  # 数据大小
            r'"(.+)"\s'  # 请求头
            r'"(.+)"'  # 客户端信息
        )
        parsers = re.findall(pattern, logfile.read())
    return parsers  # 这里返回的是一个列表，每个元素是元组，每个元组是上述正则表达中所匹配到的字符串组成。例如：
    '''
    原来的一条log记录是：216.244.66.231 - - [09/Jan/2017:06:34:01 +0800] "GET /robots.txt HTTP/1.1" 502 181 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)"
    匹配到的就是：[('216.244.66.231', '09/Jan/2017:06:34:01 +0800', '/robots.txt', '502', '181', '-', 'Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)'), ()]
    每个字符串是上述正则表达中括号分组中的匹配内容。
    '''


def logs_count():
    logs = open_parser('nginx.log')

    # 存放统计后的 IP 和请求地址
    ip_list = []
    request404_list = []

    # 统计题目要求的信息
    for log in logs:
        # 转换原时间格式
        dt = datetime.strptime(log[1][:-6], "%d/%b/%Y:%H:%M:%S")
        # 获取 11 日当天的数据，返回满足条件的 IP 地址
        if int(dt.strftime("%d")) == 11:
            ip_list.append(log[0])
        # 获取状态码为 404 的数据，返回满足条件的请求地址
        if int(log[3]) == 404:
            request404_list.append(log[2])
    return ip_list, request404_list


def main():
    ip_list, request404_list = logs_count()
    ip_counts = Counter(ip_list)
    request404_counts = Counter(request404_list)

    # 将字典按 Values 排序
    sorted_ip = sorted(ip_counts.items(), key=lambda x: x[1])
    sorted_request404 = sorted(request404_counts.items(), key=lambda x: x[1])

    # 排序后的最后一项 Values 最大, 并处理成字典返回
    ip_dict = dict([sorted_ip[-1]])
    url_dict = dict([sorted_request404[-1]])

    print(ip_dict, url_dict)


if __name__ == '__main__':
    main()
