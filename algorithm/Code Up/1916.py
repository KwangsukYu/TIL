import sys
N = int(sys.stdin.readline())

dic = {}

def fibo(num):
    if num in dic:
        return dic[num]

    if num == 1:
        dic[1] = 1
        return 1
    elif num == 2:
        dic[2] = 1
        return 1
    else:
        dic[num] = fibo(num-1) + fibo(num-2) 
        return dic[num]

print(fibo(N)%10009)

