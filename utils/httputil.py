# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : httputil.py

import requests
import json

URL = "https://api.github.com"
headers = {"Authorization": "token 8dd125eefeb55c67163ad20eb19568669f340b3d"}
request_session = requests.Session()


def get(url, **kwargs):
    return request_session.get(url=URL + url, headers=headers, **kwargs)


def post(url, **kwargs):
    return request_session.post(url=URL + url, headers=headers, **kwargs)


if __name__ == '__main__':
    res = get(URL)
    print(json.loads(res.content))
