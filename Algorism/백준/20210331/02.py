

def solution(L, x):
    answer = []
    print(type(L))
    print(type(x))
    try:
        L.index(x)
    except:
        return -1
    for i in range(len(L)):
        if L[i]==x:
            answer.append(L[i:].index(x))

    return answer


L = [3, 6, 2, 8, 7, 3]
print(solution(L, 3))
