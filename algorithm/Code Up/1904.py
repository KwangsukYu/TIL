a, b = input().split()

def odd(m, n):
    if m == 1 and n == 1:
        return 1
    elif m - 1 == n:
        if n % 2 == 0:
            return f'{n+1}'
        else:
            return f'{n}'

    elif m % 2 != 0:
        return f'{odd(m-1, n)} {m}'
    else:
        return f'{odd(m-1, n)}'

print(odd(int(b), int(a)))