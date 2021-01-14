from pathlib import Path
from datetime import datetime
# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())     #/home/user1

p1 = Path('Ex03_createPath.py')
print(p1.stat())


# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
tm = p1.stat().st_ctime
print(tm)

zt = datetime.fromtimestamp(tm)
print(zt)


# ------------------------------------------------
# 3. 디렉토리 생성
p1 = Path('temp/imsi/test')
p1.mkdir(exist_ok=True, parents=True)

# ------------------------------------------------
# 4. 파일 생성
p = Path('./imsi/a.txt')
f = open(p, 'w', encoding='utf-8')
f.write("하나둘셋 이진강 화이팅!")
f.close()

with open(p, 'a', encoding='utf-8') as f:
    f.write('하나둘셋 송채은 화이팅!')

p = Path('./imsi/c.txt')
p.touch()
# ------------------------------------------------
#  5. 경로 제거

p = Path('temp/imsi/test')
p.rmdir()