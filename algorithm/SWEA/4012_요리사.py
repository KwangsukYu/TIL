import sys
sys.stdin = open('sample_input.txt')
from itertools import combinations

def taste(li):
    result = 0
    #comb2 = list(combinations(li, 2))
    for i in range(1, 1<<len(li)):
        e = []
        for j in range(len(li)):
            if i & (1<<j):
                e.append(li[j])
        if len(e) == 2:
            result += arr[e[0]][e[1]] + arr[e[1]][e[0]]
    return result
    # for i in comb2:
    #     x, y = i
    #     result += arr[x][y] + arr[y][x]
    # return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dish1 = []
    min_v = 200000
    # comb = list(combinations(range(N), N//2))
    comb = []
    for i in range(1, 1<<N):
        e = []
        for j in range(N):
            if i & (1<<j):
                e.append(j)
        if len(e) == N//2:
            comb.append(e)

    L = len(comb)
    for i in range(L):
        comb2 = tuple(set(range(N)) - set(comb[i]))

        if abs(taste(comb[i]) - taste(comb2)) < min_v:
            min_v = abs(taste(comb[i]) - taste(comb2))

    print(f'#{tc} {min_v}')




# from itertools import combinations
# from collections import deque
#
# def taste(li):
#     result = 0
#     comb2 = list(combinations(li, 2))
#     for i in comb2:
#         x, y = i
#         result += arr[x][y] + arr[y][x]
#     return result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     dish1 = deque()
#     min_v = 200000
#     comb = deque(list(combinations(range(N), N//2)))
#
#     for i in comb:
#         dish1.append(taste(i))
#
#     L = len(comb)
#     for i in range(L):
#         dish2 = tuple(set(range(N)) - set(comb[i]))
#         for j in range(len(comb)):
#             if dish2 == comb[j]:
#                 if abs(dish1[i] - dish1[j]) < min_v:
#                     min_v = abs(dish1[i] - dish1[j])
#
#     print(f'#{tc} {min_v}')