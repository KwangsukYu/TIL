# 두항의 차이가 모두 일정한 수열?
N = int(input())
cnt = 0
def is_hansu(number):
    x = number//100
    y = (number - 100 * x) // 10
    z = number % 10
    if x - y == y - z:
        return True
        
for i in range(100, N+1):
    if is_hansu(i):
        cnt += 1

if N < 100:
    cnt = N
else:
    cnt += 99    
print(cnt)
