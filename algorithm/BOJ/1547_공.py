import sys
input = sys.stdin.readline

for i in range(3):
    N = int(input())
    ssum = 0
    for j in range(N):
        num = int(input())
        ssum += num
    
    if ssum > 0:
        print('+')
    elif ssum < 0:
        print('-')
    else:
        print(0)