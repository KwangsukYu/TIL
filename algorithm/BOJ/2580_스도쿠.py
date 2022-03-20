
r_arr = [list(map(int, input().split())) for _ in range(9)]
c_arr = list(map(list, zip(*r_arr)))

zero = []
for i in range(9):
    for j in range(9):
        if r_arr[i][j] == 0:
            zero.append((i, j))

def check(r, c):
    
    possible = [i for i in range(1, 10)]

    for i in range(9):
        if r_arr[r][i] in possible:
            possible.remove(r_arr[r][i])
        if r_arr[i][c] in possible:
            possible.remove(r_arr[i][c])

    r //= 3
    c //= 3
    for i in range(r*3, (r+1)*3):
        for j in range(c*3, (c+1)*3):
            if r_arr[i][j] in possible:
                possible.remove(r_arr[i][j])
    return list(possible)


def DFS(idx):
    global flag

    if idx == len(zero):
        flag = True
        for i in r_arr:
            print(*i)
        exit()

    r, c = zero[idx]

    pos_lst = check(r, c)
    for i in pos_lst:
        r_arr[r][c] = i
        DFS(idx+1)
        r_arr[r][c] = 0
    
DFS(0)




    

# r_arr = [list(map(int, input().split())) for _ in range(9)]
# c_arr = list(map(list, zip(*r_arr)))

# def check_squ():
#     global r_arr
#     di = [0, 0, 0, -1, -1, -1, 1, 1, 1]
#     dj = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
#     for i in range(1, 10, 3):
#         for j in range(1, 10, 3):
#             visited = [0 for _ in range(9)]
#             zero = 0
#             for k in range(9):
#                 ni = i + di[k]
#                 nj = j + dj[k]

#                 if r_arr[ni][nj] == 0:
#                     if not zero:
#                         zero = (ni, nj)
#                 elif not visited[r_arr[ni][nj] - 1]:
#                     visited[r_arr[ni][nj] - 1] += 1
#                 else:
#                     return False

#             if sum(visited) == 8:
#                 ni, nj = zero
#                 for l in range(9):
#                     if visited[l] == 0:
#                         r_arr[ni][nj] = l + 1
#                         break
#     return True

# def check_r():
#     global r_arr

#     for i in range(9):
#         visited = [0 for i in range(9)]
#         zero = 0
        
#         for j in range(9):
#             if r_arr[i][j] == 0:
#                 if not zero:
#                     zero = (i, j)
#             else: 
#                 if not visited[r_arr[i][j]-1]:
#                     visited[r_arr[i][j]-1] += 1
#                 else:
#                     return False

#         if sum(visited) == 8:
#             ni, nj = zero
#             for l in range(9):
#                     if visited[l] == 0:
#                         r_arr[ni][nj] = l + 1
#                         break
#     return True

# def check_c():
#     global r_arr

#     for i in range(9):
#         visited = [0 for i in range(9)]
#         zero = 0

#         for j in range(9):
#             if c_arr[i][j] == 0:
#                 if not zero:
#                     zero = (i, j)
#             else: 
#                 if not visited[c_arr[i][j]-1]:
#                     visited[c_arr[i][j]-1] += 1
#                 else:
#                     return False

#         if sum(visited) == 8:
#             ni, nj = zero
#             for l in range(9):
#                     if visited[l] == 0:
#                         r_arr[nj][ni] = l + 1
#                         break
#     return True

# def not_sd():
#     for i in range(9):
#         for j in range(9):
#             if r_arr[i][j] == 0:
#                 return True
#     return False

# while not_sd():
#     check_squ()
#     check_c()
#     check_r()

# for i in r_arr:
#     print(*i)
