import sys
sys.stdin = open('sample_input.txt')

def check(li, n, m):
    for j in range(n):                      # 행이랑 글자 수랑 같으면 한 번에 거꾸로 계산 가능, 오류 안남
        for k in range(n - m + 1):          # 반복 횟수는 행 - 회문의 길이 + 1만큼 5, 2 > 01, 12, 23, 34
            if k == 0:
                if li[j][:m] == li[j][m-1::-1]:
                    return li[j]
            else:                           # 다른 경우에는 인덱스를 범위만큼 조절해가면서 반복한다.
                if li[j][k:k+m] == li[j][k+m-1:k-1:-1]:
                    return li[j][k:k+m]
    else:
        return False                        # 없으면 False 리턴

T = int(input())

for tc in range(1, 2):                  # 인풋 받는 곳
    N, M = map(int, input().split())
    r_text = [input() for _ in range(N)]
    c_text = []                             # 세로줄을 문자열로 만들 리스트

    for i in range(N):
        c_t = ''
        for j in range(N):                  # 세로줄 문자하나하나 c_t에 추가하면서
            c_t += r_text[j][i]
        c_text.append(c_t)                  # 한 줄이 되면 c_text에 넣어줌
    print(c_text)

    row = check(r_text, N, M)               # 가로줄 회문 체크
    col = check(c_text, N, M)               # 세로줄 회문 체크

    if row:                                 # 회문이 1개니까 False가 아니면 출력
        print(f'#{tc} {row}')
    elif col:
        print(f'#{tc} {col}')
    else:                                   # 둘다 False면 False출력
        print(row)


