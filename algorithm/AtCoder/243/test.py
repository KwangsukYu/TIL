V, A, B, C = map(int, input().split())

lst = [A, B, C]

i = 0
while True:
    if i == 3:
        i = 0
    V = V - lst[i]
    if V < 0:
        if i == 0:
            print('F')
            break
        elif i == 1:
            print('M')
            break
        else:
            print('T')
            break
    i += 1


