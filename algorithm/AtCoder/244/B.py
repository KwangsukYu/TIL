N = int(input()); order = input()
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

r = c = 0
k = 0

for i in order:
    if i == 'R':
        k = (k + 1) % 4
    else:
        r = r + dr[k]
        c = c + dc[k]

print(r, c)
