ex = {'a','e','i','o','u'}
while True:
    cnt = 0
    N = input()
    if N == '#':
        break
    for i in N:
        if i.lower() in ex:
            cnt += 1
    print(cnt)
    