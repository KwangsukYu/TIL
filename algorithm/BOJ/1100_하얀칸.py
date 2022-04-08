arr = [list(input()) for _ in range(8)]

ans = 0
for i in range(8):
    for j in range(8):
        if i % 2:
            if j % 2  and arr[i][j] == 'F':
                ans += 1

        else:
            if j % 2 == 0 and arr[i][j] == 'F':
                ans += 1

            
print(ans)