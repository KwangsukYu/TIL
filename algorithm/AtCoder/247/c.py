N = int(input())
ans = ''
def recur(n):
    if n == 1:
        return 1
    else:
        return f'{recur(n-1)} ' + f'{n} ' + f'{recur(n-1)}'

print(recur(N))
