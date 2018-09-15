# coding=utf8
__author__ = ''
__date__ = 2018 / 5 / 5

import requests
from bs4 import BeautifulSoup


def getPicture():
    result = open("东坝.txt", "w")
    links = []
    proxie = {
        'https': 'http://101.81.141.1:9999'
    }
    for pageindex in range(0, 1500, 15):
        url = "http://www.douban.com/group/beijingzufang/discussion"
        Page = {'start': pageindex}
        wbdata = requests.get(url, params=Page, proxies=proxie).text
        soup = BeautifulSoup(wbdata, 'html.parser')
        subject_titles = soup.select("td.title > a")
        tag1 = u"东坝"
        tag2 = u"独卫"
        for n in subject_titles:
            title = n.get("title")
            link = n.get("href")
            if tag1 in title and tag2 in title and link not in links:
                result.write(link + "\n")
                links.append(link)
    result.close()


getPicture()
