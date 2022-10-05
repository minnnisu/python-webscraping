import requests #http 통신을 하기위한 외부 라이브러리
res = requests.get("http://google.com")
print("응답코드 :", res.status_code) 
# 200코드 -> 정상, 웹사이트 접근 가능
# 403코드 -> 웹사이트 접근 불가능

# if res.status_code == requests.codes.ok: #응답코드가 200일 경우
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
    
res.raise_for_status() #접근이 불가능할 경우 오류를 반환, 위의 if문과 비슷한 역활을 수행
# print(res.text) #페이지 내 html 데이터를 가져옴

with open("mygoogle.html", "w", encoding="utf8") as f: 
    f.write(res.text) #불러온 html정보를 파일로 저장

