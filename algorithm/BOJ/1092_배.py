import sys

N = int(sys.stdin.readline().rstrip())
crane = sorted(list(map(int,sys.stdin.readline().rstrip().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
moved = [0]*M

if crane[0] < box[0]:
    print(-1)
    exit()

cnt = 0
while True:
    for i in range(len(crane)):
        for j in range(M):
            if crane[i] >= box[j]:
                if not moved[j]:
                    moved[j] = 1
                    break

    if len(moved) == M:
        cnt += 1
        print(cnt)
        break
    cnt += 1

# while box:

#     for i in crane:
#         for j in range(len(box)):
#             if i >= box[j]:
#                 box.pop(j)  
#                 break
#     cnt += 1

# print(cnt)
