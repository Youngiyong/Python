
pin = '880122-2234567'
birthday = pin[0:6]
gender = "남자"
if pin[5:6] == '2':
    gender = "여자"


a = [1,3,5,4,2]

a.sort(reverse=True)
print(a)


a = ['독도는', '대한민국의', '아름다운', '섬입니다.']
result = ' '.join(a)
print(result)

a=(1,2,3)
a += (4, )
print(a)

a = b = [1, 2, 3]
a[1] = 4
print(b)

i = 0;
j = 0;

i = 0

while i<5:
    i += 1
    print("*" * i)


kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]


for i in range(0, len(kor_score)):
    print('과목별 총점 :', kor_score[i]+math_score[i]+eng_score[i] )
    print('평균 :{0:.0f}'.format((kor_score[i]+math_score[i]+eng_score[i]) / len(midterm_score)))

life = {
    'animal': { 'cats' : "", 'octopi' : "", "emus" : "" },
    'plants': "",
    'other' : ""
}