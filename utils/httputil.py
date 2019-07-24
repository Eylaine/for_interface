# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : httputil.py

import requests
import json


def get(path, params=None, header=None):
    headers = add_headers(header)
    return requests.get(url=path, params=params, headers=headers)


def post(path, data=None, header=None):
    headers = add_headers(header)
    return requests.post(url=path, data=json.dumps(data), headers=headers)


def put(path, data=None, **kwargs):
    return requests.put(url=path, data=json.dumps(data), **kwargs)


def delete(path, data=None, **kwargs):
    return requests.delete(url=path, data=json.dumps(data), **kwargs)


def add_headers(headers):
    # 默认header
    header = {"Content-Type": "application/json"}
    if headers is None:
        return header
    for each in headers.keys():
        header[each] = headers[each]
    return header
