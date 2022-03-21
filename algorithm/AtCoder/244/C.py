N = int(input())
num_lst = [i for i in range(1, 2 * N + 2)]

while True:
    print(num_lst.pop())

    if len(num_lst) == 0:
        exit()

    a = int(input())

    if a in num_lst:
        num_lst.pop(num_lst.index(a))
    else:
        break