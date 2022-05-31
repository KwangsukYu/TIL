N = int(input())
d = [0] * 50
d[0] = 0
d[1] = 1
d[2] = 1

for i in range(2, 50):
    d[i] = d[i-1] + d[i-2]

print(d[N])
