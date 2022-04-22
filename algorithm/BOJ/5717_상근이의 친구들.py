while True:
    x, y = map(int, input().split())

    if not x and not y:
        break
    else:
        print(x+y)