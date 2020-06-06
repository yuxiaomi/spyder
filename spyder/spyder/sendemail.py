import math
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(username,useremail,salt):
    my_sender = '785380424@qq.com'  # 发件人邮箱账号
    my_pass = 'cljtheejunjbbdig'  # 发件人邮箱密码
    # my_user = '578980424@qq.com'  # 收件人邮箱账号，我这边发送给自己
    my_user=useremail
    ret = True
    try:
        # msg = MIMEText('[user]您好！为确保是您本人操作，请在邮件验证码输入框输入下方验证码：[salt]', 'plain', 'utf-8')
        msg = MIMEText('{name}您好！为确保是您本人操作，请在邮件验证码输入框输入下方验证码：{passwd}'.format(name=username,passwd=salt), 'plain', 'utf-8')
        msg['From'] = formataddr(["admin", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["customer", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "搜索引擎管理系统密码重置"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

# ret = mail('yuxiaomi','578980424@qq.com',5678)


string=str(time.time()*7).split('.',1)
salt=string[1]
# print(string)
# print(string[0],string[1])
# print(math.modf(salt)[0],type(salt))

mail('yuxiaomi','578980424@qq.com',salt)
