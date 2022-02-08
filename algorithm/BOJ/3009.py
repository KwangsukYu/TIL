x, y = [], []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
ans = []
for j in x:
    if x.count(j) % 2:
        ans.append(j)
for k in y:
    if y.count(k) % 2:
        ans.append(k)
print(*ans)
