T = int(input())

lst = []

for i in range(T):
    x, y = map(int, input().split())
    lst.append([x, y])

cnt_lst = []
for i in range(T):
    cnt = 1
    for j in range(T):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]: 
            cnt += 1
    cnt_lst.append(cnt)

print(*cnt_lst)


