def solution(L, x):
    temp = 0
    L.sort()
    for i in L:
        if x<=i:
            temp = L.index(i)
            break
        else:
            temp = L.index(i)
    answer = L
    answer.insert(temp, x)
    return answer


print(solution([30, 17, 58, 72, 91], 1))