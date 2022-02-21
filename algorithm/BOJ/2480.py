dice = list(map(int, input().split()))

if len(set(dice)) == 1:
    print(dice[0]*1000 + 10000)
elif len(set(dice)) == 3:
    a = max(dice)
    print(a*100)
else:
    for i in range(1,3):
        if dice[0] == dice[i]:
            print(dice[0]*100 + 1000)
            break
    else:
        print(dice[1]*100 + 1000)
        

