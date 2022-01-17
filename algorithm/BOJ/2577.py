A = int(input())
B = int(input())
C = int(input())

N = str(A*B*C)

for i in range(0, 10) :
    print(N.count(str(i)))
    