#coding=utf-8

#发送邮件：带附件和正文

import smtplib

from email.mime.text import MIMEText

#from email.header import Header

from email.mime.multipart import MIMEMultipart
from Outputs.zip_file import zip_file_path

import os,time

sender = 'gw679977@163.com' #发送邮箱

# _recer = ["wuwanhua@loonxi.com","liutongbin@loon.com","huanghexiang@loonxi.com","gaowei@loonxi.com","houshihang@loonxi.com","lifei@loonxi.com"] #接收邮箱
_recer = ["gaowei@loonxi.com"]
smtpserver = 'smtp.163.com' #发送邮箱服务器

pswd ='IILUQXWOHHPEHHXH' #开启stmp的授权码

msg = MIMEMultipart() #创建一个带附件的实例

theme_time = time.strftime("%Y-%m-%d-%H_%M", time.localtime(time.time()))

msg['Subject'] = '{}测试报告'.format(theme_time)#发送邮件主题

msg['From'] = sender

msg["To"] = ",".join(_recer)

msg.attach(MIMEText('通过定时任务发送测试报告......','plain','utf-8'))#邮件正文内容

#生成压缩包
file_name = '测试报告{}.zip'.format(theme_time)
zip_file_path(r"./html", 'E:/onloon/Outputs/TestReportzip', file_name)
print(file_name)

#构造附件att，传送目录下的text.txt文件

#单附件发送


att = MIMEText(open('./TestReportzip/{}'.format(file_name) ,'rb').read(), 'base64', 'utf-8')  #.format(file_name)

att['Content-Type'] = 'application/octet-stream'

att['Content-Disposition'] = 'attachment;filename="'+file_name+'"'
att.add_header('Content-Disposition',)

msg.attach(att)

'''

#多附件发送

#files = ['text.txt','text - 副本.txt']

#path = 'D:'

files = ['2.jpg','个人-娱乐爱好-电脑桌面.rar']

path = 'D:\\04-个人备份\\个人-娱乐爱好-电脑桌面'

for f in files:

    if os.path.isfile(path+'\\'+f):

        att = MIMEText(open(path+'\\'+f,'rb').read(),'base64','utf-8')

        att['Content-Type'] = 'application/octet-stream'

        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", f))

    msg.attach(att)
'''

try:
#====================登录smtp服务器======================


    stmp = smtplib.SMTP()

    stmp.connect(smtpserver)

    stmp.login(sender,pswd) #使用授权码登录

    stmp.sendmail(sender,_recer,msg.as_string()) #发送邮件

    stmp.quit()

    print('send success')

except smtplib.SMTPException:
    print("Error:无法发送邮件")

#smtplib.SMTPException:
# print("Error:无法发送邮件")