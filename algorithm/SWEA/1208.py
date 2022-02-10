import sys
sys.stdin = open('input.txt')
for ts in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    def sort_box(x):
        for j in range(99, 0, -1):
            for i in range(0, j):
                if x[i] > x[i+1]:
                    x[i], x[i+1] = x[i+1], x[i]
        return x
    a = box
    while N > 0:
        a[-1] -= 1
        a[0] += 1
        if a[-1] == a[0]:
            print(a[-1] - a[0])
        a = sort_box(box)
        N -= 1
    print(f'#{ts} {a[-1] - a[0]}')










