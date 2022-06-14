from email.utils import formataddr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
msg_from = '276125681@qq.com'  # 发送方邮箱用户名
passwd = 'wybyjenqeruwbigd'  # 填入发送方邮箱的授权码，163和QQ邮箱的第三方是另外的授权密码，而非原邮箱密码

msg_to = ["13917732040@139.com"]  #  接收邮件，其他人的邮箱

# 创建一个带附件的实例
# 内容不要有文字的测试demotest，防止进垃圾箱
# 标准邮件需要三个头部信息： From, To, 和 Subject
message = MIMEMultipart()
message['From'] = Header("发件人", 'utf-8')# 发信人自称名字
#message['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
message['To'] = Header("收件人", 'utf-8')#收件人名字
#设置真实收件人发件人
# message["From"] = formataddr(["小东", msg_from])  # 列表里的对应发件人邮箱昵称、发件人邮箱账号
# message["To"] = formataddr(["小明", msg_to[0]])  # 列表里的对应收件人邮箱昵称、收件人邮箱账号


message['Subject'] = Header('Python SMTP 邮件', 'utf-8')# 邮件标题


 # 邮件正文内容
# 三个参数：第一个为文本内容，第二个为格式 plain 代表文本格式，html 代表网页模式， 第三个 utf-8 设置编码

message.attach(MIMEText('冰石头正在进行邮件发送测试……', 'plain', 'utf-8'))

# mail_msg = """
# <p>HTML邮件测试</p>
# <table>
# <thead>
#   <tr>
#     <th>序号</th>
#     <th>姓名</th>
#     <th>爱好</th>
#   </tr>
#   </thead>

#   <tbody>
#   <tr>
#     <td>1</td>
#     <td>小明</td>
#     <td>打球</td>
#   </tr>
#   <tr>
#     <td>2</td>
#     <td>小红</td>
#     <td>发豪</td>
#   </tr>
#   </tbody>
# </table>
# """
# message.attach(MIMEText(mail_msg, 'html', 'utf-8')) #如果要发送html需要将plain改成html




#  # 构造附件1，传送当前目录下的 test.txt 文件
# att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
#  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字，已测试
# att1["Content-Disposition"] = 'attachment; filename="demo.txt"'
# message.attach(att1)


# 构造附件2，传送当前目录下的 mypicture.png 图片
# att2 = MIMEText(open('mypicture.png', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="mypicture.png"'
# message.attach(att2)


try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # qq邮箱的smtp地址及端口号
    smtpObj.login(msg_from, passwd)
    smtpObj.sendmail(msg_from, msg_to, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

