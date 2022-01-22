T = int(input())

for i in range(1, T+1):
    numlist = list(map(int, input().split()))
    total = 0
    for j in numlist:
        if j % 2 != 0:
            total += j
    print(f"#{i} {total}")

