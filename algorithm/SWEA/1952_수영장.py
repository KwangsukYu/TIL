import sys
sys.stdin = open('sample_input.txt')

def check(idx, v):
    global min_price

    if v > min_price:
        return

    if idx == 12:
        if v < min_price:
            min_price = v
        return

    check(idx + 1, v + plan[idx] * price[0])
    check(idx + 1, v + price[1])
    if idx < 10:
        check(idx + 3, v + price[2])

for tc in range(1, int(input()) + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    min_price = price[3]
    check(0, 0)
    print(f'#{tc} {min_price}')