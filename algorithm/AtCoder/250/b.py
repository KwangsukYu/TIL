N, A, B = map(int,input().split())

arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i % 2:
            if j % 2:
                arr[i][j] = '.' * B
            else:
                arr[i][j] = '#' * B
        else:
            if j % 2:
                arr[i][j] = '#' * B 
            else:
                arr[i][j] = '.' * B

i = 0

while i < N*A:
    new_arr = arr[i]

    for _ in range(A-1):
        arr.insert(i, new_arr)
    
    i += A

for i in arr:
    print(''.join(i))



