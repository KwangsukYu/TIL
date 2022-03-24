import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):         # 인풋 받기
    N = float(input())
    lst = [2**-i for i in range(1, 13)]     # 미리 12자리 수까지 구해놓고
    print(lst)
    print(f'#{tc}', end=' ')

    for i in range(1, 1<<12):               # 가능한 모든 조합의 합에서 N이 나오면
        sum_v = 0
        idx_lst = []                        # 인덱스와 같이 담아서
        for j in range(12):
            if i & (1<<j):
                sum_v += lst[j]
                idx_lst.append(j)

        if sum_v == N:
            ans = ''
            for i in range(idx_lst[-1]+1):  # ex) [0, 2]면 리스트의 길이 +1 만큼 순회하면서
                if i in idx_lst:            # i 가 리스트 안에 있으면 1을 문자열에 더해준다.
                    ans += '1'
                else:
                    ans += '0'              # 없으면 0을 더해준다.
            break
    else:                                   # 조합의 합에서 나오지 않는다면 overflow
        print('overflow')
