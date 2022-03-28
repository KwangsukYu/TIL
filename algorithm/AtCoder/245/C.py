N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = [False for _ in range(N-1)]
x_list = [[] for _ in range(N-1)]

if len(A) >= 2:
    for i in range(N-1):
        if abs(A[i] - A[i+1]) <= K:
            ans[i] = True
            x_list[i].append((A[i], A[i+1]))

        elif abs(A[i] - B[i+1]) <= K:
            ans[i] = True
            x_list[i].append((A[i], A[i+1]))
            
        elif abs(B[i] - A[i+1]) <= K:
            ans[i] = True
            x_list[i].append((A[i], A[i+1]))

        elif abs(B[i] - B[i+1]) <= K:
            ans[i] = True
            x_list[i].append((A[i], A[i+1]))
else:
    print('Yes')
    exit()

for i in x_list:
    if not i:
        print('No')
        exit()

for i in range(N-2):
    if len(x_list[i]) >= 2 and len(x_list[i+1]) >= 2:
        if x_list[i][0][1] != x_list[i+1][0][0] and x_list[i][1][1] != x_list[i+1][0][0] and x_list[i][0][1] != x_list[i+1][1][0] and x_list[i][1][1] != x_list[i+1][1][0]:
            print('No')
            break

    elif len(x_list[i]) >= 2 and len(x_list[i+1]) == 1:
        if x_list[i][0][1] != x_list[i+1][0][0] and x_list[i][1][1] != x_list[i+1][0][0]:
            print('No')
            break
    
    elif len(x_list[i]) == 1 and len(x_list[i+1]) == 1:
        if x_list[i][0][1] != x_list[i+1][0][0] and x_list[i][0][1] != x_list[i+1][1][0]:
            print('No')
            break

    elif x_list[i][0][1] != x_list[i+1][0][0]:
        print('No')
        break
else:
    print('Yes')
