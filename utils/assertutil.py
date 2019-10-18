# coding=utf-8
# Time   : 2019/7/9 11:10
# Author : zhonglin.zhang
# File   : assertutil.py

from jsonpath import jsonpath
from jsonschema import Draft7Validator
import json

from utils.logutil import logger
from settins import ROOT_PATH


class AssertUtil:

    def __init__(self, response):
        self.code = response.status_code
        self.content = response.json()

    def assert_http_200(self):
        if self.code is 200:
            assert True
        else:
            logger.error(self.content)
            assert False

    def assert_json_schema(self, schema_file):
        schema_path = ROOT_PATH + '/data/schema/' + schema_file
        with open(schema_path, 'r') as js:
            json_schema = json.loads(js.read())
        v = Draft7Validator(json_schema)

        flag = True
        for error in v.iter_errors(self.content):
            flag = False
            json_path = "$"
            for each in error.schema_path:
                if isinstance(each, str):
                    json_path = json_path + "." + each
                elif isinstance(each, int):
                    json_path = json_path + "[" + str(each) + "]"
            logger.error("json path: " + json_path)
            logger.error("error info: " + error.message)

        assert flag

    def assert_json_value(self, json_str: dict):
        for key in json_str.keys():
            data = jsonpath(self.content, key)

            if data is False:
                logger.error(u"未获取到json path对应的值：" + key)
                assert False
            assert data == json_str[key]
