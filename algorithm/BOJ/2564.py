def short(dong, shop):
    short_x = 0
    short_y = 0
    if dong is shop:
        return 0
    else:
        if dong[1] == shop[1]:
            short_x = abs(dong[0] - shop[0])
        else:    
            if dong[0] + shop[0] <= 2 * x - dong[0] - shop[0]:
                short_x = dong[0] + shop[0]
            else:
                short_x = 2 * x - dong[0] - shop[0]

        if dong[0] == shop[0]:
            short_y = abs(dong[1] - shop[1])
        else:
            if dong[1] + dong[1] <= 2 * y - dong[1] - shop[1]:
                short_y = dong[1] + shop[1]
            else:
                short_y = 2 * y - dong[1] - shop[1]
        return short_x + short_y
        
x, y = map(int, input().split())
location = []
N = int(input())
for i in range(N + 1):
    a, b = map(int, input().split())
    if a == 1:
        location.append([b, y])
    elif a == 2:
        location.append([b, 0])
    elif a == 3:
        location.append([0, y-b])
    else:
        location.append([x, y-b])

donggeon = location[-1]
ans = 0

for i in location[:-1]:
    ans += short(donggeon, i)

print(ans)