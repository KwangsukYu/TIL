import sys
sys.stdin = open('sample_input.txt')

def calc(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '/':
        return int(n1 / n2)
    elif oper == '*':
        return n1 * n2

def check(li):
    stack = []
    for i in li:
        try:                        # 숫자면 stack에 저장 아니면 except 분기
            stack.append(int(i))
        except ValueError:
            if i == '.':            # .일 때 스택의 길이가 1이면 반환 아니면 error
                if len(stack) == 1:
                    return stack[-1]
                else:
                    return 'error'
            else:
                try:                        # . 이아닌 다른 기호일 때는 숫자 2개를 꺼내고 연산
                    n1 = stack.pop()
                    n2 = stack.pop()
                    num = calc(n2, n1, i)   # 순서 바꿔야함!
                    stack.append(num)
                except IndexError:          # 만약 숫자 두개가 없다면 error
                    return 'error'

T = int(input())
for tc in range(1, T + 1):
    sample = input().split()
    print(f'#{tc} {check(sample)}')

