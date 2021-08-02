def fibo(n):
    test = []
    for x in  range(0, n):
        if x<2:
            test.append(1)
        else:
            test.append(test[x-2] + test[x-1])
    return test[-1]

print(fibo(200))

