# 1 2 1    4 
# 1 2 3 2 1   9
# 1 2 3 4 3 2 1 16
# 1 2 3 4 5 4 3 2 1 25


T = int(input())

for test in range(T):
    x, y = map(int, input().split())
    dist = y - x
    sqt = 0
    for i in range(1, 2**31):
        if i**2 > dist:
            sqt = i - 1
            break
    cnt_plus = dist - sqt**2

    def haah(num, sqt_f):
        cnt = 0
        while num > 0:
            if num - sqt_f == 0:
                cnt += 1
                return cnt
            elif num - sqt_f < 0:
                sqt_f -= 1
            else:
                cnt += num //sqt_f
                if num//sqt_f == 0:
                    return cnt
                num = num % sqt_f
                sqt_f -= 1

    if sqt == 1:
        print(dist)
    else:
        if cnt_plus:
            print(2 * sqt - 1 + haah(cnt_plus, sqt))
        else:
            print(2 * sqt - 1)

    








