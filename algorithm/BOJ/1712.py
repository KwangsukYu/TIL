a, b, c = map(int, input().split())

# if c <= b:
#     print(-1)
# else:
#     n = 1
#     while True:
#         if c*n > a + b*n:
#             print(n)
#             break
#         else:
#            n += 1
if b >= c:
    print(-1)
elif b == 0 or c == 0:
    print(-1)
else:
    ans = a // (c - b)
    print(ans + 1)
