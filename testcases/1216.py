# coding = utf-8
# Author: Shenbq
# Date: 2021/12/16 12:05
import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1124253529@qq.com"  # 用户名
mail_pass = "Sqn66881997101"  # 口令
sender = '1124253529@qq.com'
receivers = ['1124253529@qq.com']

message = MIMEText('Python邮件发送测试。。。', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("ERROR:无法发送邮件")
