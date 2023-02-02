from itertools import combinations

def chk_idx(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

def check_student(r, c):
    for i in range(1, N):
        if chk_idx(r, c+i):
            if new_arr[r][c+i] == 'S':
                return False
            if new_arr[r][c+i] == 'O':
                break
        else:
            break

    for i in range(1, N):
        if chk_idx(r, c-i):
            if new_arr[r][c-i] == 'S':
                return False
            if new_arr[r][c-i] == 'O':
                break
        else:
            break

    for i in range(1, N):
        if chk_idx(r+i, c):
            if new_arr[r+i][c] == 'S':
                return False
            if new_arr[r+i][c] == 'O':
                break
        else:
            break
        
    for i in range(1, N):
        if chk_idx(r-i, c):
            if new_arr[r-i][c] == 'S':
                return False
            if new_arr[r-i][c] == 'O':
                break
        else:
            break

    return True

def check_arr(comb):
    for r, c in comb:
        new_arr[r][c] = 'O'
    for r, c in teachers:
        if not check_student(r, c):
            return False
    return True

N = int(input())
arr = [list(input().split()) for _ in range(N)]

teachers = []
empty_space = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            empty_space.append((i, j))
        
        if arr[i][j] == 'T':
            teachers.append((i, j))

comb = combinations(empty_space, 3)

ans = "NO"
for c in comb:
    new_arr = [i[:] for i in arr]
    if check_arr(c):
        ans = "YES"
        break


print(ans)