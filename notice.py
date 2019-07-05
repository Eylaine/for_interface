# coding=utf-8
# Time   : 2019/6/19 15:00
# Author : zhonglin.zhang
# File   : notice.py.py

from datetime import datetime

from utils.fileutils import IniFile
from utils.jenkins import Jenkins
from utils.mail import Mail


if __name__ == '__main__':
    # mail_infoo = {"to":"zhangzhonglin@aikucun.com","cc":"","subject":"接口自动化测试报告",
    #               "result":{"start_time":"aaaa","duration":"100","total_num":"12","pass_rate":"90",
    #                         "report_url":"http://host:port/job/api.auto/50/allure/"}}
    now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    mail_infoo = dict()
    mail_infoo['subject'] = '接口自动化测试报告' + now
    mail_infoo['to'] = IniFile().get_value('EMAIL', 'to')
    mail_infoo['from'] = IniFile().get_value('EMAIL', 'from')
    mail_infoo['cc'] = IniFile().get_value('EMAIL', 'cc')
    mail_infoo['result'] = Jenkins().get_result_info()
    ml = Mail(mail_infoo)
    ml.send_html_email()
