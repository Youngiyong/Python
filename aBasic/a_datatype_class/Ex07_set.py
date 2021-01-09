# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다


s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])

print(s)

s3 = {5,6,4,3,5,6,6,6,6}
print(s3)


print(s.intersection(s3))  # 교집합
print(s.union(s3))   # 합집합
print(s - s3)     # 차 집합

print(s & s3)
print(s | s3)
#-----------------------
# [ 참고 ] and와 or 연산자의 결론
# 숫자인 경우에 0 - False, 0이 아닌 숫자 - True
a = 10      # True
b = -1      # True
if a and b:
    print('True1')
if a or b:
    print('True2')
print(a and b)  # True???   -1
print(a or b)   # True???   10

print(s and s3)
print(s or s3)
