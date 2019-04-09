from bs4 import BeautifulSoup
# virtualenv scrapingEnv  创建虚拟环境
# cd scrapingEnv/  移动到环境目录
# source bin/activate  开始运行环境
# deactivate  退出环境
import requests
r = requests.get("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(r.text,features='html.parser')
print(bsObj.h1)