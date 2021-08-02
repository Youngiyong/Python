#각 자릿수의 값을 제곱해서 더해주는 함수
def solution(n):
    flag = True
    while flag:
        temp = 0
        for i in str(n):
            temp += int(i) * int(i)
        if temp==1:
            flag=False
        n=temp

    if flag is False:
        print("Happy")



solution(43)


