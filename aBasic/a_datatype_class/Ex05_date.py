"""

"""
# import datetime
# today = datetime.date.today();
# print('today is ', today)

from datetime import date, timedelta
today = date.today();
print('today is ', today)
print('년도 ', today.year)
print('월 ', today.month)
print('일 ', today.day)

# 날짜계산 -> timedelta
#from datetime import timedelta

print('어제', today + timedelta(days=-1))
print('일주일후', today + timedelta(weeks=1))
print('10일전', today + timedelta(days=-10))
print('한달전', today + timedelta(weeks=-4))

from dateutil.relativedelta import relativedelta
aftermonth = today + relativedelta(months=1)
print(aftermonth)

#------------------------------------------------------
# 날짜 형식 출력 ( strftime() )

from datetime import datetime
onul = datetime.today()
print(onul) # 2021-01-06 09:52:27.454561
print(onul.strftime("%m-%d-%Y >> %H : %M"))

# 문자열을 날짜형으로 변환 ( ***** strptime() )
naljja = '2021-01-08 12:50'
mydate = datetime.strptime(naljja, '%Y-%m-%d %H:%M')
print(mydate)
print(type(mydate))
print(type(onul))

print(','.join(str(i) for i in range(2,8)))