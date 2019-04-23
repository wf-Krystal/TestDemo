#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

url = 'http://httpbin.org/get'
r = requests.get(url)

print(r.headers)
print(r.status_code)
print(r.text)

bad_r = requests.request('get', 'http://httpbin.org/status/404')
print(bad_r.status_code)

#bad_r.raise_for_status()

json_r = requests.get('https://api.github.com/events')
print(json_r.json())