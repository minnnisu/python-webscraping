import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img" ,attrs={"class":"thumb_img"})

for idx,image in enumerate(images):
    img_url = image['src']
    if(img_url.startswith("//")):
        img_url = "http" + img_url
    print(img_url)
    if(idx >= 4):
        break