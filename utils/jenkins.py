# coding=utf-8
# Time   : 2019/6/17 16:10
# Author : zhonglin.zhang
# File   : jenkins.py

import re
from datetime import datetime

from utils.httputil import *


class Jenkins:

    def __init__(self):
        self.base_url = 'http://host:port/job/api.auto/'
        self.build_num, self.report_url = self.set_build_info()
        self.duration = ''
        self.total_num = 0
        self.pass_rate = 0.0
        self.set_console_info()

    def set_build_info(self):
        url = self.base_url + 'api/json?pretty=true'
        response = get(url).json()
        build_num = response['lastBuild']['number']
        report_url = response['lastBuild']['url'] + 'allure'
        return build_num, report_url

    def set_console_info(self):
        url = self.base_url + str(self.build_num) + '/consoleText'
        response = get(url).text
        pattern = r'in ([\.\d]*) seconds'
        match_result = re.findall(pattern, response)
        self.duration = match_result[0]

        pattern_pass = r'(\d) passed'
        pass_num = re.findall(pattern_pass, response)[0]

        pattern_fail = r'(\d) failed'
        fail_result = re.findall(pattern_fail, response)

        if fail_result:
            fail_num = fail_result[0]
        else:
            fail_num = '0'

        self.total_num = int(pass_num) + int(fail_num)
        # 通过率保留两位小数
        self.pass_rate = float('%.2f' % (100 * int(pass_num) / self.total_num))

    def get_result_info(self):
        result = dict()
        result['start_time'] = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        result['duration'] = self.duration + 's'
        result['report_url'] = self.report_url
        result['total_num'] = self.total_num
        result['pass_rate'] = str(self.pass_rate) + '%'

        return result


if __name__ == '__main__':
    jenkins = Jenkins()
    print(jenkins.get_result_info())
