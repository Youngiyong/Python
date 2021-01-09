
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴

msg = '{1}님 오늘도 행복햐~ {0}로부터'
print(msg.format('홍길동', '이진강'))

msg = '{to}님 오늘도 행복햐~ {by}로부터'
print(msg.format(to='홍길동', by='이진강'))

# [참고] http://pyformat.info

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456

print('%s님은 %d세이고 신장은 %10.3fcm 입니다' % (name,age,height))
print('{0}님은 {1}세이고 신장은 {2:.0f} cm 입니다'.format(name,age,height))
msg = '{name}남은 {age}세이고 신장은 {height}cm 입니다'
print(msg.format(name="홍길동", age=22, height=170.456))

#--------------------------------------------------
# 실수인 경우


