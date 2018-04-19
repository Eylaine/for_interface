# coding=utf-8
# Time    : 2018/3/13 21:45
# Author  : Eylaine
# File    : fileutil.py

from common import ROOTPATH
import json


def read_json(filename):

    with open(ROOTPATH + "/data/" + filename) as jf:
        data = json.load(jf)

    return data


if __name__ == '__main__':
    case = read_json("testcase.json")
    for each in case:
        print(each)
