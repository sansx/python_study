import requests
import re
import codecs
import json

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
        all = getdate + getday + getweather + gettemp
        m = re.search(all,line)
        weather = {}
        if m != None:
            weather['date'] = m.group(1)
            weather['day'] = m.group(2)
            weather['weather'] = m.group(3)
            weather['temp'] = m.group(4)
            print(weather)
        allweather[str(index)] = weather
            
        
    f.write(json.dumps(allweather))


