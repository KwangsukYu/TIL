R, C = map(int, input().split())

arr = [input() for _ in range(R)]

for i in arr:
    print(i[::-1])