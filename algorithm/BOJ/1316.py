def find_same(index_dict):
    for values in index_dict.values():
        for k in range(len(values)-1):
            if abs(values[k] - values[k+1]) != 1:
                return 0
    else:
        return 1

N = int(input())
ans = 0
for case in range(N):
    word = input()
    index_dict = {}
    cnt = 0

    for j in word:
        if j not in index_dict:
            index_dict[j] = [cnt]
            cnt += 1
        else:
            index_dict[j].append(cnt)
            cnt += 1
    ans += find_same(index_dict)

print(ans)


            



