N = int(input())
order = list(map(int, input().split()))

order.sort()


for i in range(1, len(order)):
    order[i] = order[i-1] + order[i]

print(sum(order))

