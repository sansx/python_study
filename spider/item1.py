import http.client as http
import pickle
import re


conn = http.HTTPConnection("www.cnblogs.com")
conn.request("GET","/vamei")
res = conn.getresponse()

print(res)

content = res.read()
print(type(content))
content =  bytes.decode(content).split("\r\n")

# with open("./text.txt","wb") as f:
#     pickle.dump(content,f)


pattern = "posted @ (\d{4}-\d{2}-\d{2} [0-2]\d:[0-6]\d) Vamei 阅读\((\d+)\) 评论"
for line in content:
    m = re.search(pattern, line)
    if m != None:
        print(m.group(1),m.group(2))