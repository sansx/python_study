import requests 

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# url = 'https://api.github.com/events'
s = requests.Session()

headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "hacker-news.firebaseio.com",
    "Upgrade-Insecure-Requests": '1',
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
}
proxies = {"https": "103.242.219.242:8080"}

res = s.get(url, headers=headers, proxies= proxies)
sub_ids = res.json()
sub_dicts = []

for sub_id in sub_ids[:30]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(sub_id) + '.json'
    sub_r = s.get(url, headers=headers, proxies= proxies)
    res_dict = sub_r.json()
    res = {
        'title': res_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(sub_id),
        'comments': res_dict.get('descendants',0)
    }

    sub_dicts.append(res)

sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)

with open("./res.txt",'w') as f:
    for sub_dict in sub_dicts:
        title = "\nTitle:" + sub_dict['title']
        link = "Discussion link:" + sub_dict['link']
        comments = "Comments:" + str(sub_dict['comments'])
        text = title + "\n" + link + "\n" + comments + "\n"
        f.write(text)

# for sub_dict in sub_dicts:
#     print("\nTitle:", sub_dict['title'])
#     print("Discussion link:", sub_dict['link'])
#     print("Comments:", sub_dict['comments'])
