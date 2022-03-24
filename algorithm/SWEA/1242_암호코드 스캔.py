import sys
sys.stdin = open('sample_input.txt')

# def make_num(k):
#     n0 = '0' * k + '0' * k + '0' * k + '1' * k + '1' * k + '0' * k + '1' * k
#     n1 = '0' * k + '0' * k + '1' * k + '1' * k + '0' * k + '0' * k + '1' * k
#     n2 = '0' * k + '0' * k + '1' * k + '0' * k + '0' * k + '1' * k + '1' * k
#     n3 = '0' * k + '1' * k + '1' * k + '1' * k + '1' * k + '0' * k + '1' * k
#     n4 = '0' * k + '1' * k + '0' * k + '0' * k + '0' * k + '1' * k + '1' * k
#     n5 = '0' * k + '1' * k + '1' * k + '0' * k + '0' * k + '0' * k + '1' * k
#     n6 = '0' * k + '1' * k + '0' * k + '1' * k + '1' * k + '1' * k + '1' * k
#     n7 = '0' * k + '1' * k + '1' * k + '1' * k + '0' * k + '1' * k + '1' * k
#     n8 = '0' * k + '1' * k + '1' * k + '0' * k + '1' * k + '1' * k + '1' * k
#     n9 = '0' * k + '0' * k + '0' * k + '1' * k + '0' * k + '1' * k + '1' * k
#     num_lst = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
#
#     return num_lst
# num_lst = make_num(1)

num_lst = [
    '211', '221', '122', '411', '132', '231', '114', '312', '213', '112'
]
def find_correct(code):
    res = 0

    for i in range(7):
        if i % 2:
            res += code[i]
        else:
            res += code[i] * 3

    if (res + code[-1]) % 10:
        return False
    else:
        return True

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = set(input()[:M].rstrip('0') for _ in range(N))
    ans = 0
    code_num_lst = []
    arr = sorted(arr - {''})

    for i in arr:
        new_code = ''
        for j in i:
            new_code += format(int(j, 16), '04b')
        new_code = new_code.rstrip('0')
        cnt_lst = [0, 0, 0]
        code_num = []

        for k in range(len(new_code)-1, -1, -1):
            if new_code[k] == '1' and cnt_lst[1] == 0:
                cnt_lst[2] += 1
            elif new_code[k] == '0' and cnt_lst[0] == 0:
                cnt_lst[1] += 1
            elif new_code[k] == '1' and cnt_lst[1] != 0:
                cnt_lst[0] += 1
            elif new_code[k] == '0':
                if new_code[k-1] == '1':
                    min_v = min(cnt_lst)
                    check = ''

                    for l in cnt_lst:
                        check += str(l//min_v)

                    for q in range(10):
                        if check == num_lst[q]:
                            code_num.append(q)
                    cnt_lst = [0, 0, 0]

                    if len(code_num) == 8:
                        if find_correct(code_num[::-1]) and code_num[::-1] not in code_num_lst:
                            code_num_lst.append(code_num[::-1])
                            ans += sum(code_num)
                        code_num = []

    print(f'#{tc} {ans}')

