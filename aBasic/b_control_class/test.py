# kg = int(input("무게(킬로그램):"))
# m = float(input("키(미터):"))
# bmi = kg / (m ** 2)
# print('당신의 BMI:{:.2f}'.format(bmi))
# if 20 <= bmi <= 24.9:
#     print('정상입니다.')
# elif 25 <= bmi <= 29.9:
#     print('과체중입니다.')
# else:
#     print('비만입니다.')

from random import random
randomNum = str(int(random()*99))
print(randomNum)
inputNum = str(input("복권 번호(1-99사이)를 입력하시오:"))
if len(inputNum)==2:
    if randomNum[0] == inputNum[0] and randomNum[1] == inputNum[1]:
        print("100만원을 받는다.")
    elif randomNum[0] == inputNum[0] or randomNum[1] == inputNum[1]:
        print('50만원을 받는다.')
    else:
        print("상금은 없습니다.")
else:
    if randomNum[0]==inputNum[0]:
        print("100받는다.")
    else:
        print("상금은 없습니다.")

def even_filter(result=[]):
    list = [n for n in result if n%2==0]
    print(list)

even_filter([1,2,3,4,5,6])

def is_prime_number(input):
    list = [n for n in range(2,input) if input % n == 0]
    if (len(list)==0): return "소수"
    else: return "소수아님"
print(is_prime_number(61))


def count_vowel(a):
    count = 0;
    for i in a:
        count += 1;
    print(count)

count_vowel("dsdsdsdd")
count_vowel("악악악")