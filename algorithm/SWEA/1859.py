T = int(input())
for i in range(T):
    days = int(input())
    price = list(map(int, input().split()))[::-1]
    result = 0
    maxx = price[0]

    for j in range(1, days):
        if maxx > price[j]:
            result += maxx - price[j]
        else:
            maxx = price[j]

    print(f'#{i+1} {result}')

"""
가장 비싼 날을 찾고
그 전까지의 값을 - 하면서 
비싼 날 값에 곱하고 
다시 반복

"""
    