S = int(input())
lst = list(map(int, input().split()))
set_lst = set(lst)
N = int(input())

if N in set_lst:
    print(0)
    exit()

cnt = 1000
for i in range(0, S-1):
    if list[i]