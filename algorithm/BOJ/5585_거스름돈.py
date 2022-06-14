N = int(input())
change = 1000 - N

money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in money:
    while True:
        if change - i >= 0:
            cnt += 1
            change -= i
        else:
            break

print(cnt)
