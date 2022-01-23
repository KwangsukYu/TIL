N = int(input())
num_list = list(map(int, input().split()))
sosu_list = []
for i in num_list:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sosu_list.append(i)

if 1 in sosu_list:
    sosu_list.remove(1)
print(len(sosu_list))



