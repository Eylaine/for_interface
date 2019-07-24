# coding=utf-8
# Time   : 2019/6/19 15:00
# Author : zhonglin.zhang
# File   : notice.py.py

from datetime import datetime

from utils import get_ini_value
from utils.jenkins import Jenkins
from utils.mail import Mail


if __name__ == '__main__':
    now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    mail_info = dict()
    mail_info['subject'] = '接口自动化测试报告' + now
    mail_info['to'] = get_ini_value('EMAIL', 'to')
    mail_info['from'] = get_ini_value('EMAIL', 'from')
    mail_info['cc'] = get_ini_value('EMAIL', 'cc')
    mail_info['result'] = Jenkins().get_result_info()
    ml = Mail(mail_info)
    ml.send_html_email()
