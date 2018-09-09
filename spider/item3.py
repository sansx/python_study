import requests
import re
import codecs
import json
from functools import reduce
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


url = 'http://weather.sina.com.cn/wenzhou'
r = requests.get(url, stream=True)
d = bytes.decode(r.content)


getall = "\<div class=\"blk_fc_c0_i\" \>[\s\S]*?\<\/div\>"
getdate = "[\s\S]*?wt_fc_c0_i_date\"\>(\d{2}-\d{2})"
getday = "[\s\S]*?wt_fc_c0_i_day .*\>(.*)\<"
getweather = "[\s\S]*?icons0_wt png24.{50,100} title=\"(.{2,4})\"\>"
gettemp = "[\s\S]*?wt_fc_c0_i_temp\"\>(.{5,15})\<"

d = re.findall(getall,d)
print(len(d))
with codecs.open("./weather.json",'w','utf-8') as f:
    allweather = {}
    for index,line in enumerate(d):
        all = getdate + getday + gettemp
        m = re.search(all,line)
        aw = re.findall(getweather,line)
        weather = {}
        if m != None:
            aa = reduce(lambda x,y: x + " " + y, aw)
            weather['date'] = m.group(1)
            weather['day'] = m.group(2)
            weather['weather'] = aa
            weather['temp'] = m.group(3)
            
        allweather[str(index)] = weather
            
        
    f.write(json.dumps(allweather))

#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '646924078@qq.com'
#pwd为qq邮箱的授权码
pwd = 'iitgwnbwynbhbfjd' ## xh**********bdc
#发件人的邮箱
sender_qq_mail = '646924078@qq.com'
#收件人邮箱
receiver = '646924078@qq.com'

#邮件的正文内容
# mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
allstr = ""
print(type(allweather))
for i in allweather:
    tostr = ""
    for b in allweather[i]:
        tostr += allweather[i][b]+" "
    allstr += tostr + "\n"

mail_content = allstr
#邮件标题
mail_title = 'Maxsu的邮件'

#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()



paswd = "iitgwnbwynbhbfjd"
