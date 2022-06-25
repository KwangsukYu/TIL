ans = 0
min_v = 100
for i in range(7):
    num = int(input())

    if num % 2:
        ans += num
        if num < min_v:
            min_v = num

if ans:
    print(ans)
    print(min_v)
else:
    print(-1)