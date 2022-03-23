import sys
sys.stdin = open('input.txt')

# 문제에서 주어진 수들을 각각 인덱스 번호와 맞게 리스트로 만들어준다
num_lst = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011'
    ]

# 인풋 값은 string으로 받아서
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N) ]

    # 올바른 암호를 출력했을 경우를 알기 위한 flag 변수
    flag = True

    # 배열을 순회하며 암호를 찾는 함수
    def find_code(arr):
        res = []
        for i in arr:

            # 거꾸로 돌면서 1을 찾으면 그 부분부터 56개의 글자 수를 리스트에 담아서반환한다.
            for j in range(M-1, -1, -1):
                if i[j] == '1':
                    code = i[j-55:j+1]
                    res.append(code)
        return res

    # 그 암호가 올바른지 판단하는 함수
    def find_correct(code):
        res = 0

        # 짝수 홀수를 나눠서 조건에 맞게 res에 더해주기, 인덱스의 경우엔 짝수 홀수가 반대로 됨
        for i in range(7):
            if i % 2:
                res += code[i]
            else:
                res += code[i] * 3

        # 만약 총합과 마지막 검증 숫자를 더한게 10으로 나누어 떨어지면 True, 아니면 False를 반환
        if (res + code[-1]) % 10:
            return False
        else:
            return True

    # 위 암호를 찾는 함수를 실행해서 리스트를 받은 다음에
    res = find_code(arr)

    # 암호 리스트를 순회하면서
    for cod in res:

        # 해독 된 숫자를 담을 리스트
        code_num = []

        # 7자리씩 8개의 암호가 있으므로 8번 순회하면서 7자리씩 끊어준다.
        for i in range(8):
            res_code = cod[7*i : 7 + 7*i]

            # 처음에 만들어준 암호 숫자 리스트와 비교하여 같으면 code_num에 넣어줌
            for j in range(10):
                if res_code == num_lst[j]:
                    code_num.append(j)

        # 만약에 code_num에 숫자가 있고 올바른 암호라면
        # flag를 False로 바꿔주고 출력
        if code_num:
            if find_correct(code_num):
                flag = False
                print(f'#{tc} {sum(code_num)}')
            break

    # 만약 올바른 암호가 없다면 0을 출력
    if flag:
        print(f'#{tc} {0}')