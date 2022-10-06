import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 독립일기 웹툰의 모든 화 제목을 가져옴
title = soup.find_all("td", attrs={"class":"title"})
for element in title:
    print("title: ", element.get_text())
    print("link: ", "https://comic.naver.com" + element.a['href'])
