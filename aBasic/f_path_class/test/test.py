class Calculator:

    def __init__(self,data):
        self.data=data

    def sum(self):
        self.sum=0
        for i in self.data:
            self.sum+=i
        print(self.sum)

    def avg(self):
        self.avg=self.sum/len(self.data)
        print(self.avg)

cal1=Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

ko = input("국어 성적을 입력하세요 : ")
math = input("수학 성적을 입력하세요 : ")
en = input("영어 성적을 입력하세요 : ")

calc = int(ko) + int(math) + int(en)
avg = calc / 3
result = round(avg, 2)

print("국어 성적 : ", ko)
print("수학 성적 : ", math)
print("영어 성적 : ", en)

print("총점 : ", calc)
print("평균 : ", result)


def product(scalar,num_list):
    print([num*scalar for num in num_list])

product( 5,[1,2,3,4] )

matrix_x = [[2,5],[2,1]]
matrix_y = [[2,4],[5,3]]

def matrix_add(*matrix_variables):
    return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]

print(matrix_add(matrix_x, matrix_y))


def vector_sub(*vector_variables):
    return [t[0] * 2 - sum(t) for t in zip(*vector_variables)]

print(vector_sub([1, 3], [2, 4]))
print(vector_sub([1, 5], [10, 4], [4, 7]))