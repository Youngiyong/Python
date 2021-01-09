"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = eval(input('나이 입력->'))
# print(age+1, '세입니다')
# print(type(age))
#
# key = eval(input('키를 입력->'))
# print(key, 'cm입니다')
# print(type(key))
# #----------------------------------
# # 단을 입력받아 구구단을 구하기
# num = int(input("단을 입력->"))
# for i in range(1, 10):
#     #print(num, '*', i, num*i )
#     print('{} * {} = {}'.format(num, i, num*i))
#
# avg = 0
# for i in range(0, 5):
#     num= int(input("정수를 입력하세요:"))
#     avg += num
#
# print(avg/5)
#-----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕', '친구')
print('안녕' '친구')

for i in range(2, 8):
    print(i)

# 3번문제
import numpy

num = map(int, input('정수리스트 입력').split())
numlist = list(num)

print(len(numlist))
print(sum(numlist))

def calc(numlist):
    print('평균 : ',sum(numlist)/len(numlist) )
    print('표준편차 : ', numpy.std(numlist))

calc(numlist)

# test = []
# test = int(input("정수리스트입력 :"))
# print(test)
# test = [ 1, [2, 'ABC'], [3, 'DEF'], [4, 'GHI'], [5, 'JKL'], [6, 'MNO'], [7, 'PQRS'], [8, 'TUV'],
#          [9, 'WXYZ'],'*',0,'#']


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3

import sys
args = sys.argv[1:]
for i in args:
    print(i)
print('서버 연결')