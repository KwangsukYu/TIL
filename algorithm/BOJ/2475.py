N = input().split()

N_list = list(map(int,N))

total = 0
for i in N_list :
    total = total + i*i

print(total % 10)