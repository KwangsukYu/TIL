import sys
sys.stdin = open('sample_input.txt')

def partition(li, l, r):
    p = li[l]
    i = l
    j = r
    while i <= j:

        while i <= j and li[i] <= p:
            i += 1

        while i <= j and li[j] >= p:
            j -= 1
        if i < j:
            li[i], li[j] = li[j], li[i]

    li[l], li[j] = li[j], li[l]

    return j


def quick(li, l, r):
    if l <= r:
        s = partition(li, l , r)
        quick(li, s + 1, r)
        quick(li, l, s - 1)

for tc in range(1, 1+int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    quick(lst, 0, N-1)
    print(f'#{tc} {lst[N//2]}')

