# 기본적으로 서버의 과부하, 정보 보호 목적 등으로 requests를 통해 접근이 불가능하게 만들어진 사이트들이 있음
# 이는 pc 또는 모바일과 같은 환경으로 접근한 것이 아니기 때문에 발생한 오류암
# user agent를 이용하여 해결이 가능

import requests #http 통신을 하기위한 외부 라이브러리
url = "http://nadocoding.tistory.com"
# 현재 pc환경의 user-agent를 헤더파일로 줌
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
res = requests.get(url, headers=headers)
res.raise_for_status() #접근이 불가능할 경우 오류를 반환, 위의 if문과 비슷한 역활을 수행

with open("nadocoding.html", "w", encoding="utf8") as f: 
    f.write(res.text) #불러온 html정보를 파일로 저장
