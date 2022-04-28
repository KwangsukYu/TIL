N = int(input())
lst = []

for i in range(N):
    num = int(input())
    lst.append(num-1)

max_v = 0
ans = 0
ans_i = 0


for i in range(N):
    ans_idx = [i]
    ans_v = [lst[i]]

    for j in range(N):
        if i == j:
            continue

        if j == lst[j]:
            ans_idx.append(j)
            ans_v.append(lst[j])

        elif j in ans_v:
            ans_idx.append(j)
            ans_v.append(lst[j])
        
        elif lst[j] in ans_idx:
            ans_idx.append(j)
            ans_v.append(lst[j])


    if len(ans_idx) > max_v:
        remove_lst = []
        for i in ans_idx:
            if i not in ans_v:
                remove_lst.append(i)
        max_v = len(ans_idx)
        ans_i = ans_idx
        ans = ans_v

ans.sort()

for i in remove_lst:
    r = ans_i.index(i)
    ans.pop(r)
print(len(ans))

for i in ans:
    print(i+1)


