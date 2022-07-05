for i in range(int(input())):
    t = input()
    if len(t) > 1:
        print(t[0]+t[-1])
    else:
        print(t[0]+t[0])