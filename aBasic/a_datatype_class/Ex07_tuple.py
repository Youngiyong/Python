"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여  - 리스트와 동일하게 추출
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1, 2, 3) # list = [1, 2, 3]
print(t)
# print(t(0))   //에러
print(t[0])

t2 = 1, 2, 3    #권장하지 않음
print(t2[-1])

# 빈 튜플 생성
t3 = ()
print(t3)
t4 = tuple()
print(t4)
# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0;  # 블럭이 생기면서 실행 안됨
# del t[1]   # 에러 발생
print('------------------- 2 -----------------')
t = (1,2,3)
# t[1]=0
print(t)
del t  # 가능함(정상코딩)
# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')
# *************** 튜플요소가 하나인 경우 ( ,)
#
t2 = ('one',)
print(t2)
print(t2[0])
print(type(t2))

tt = ('one', 'two')
print(tt)
print(tt[0])
print(type(tt))
# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
t1 = (1,)
t2 = (5,6,7)
print(t1 + t2)
print(t2 * 2)
print(t2[-1])
print(t2[1:])

# (5) 튜플 요소 풀기
print('-'*50)
t5 = (1,2,3)
a,b,c = t5
print(a+b+c)
print(a, b, c)

print(sum(t5))

# (6) 튜플과 리스트 출력
print('='*50)
my_list = ['a','b','c']
my_tuple = ('z','y','x')
print(tuple(my_list))
print(list(my_tuple))

print(type(my_list))
yr_tuple = tuple(my_list)
print(type(yr_tuple))