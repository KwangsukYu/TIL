while True:
    A, B = map(int, input().split())

    if not A and not B:
        exit()
    
    if A <= B:
        print('No')
    else:
        print('Yes')