x, y, w, h = map(int, input().split())

a, b = w - x, h - y

ans = [a, b, x, y]

print(min(ans))
    