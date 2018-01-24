# coding:utf-8


import requests
from bs4 import BeautifulSoup
import urllib.request
import re

# 指定入口url
url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
count = 0
count1 = 0
while True:
    if count1 > 3:
        break
    try:
        html = urllib.request.urlopen(url, timeout=10).read()
        s = BeautifulSoup(html, "html.parser")
        h1 = s.find('h1').get_text()
        h2 = s.find('h2').get_text()
        print(h1, h2)

        # 获取新url
        new_url = list(set([]))
        texts = s.find_all('div', attrs={"class": "para"})
        links = s.find_all('a', href=re.compile(r'/item/'))
        for test in texts:
            for link in links:
                link = str(link.get('href'))
                href = urllib.request.urljoin("https://baike.baidu.com/item/PyGame", link)
                new_url.append(href)
        new = new_url[15:20]

    # 从新url中提取url分析并放进旧url
        old_url = []  # 用来获取new_url[]中的元素
        url = new[count]
        print(url)
        old_url.append(url)
        del new[count]
        print(count)
        count += 1

    except Exception as e:
        print(e)
        break
    count1 += 1
    print(count1)



