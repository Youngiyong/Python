inputNum = int(input())
n = []
for i in range(inputNum):
    a, b = input().split()
    n.append(int(a)+int(b))

for j in n:
    print(j)

try:
    sumlist = []
    inputline = int(input(''))
    for i in range(inputline):
        list = [int(j) for j in (input('').split())]
        sumlist.append(sum(list))
    for i in range(len(sumlist)):
        print(sumlist[i])
except:
    print("왜 숫자 아닌걸 입력하시나요..")