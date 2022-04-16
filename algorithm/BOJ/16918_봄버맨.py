R, C, N = map(int, input().split())

arr = [list(input()) for _ in range(R)]

def boom(arr):
    boomlst = []
    for  i in range(R):
        for j in range(C):
            if arr[i][j] == '1':
                boomlst.append((i, j))
            elif arr[i][j] == '3':
                arr[i][j] = '1'
    
    for i, j, in boomlst:
        for di, dj in ((0, 0),(-1,0),(1,0),(0,1),(0,-1)):
            if 0 <= i+di < R and 0 <= j+dj < C:
                arr[i+di][j+dj] = '.'


def set_boom(arr):
    for  i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = '3'
            
            elif arr[i][j] == 'O':
                arr[i][j] = '1'

            elif arr[i][j] == '3':
                arr[i][j] = '1'

N -= 1
if N == 0:
    for i in arr:
        print(''.join(i))
    exit()

N -= 1
set_boom(arr)
if N == 0:
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '1' or arr[i][j] == '3':
                arr[i][j] = 'O'
    for i in arr:
        print(''.join(i))
    exit()

while N:

    N -= 1
    boom(arr)
    if not N: break

    N -= 1
    set_boom(arr)
    if not N: break

for i in range(R):
    for j in range(C):
        if arr[i][j] == '1' or arr[i][j] == '3':
            arr[i][j] = 'O'

for i in arr:
    print(''.join(i))