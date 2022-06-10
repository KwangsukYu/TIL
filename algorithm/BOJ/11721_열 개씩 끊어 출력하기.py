T = input()

idx = 0
cnt = 0
while True:
    print(T[idx], end='')
    cnt += 1
    if cnt == 10:
        cnt = 0
        print()
    idx += 1

    if idx >= len(T):
        break

