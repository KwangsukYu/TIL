N, target = map(int, input().split())
coins = []
for i in range(N):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

cnt = 0

for i in coins:
    while target - i >= 0:
        cnt += target//i
        target = target % i

print(cnt)
