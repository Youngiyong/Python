def solution(n):
    temp = ''
    for i in n:
        temp += str(i)

    temp2 = int(temp)+1
    return temp2

print(solution([6,2,9,9]))
