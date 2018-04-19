# !/usr/bin/python
# _*_ coding: utf-8 _*_

# @Time    : 2018/4/18
# @Author  : zhonglin.zhang

from utils.fileutil import read_json
from utils.httputil import get, post
import json

if __name__ == '__main__':
    data = read_json("testcase.json")

    for each in data:
        path = each["path"]
        method = each["method"]
        params = each["params"]
        data = each["data"]
        response = each["response"]

        if method is "GET":
            resp = get(path=path, params=params)
            code = resp.status_code
            data = json.dumps(resp.content)

        if method is "POST":
            resp = post(path=path, data=data)
            code = resp.status_code
            data = json.dumps(resp.content)
