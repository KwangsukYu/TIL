import sys
sys.stdin = open('sample_input.txt')

def winner(n1, n2):
    if (lst[n1] == 1 and lst[n2] == 3) or (lst[n1] == 2 and lst[n2] == 1) or (lst[n1] == 3 and lst[n2] == 2):
        return n1
    elif lst[n1] == lst[n2]:
        return n1
    else:
        return n2

def team(s, e):
    if s == e:
        return s
    else:
        t1 = team(s, (s+e)//2)
        t2 = team((s+e)//2 + 1, e)
        print(t1, t2)
        return winner(t1, t2)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {team(0,N-1)+1}')