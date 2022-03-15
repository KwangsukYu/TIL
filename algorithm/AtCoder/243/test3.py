N = int(input())
lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append([y, x])

order = input()
dic_l_max = {}
dic_r_min = {}

# left - max 
for i in range(N):
    if order[i] == 'L':
        try:
            if lst[i][1] > dic_l_max[f'{lst[i][0]}']:
                dic_l_max[f'{lst[i][0]}'] = lst[i][1]
        except:
            dic_l_max[f'{lst[i][0]}'] = lst[i][1]

# right - min
    if order[i] == 'R':
        try:
            if lst[i][1] < dic_r_min[f'{lst[i][0]}']:
                dic_r_min[f'{lst[i][0]}'] = lst[i][1]
        except:
            dic_r_min[f'{lst[i][0]}'] = lst[i][1]

for k, v in dic_l_max.items():
    try:
        if dic_r_min[k] < v:
            print('Yes')
            break
    except:
        pass
else:
    print('No')