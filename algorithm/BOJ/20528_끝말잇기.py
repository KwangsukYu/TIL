def Ispel(t):
    if t == t[::-1]:
        return True

N = int(input())
t_lst = list(input().split())

for i in range(N-1):
    if Ispel(t_lst[i]) and Ispel(t_lst[i+1]) and t_lst[i][-1] == t_lst[i+1][0]:
        pass
    else:
        print(0)
        exit()

print(1)