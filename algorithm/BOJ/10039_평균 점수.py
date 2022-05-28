total = 0
for i in range(5):
    N = int(input())
    if N < 40: N=40
    total += N 

print(total//5)