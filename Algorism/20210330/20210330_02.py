def solution(phone_book):
    for i in phone_book:
        print(i.replace(" ", "", 2))
    answer = True
    return answer

print(solution(['119', '97 674 223', '11 9552 4421']))