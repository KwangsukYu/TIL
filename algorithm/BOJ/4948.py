import math

a = [True for i in range(2 * 123456 + 1)]
for i in range(2, int(math.sqrt(2 * 123456)) + 1):
    if a[i] == True:
        j = 2
        while i * j <= 2 * 123456:
            a[i * j] = False
            j += 1

n = 1
while n > 0:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(a[n + 1:2 * n].count(True))

    