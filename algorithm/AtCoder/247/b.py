N = int(input())

def DFS(name, idx):
    global flag

    if idx >= N*2:
        flag = True
        return

    if name_set[idx] not in name and name_set[idx+1] not in name:
        name.append(name_set[idx])
        DFS(name, idx+2)
        name.pop()
        name.append(name_set[idx+1])
        DFS(name, idx+2)

    elif name_set[idx] not in name:
        if name_set[idx+1] not in name:
            name.append(name_set[idx])
            DFS(name, idx+2)
    
    elif name_set[idx+1] not in name:
        if name_set[idx] not in name:
            name.append(name_set[idx+1])
            DFS(name, idx+2)

name_set = []

for i in range(N):
    a, b = input().split()
    name_set.append(a)
    name_set.append(b)
    flag= False
name = []
DFS(name, 0)

if flag:
    print('Yes')
else:
    print('No')