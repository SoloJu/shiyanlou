#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime

# set dict for ip
ip_dict = {}
url_dict = {}
# set re pattern for request, ip, url
request_p = re.compile('GET')
ip_p = re.compile(
    '[1-9]{1}\d{0,2}\.[1-9]{1}\d{0,2}\.[1-9]{1}\d{0,2}\.[1-9]{1}\d{0,2}')
url_p = re.compile('\"GET .* HTTP\/1\.1\"')
dt_p = re.compile('\[\d{1}.*\d{1}\]')
response_p = re.compile('HTTP\/1\.1\" \d{3}')
# open log file
with open('nginx.log', 'r', encoding='utf-8') as log_file:
    # file can be listed for each line
    for line in log_file:
        match_request = request_p.search(line)
        if match_request is not None and match_request.group() == 'GET':
            match_dt = dt_p.search(line)
            if match_dt is not None and datetime.strptime(match_dt.group().strip('[,]'), '%d/%b/%Y:%H:%M:%S %z').date() == datetime(2017, 1, 11).date():
                match_ip = ip_p.search(line)
                if match_ip.group() not in ip_dict:
                    ip_dict[match_ip.group()] = 1
                else:
                    ip_dict[match_ip.group()] += 1
            else:
                continue
            match_response = response_p.search(line)
            if match_response is not None and match_response.group().split()[1] == '404':
                match_url = url_p.search(line)
                if match_url.group().split()[1] not in url_dict:
                    url_dict[match_url.group().split()[1]] = 1
                else:
                    url_dict[match_url.group().split()[1]] += 1
            else:
                continue
        else:
            continue

largest_ip = max(ip_dict, key=ip_dict.get)
print(largest_ip, ip_dict.get(largest_ip))
largest_url = max(url_dict, key=url_dict.get)
print(largest_url, url_dict.get(largest_url))
