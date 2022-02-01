# 벌집 1 2 3 4 5
# 가로 1 2 3 4 5 
# 세로 1 1 3 5 7 

N = int(input())


sum = 1
cnt = 1 
n = 1
while sum < N :
    cnt += 1
    sum += 2 * (cnt + 2 * (cnt - 1) - 1)
    

print(cnt)
