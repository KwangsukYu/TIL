import sys
sys.setrecursionlimit(1000000)

n = int(input())

def my_sum(num):
    if num == 1:
        return 1
    else:
        return num + my_sum(num-1)

print(my_sum(n))