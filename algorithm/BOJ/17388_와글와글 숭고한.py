lst = list(map(int, input().split()))
if sum(lst) >= 100: print("OK")
else :
    ans = lst.index(min(lst))
    if ans == 0:
        print("Soongsil")
    elif ans == 1:
        print("Korea")
    else:
        print("Hanyang")