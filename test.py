# coding: utf-8
import requests
import time
from bs4 import BeautifulSoup

def urlcall(url):
    # アクセスするURL
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    # タイトル要素を取得する class="sti-ttl-item__name"
    all_result = soup.find_all('div', class_="sti-ttl-item__name")

    res_arr = []
    for res in all_result:
        res_arr.append(res.string.strip())

    return res_arr

# list = ['a', 'k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w']
list = ['a', 'k']

output_arr = []
for li in list:
    url = "https://XXX" + li
    output_arr.extend(urlcall(url))
    time.sleep(2)

for val in output_arr:
    print(val)
