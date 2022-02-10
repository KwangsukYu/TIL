# import sys
# sys.stdin = open('s_input.txt')

# 5000개의 버스, N개의 버스 노선
# i 번째 버스 노선은 번호가 A이상 B이하만 다님
# P개의 버스정류장에 대해 각 정류장에 몇대의 버스가 다니는지?
# P개의 J번째 줄에는 하나의 정수가 주어진다.

T = int(input())
for t in range(T):
    N = int(input())
    total_station = [0]*5000
    for n in range(N):
        x, y = map(int, input().split())
        for i in range(x - 1, y):
            total_station[i] += 1
    P = int(input())
    ans = []
    for i in range(P):
        a = int(input())
        ans.append(total_station[a-1])
    print(f'#{t+1}', *ans)



