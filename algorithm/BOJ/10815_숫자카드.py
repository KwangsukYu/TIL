N = int(input())
sang = set(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

for i in cards:
    if i in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')