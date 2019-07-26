# coding=utf-8
# Time   : 2019/6/17 16:11
# Author : zhonglin.zhang
# File   : mail.py

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

from utils import get_ini_value
from settins import ROOT_PATH


class Mail:

    def __init__(self, mail_info):
        self.mail_info = mail_info
        self.username = get_ini_value('EMAIL', 'from')
        self.password = get_ini_value('EMAIL', 'password')
        self.server = self.get_server()
        self.message = self.get_content(self.mail_info['result'])
        self.server.login(self.username, self.password)

    def send_html_email(self):
        """email_info: {to_list: [], cc_list: [], result: {}, # info: [{}, {}]}"""
        msg = MIMEMultipart('related')
        msg['From'] = self.username
        msg['To'] = self.mail_info['to']
        msg['Cc'] = self.mail_info['cc']
        msg['Subject'] = self.mail_info['subject']
        msg.attach(self.get_icon())
        content = MIMEText(self.message, _subtype='html', _charset='utf-8')
        msg.attach(content)

        self.server.sendmail(self.username, self.mail_info['to'].split(";") +
                             self.mail_info['cc'].split(';'), msg=msg.as_string())

    def get_server(self):
        temp_server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        temp_server.login(self.username, self.password)

        return temp_server

    def get_content(self, result):
        env = Environment(loader=FileSystemLoader(ROOT_PATH + '/data'))
        template = env.get_template('template.html')
        content = template.render(result=result)
        return content

    def get_icon(self):
        # with open(ROOTPATH + '/data/100x50.png', 'rb') as img:
        #     img_data = img.read()

        ff = open(ROOT_PATH + '/data/100x50.png', 'rb')
        img = MIMEImage(ff.read())
        ff.close()
        img.add_header('Content-ID', 'icon')

        return img


class Report:

    def __init__(self):
        pass
