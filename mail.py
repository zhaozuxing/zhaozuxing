# -*- coding:gbk -*-

import smtplib
from email.mime.text import MIMEText



def mail(mail_text, mail_to):
    # set the mail context
    msg = MIMEText(mail_text)

    # set the mail info
    msg['Subject'] = "每日健康打卡通知"
    msg['From'] = '544041725@qq.com'
    msg['To'] = '544041725@qq.com'

    # send the mail
    send = smtplib.SMTP_SSL("smtp.qq.com", 465)
    send.login('544041725', 'hbpzfftvadaibbfi')
    send.send_message(msg)
    # quit QQ EMail
    send.quit()
