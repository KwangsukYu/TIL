N = int(input())
if N >= 100:
    if N % 10 == 0:
        ans = N//100 + 10
        print(ans)
    else:
        ans = 10 + N % 100
        print(ans)
else:
    ans = N//10 + N%10
    print(ans)