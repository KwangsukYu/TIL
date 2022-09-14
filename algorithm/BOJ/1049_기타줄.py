N, M = map(int, input().split())
min_price = 1000000
min_set_price = 1000000

for i in range(M):
    six, one = map(int, input().split())
    if six < min_set_price:
        min_set_price = six
    
    if one < min_price:
        min_price = one
        
total_price = 0
while True:
    if N < 6:
        total_price += min(min_set_price , min_price * N)
        break
    else:
        total_price += min(min_set_price * (N // 6), min_price * 6 *  (N // 6))
        N = N % 6

print(total_price)

    

