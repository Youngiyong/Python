"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
p = Path(r"..")
print(p)
print(p.resolve())   # .을찍었을때 실제 경로를 보여준다.
print("1--------------------")

test = []
for x in p.iterdir():  #
    if x.is_dir():  #디렉토리인경우만 실행
        test.append(x)
print(test)

# [복습] list comprehence
test1 = [x for x in p.iterdir() if x.is_dir()]
print(test1)

print("2--------------------") # 조건을줘서 필요한 것만 가져오고싶다.
p = Path('.')  # 현재디렉토리
subs = list(p.glob('../a_datatype_class/*.txt'))   # .txt 파일만
print(subs)     # 윈도우 패쓰 객체로 담겨져있음.
print(type(subs[0]))   # 윈도우 패쓰 객체인거 확인.




