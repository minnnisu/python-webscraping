from cgitb import text
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"}) #조건에 만족하는 모든 요소를 가져옴, 리스트 반환
for cartoon in cartoons:
    print(cartoon.get_text())