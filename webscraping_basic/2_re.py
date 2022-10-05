#주민등록번호
#901212-1234567 -> 앞에 6자리 숫자 + "-" + 뒤에 7자리 패턴을 가지고 있음

#차량번호
#11가 1234 
#112가 1234
# -> 2~3자리 숫자 + 한글 한 글자 + 숫자 4자리 패턴을 가지고 있음

#정규식은 특정 문자 조합을 찾기 위한 패턴이다

import re

# 문제사항
# 4가지 문자 중 물음표를 제외한 3가지문자(ca?e)만을 알고 있는 상태
# 이럴경우 ?에 들어갈 수 있는 모든문자를 탐색해야 함(caae, cabe, cace, ...)

def print_match(m):
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열 반환, 매치가 안 될 경우 오류 발생
        print("m.string: ", m.string) # 입력받은 문자열 반환
        print("m.start(): ", m.start()) # 일치하는 문자의 시작 인덱스
        print("m.end(): ", m.end()) # 일치하는 문자의 끝 인덱스
        print("m.span(): ", m.span()) #일치하는 문자의 시작과 끝 인덱스를 함께 표시
    else:
        print("매치 되지않음")

p = re.compile("ca.e") # 정규식을 인수로 받음, "."은 하나의 문자를 의미
# m = p.match("cafe") # 주어진 문자열이 처음부터 일치하는 패턴이 있는지 확인
# m = p.match("caffe") 
# m = p.match("careless") # 앞부분 care이 일치하기 때문에 매치가 됨
# print_match(m)

# m = p.search("good care") # 주어진 문자열에 일치하는 패턴이 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") # 일치하는 모든 것을 리스트로 반환
print(lst)
 