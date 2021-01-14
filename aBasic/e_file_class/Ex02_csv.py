# Ex02_csv.py

# 1. 리스트의 데이타를 csv로 저장하기
import csv
#
# data = [[1, '김길동', '책임'], [2, '박길동', '연구원'], [3, '최길동', '선임']]
#
# with open('./data/imsi.csv', 'w', encoding='utf-8') as f:  # csv파일을 쓰기 모드로 오픈
#     cout = csv.writer(f)    # 파일 객체를 csv.write로 넣는다.
#     cout.writerow(data)     # list 데이터를 한 라인에 추가하게 된다.

data = []
with open('./data/imsi.csv', 'r', encoding='utf-8') as f:
    cin = csv.reader(f)
    data = [row for row in cin if row]
print(data)