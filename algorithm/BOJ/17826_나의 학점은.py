score = list(map(int, input().split()))
hong = int(input())
score.append(hong)
score.sort(reverse=True)
ans = score.index(hong) + 1

if ans <= 5: print('A+')
elif ans <= 15: print('A0')
elif ans <= 30: print('B+')
elif ans <= 35: print('B0')
elif ans <= 45: print('C+')
elif ans <= 48: print('C0')
else : print('F')