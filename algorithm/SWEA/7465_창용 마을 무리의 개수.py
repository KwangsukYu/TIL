import sys
sys.stdin = open('s_input.txt')

def find(n):
    while lst[n] != n:
        n = lst[n]
    return n

def union(n1, n2):
    lst[find(n1)] = find(n2)

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    lst = list(range(N+1))

    for _ in range(M):
        p1, p2 = map(int, input().split())
        # if p1 > p2: p1, p2 = p2, p1
        union(p1, p2)

    for i in range(N+1):
        lst[i] = find(i)

    print(f'#{tc} {len(set(lst))-1}')