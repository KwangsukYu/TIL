import sys

N = int(input())
num_lst = list(map(int,input().split()))
Q = int(input())
 
for q in range(Q):
    cnt = 0
    L, R, X = map(int, sys.stdin.readline().rstrip().split())
    L -= 1
    R -= 1
    while L <= R:
        if num_lst[L] == X:
            cnt +=1
        if num_lst[R] == X:
            cnt += 1
        L += 1
        R -= 1
    print(cnt)

