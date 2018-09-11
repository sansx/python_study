import requests
import re
import codecs
import json
from functools import reduce
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import datetime
from time import sleep

def get_sina_weather(tofile=False):
    url = 'http://weather.sina.com.cn/wenzhou'
    r = requests.get(url, stream=True)
    d = bytes.decode(r.content)
    getall = "\<div class=\"blk_fc_c0_i\" \>[\s\S]*?\<\/div\>"
    getdate = "[\s\S]*?wt_fc_c0_i_date\"\>(\d{2}-\d{2})"
    getday = "[\s\S]*?wt_fc_c0_i_day .*\>(.*)\<"
    getweather = "[\s\S]*?icons0_wt png24.{50,100} title=\"(.{2,4})\"\>"
    gettemp = "[\s\S]*?wt_fc_c0_i_temp\"\>(.{5,15})\<"
    d = re.findall(getall,d)
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
    if tofile:
        with codecs.open("./weather.json",'w','utf-8') as f:
            f.write(json.dumps(allweather))
    return allweather
#qq邮箱smtp服务器
# host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
# sender_qq = '646924078@qq.com'
#pwd为qq邮箱的授权码
# pwd = ## xh**********bdc
#发件人的邮箱
# sender_qq_mail = '646924078@qq.com'
#收件人邮箱
# receiver = '646924078@qq.com'
#邮件标题
# mail_title = 'xiath的邮件'
#邮件的正文内容
# mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'

def sendmail(**arg):
    args = {}
    args['host_server'] = 'smtp.qq.com'
    args['sender_qq'] = '646924078@qq.com'
    args['pwd'] = 'tnrxeujhzsombfec'
    args['sender_qq_mail'] = '646924078@qq.com'
    args['receiver'] = '646924078@qq.com'
    args['mail_content'] = "mail test"
    args['mail_title'] = 'xiath的邮件'
    for i in arg:
        args[i] = arg[i]
    # ssl登录
    smtp = SMTP_SSL(args['host_server'])
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(args['host_server'])
    smtp.login(args['sender_qq'], args['pwd'])
    msg = MIMEText(args['mail_content'], "plain", 'utf-8')
    msg["Subject"] = Header(args['mail_title'], 'utf-8')
    msg["From"] = args['sender_qq_mail']
    msg["To"] = args['receiver']
    smtp.sendmail(args['sender_qq_mail'], args['receiver'], msg.as_string())
    smtp.quit()

# 设定发送时间，小时：hour，分钟：min，秒：sec
def get_timer(hour=6,min=0,sec=0):
    theTime = datetime.datetime.now().strftime('%H:%M:%S')
    getToday = datetime.datetime.today()
    toyear = getToday.year
    tomo = getToday.month
    today = getToday.day
    getsec = (datetime.datetime(toyear,tomo,today,hour,min,sec)-datetime.datetime.now()).total_seconds()
    if getsec < 0:
        getsec = (datetime.datetime(toyear,tomo,today,hour,min,sec) + datetime.timedelta(days=1) - datetime.datetime.now()).total_seconds()
    print(int(getsec))
    return int(getsec)


# 此处开始准备发送，可以放入while循环，每日提醒
sleep_time = get_timer(hour=22,min=18,sec=0)
print("Waiting for send mail")
sleep(sleep_time)

allweather = get_sina_weather(tofile=True)

allstr = ""
for i in allweather:
    tostr = ""
    for b in allweather[i]:
        tostr += allweather[i][b]+" "
    allstr += tostr + "\n"


sendmail(mail_content = allstr)

print("Send successfully")
# print(abs(-100))


