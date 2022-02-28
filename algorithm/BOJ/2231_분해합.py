N = int(input())

def check(N):
    for i in range(1, N + 1):
        a = i
        tot = i
        while i > 0:
            tot += i % 10
            i //= 10
        if tot == N:
            return a
    return 0

print(check(N))
