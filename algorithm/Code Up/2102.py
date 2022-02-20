N = int(input())
j = 1
flag = False
while N * j < 2**64:
    str_num = str(N * j)
    for i in str_num:
        if i == '1' or i == '0':
            pass
        else:
            break
    else:
        flag = True

    if flag:
        break

    j += 1
print(str_num) 