N = int(input())
M = int(input())
sosu_list = []
for i in range(N, M+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sosu_list.append(i)

if 1 in sosu_list:
    sosu_list.remove(1)

if sosu_list == []:
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))