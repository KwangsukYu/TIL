import sys

a = [True for number in range(10000 + 1)]
a[1] = False
for i in range(2, int(10000**0.5) + 1):
    if a[i] == True:
        j = 2
        while i * j <= 10000:
            a[i * j] = False
            j += 1
prime = [i for i in range(2, 10000 + 1) if a[i]==True]

T = int(sys.stdin.readline())

for test in range(T):
    n = int(sys.stdin.readline())
    ans = []
    for j in prime[:n]:
        if n - j in prime and j <= n - j:
            ans.append([j, n - j])
    print(*ans[-1])
    

#     print(ans)
    # for k, v in ans.items():
    #     if min(ans.values()) == v:
    #         print(k)
        
                

