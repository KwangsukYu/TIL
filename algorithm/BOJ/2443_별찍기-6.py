N = int(input())
star = ['*']*(2*N-1)
print(''.join(star))
for i in range(N):
    star[i] = ' '
    star[-1-i] = ' '
    print(''.join(star).rstrip())