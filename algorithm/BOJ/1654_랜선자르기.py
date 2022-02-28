import sys

K, N = map(int, sys.stdin.readline().split())

max_lan = 0
lan_lst = []
for i in range(K):
    lan = int(sys.stdin.readline())
    lan_lst.append(lan)
    if max_lan < lan: max_lan = lan
lst = []
s, e = 1, max_lan
while s <= e:
    tot = 0
    middle = (s+e) // 2

    for i in lan_lst:
        tot += i // middle
    
    if tot < N:
        e = middle - 1
    else:
        s = middle + 1

print(e)        # 최대 랜선의 길이