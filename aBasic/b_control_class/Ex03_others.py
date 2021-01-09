msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리



#unpacking : 각 요소를 분해
#   * 각 요소의 수와 변수의 수는 동일하게
c1, c2, c3 = di.values()
print(c1, c2, c3)

# 딕셔너리는 반복문을 이용하여 key와 value 출
for key, value in di.items():
    print(key, ":", value)

alist = [ (1,2), (3,4), (5,6)]

for item in alist:
    print(item)

for (a, b) in alist:
    # alist라는 리스트(집합류)에서 추출한 요소가 (a, b) 형식의 튜플이다
    #그 튜플에서 다시 a, b로 분해해서 각각의 변수에 지정한다.
    print('first+second={}'.format(a+b))

# ------------------------------------
# [2] enumerate ()  //tuple 형식의 index, value 형식으로 추출 열


user_list = ['개발자', '코더', '전문', '분석가']
for value in user_list:
    print(value)

for value in enumerate(user_list):
    print(value)

for idx, value in enumerate(user_list):
    print(idx, value)


# --------------------------
# [3] zip() ****************
days = ['월', '화', '수','목']
doit = ['잠자기', '밥먹기', '공부하기', '놀기']


print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for (a, b) in zip(days, doit):
    print('{}요일에는 {}를 합니다'.format(a, b))