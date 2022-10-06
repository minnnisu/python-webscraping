import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #BeautifulSoup 객체를 생성함
# print(soup.title.get_text()) #title 태그내용을 가져옴
# print(soup.a) #soup 객체에서 처음으로 나타나는 a태그를 가져옴 
# print(soup.a.attrs) # a태그의 속성 정보를 가져옴
# print(soup.a["href"]) #특정 속성을 가져옴

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 매개변수로 받은 값에 해당하는 element 중 첫번째 값을 가져옴
rank1 = soup.find("li", attrs={"class","rank01"})
# print(rank1.a) # rank1 아래의 첫번째 a태그를 가져옴
# rank2 = rank1.next_sibling.next_sibling # 다음 형제요소를 가지고 옴, 원래는 next_sibling을 한번만 해도 되지만 개행이 있어 두 번 실행한 것
# rank3 = rank1.next_sibling.next_sibling 
# rank2 = rank2.previous_sibling.previous_sibling # 이전 형제요소를 가져옴
# print(rank2)
# print(rank1.parent) # 부모 요소를 가졍옴
# rank2 = rank1.find_next_sibling("li") # 특정 element를 가진 첫번째 다음 형제를 가져옴
# print(rank2.get_text())
 # print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="현실퀘스트-50화")
print(webtoon)