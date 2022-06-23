coordinate = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    coordinate.append((x, y))

coordinate.sort()

for x, y in coordinate:
    print( x, y)