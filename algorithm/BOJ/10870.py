n = int(input())

def fibo(num):
    if num == 1 or num ==0:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

print(fibo(n))