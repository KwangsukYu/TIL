def hanoi(n, start, end, other):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, other, end)
        print(start, end)
        hanoi(n-1, other, end, start)

num = int(input())
hanoi(num, 1, 3, 2)