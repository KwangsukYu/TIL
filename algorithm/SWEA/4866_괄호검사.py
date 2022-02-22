import sys
sys.stdin = open('sample_input.txt')
# 괄호 순서도 고려

def check(t):
    stack = []
    for i in t:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            try:
                if i == ')':
                    if stack[-1] != '(':
                        return f'#{tc} {0}'
                    else:
                        stack.pop()
                else:
                    if stack[-1] != '{':
                        return f'#{tc} {0}'
                    else:
                        stack.pop()
            except IndexError:
                stack.append(i)

    return f'#{tc} {0}' if stack else f'#{tc} {1}'

T = int(input())
for tc in range(1, T + 1):
    text = input()
    print(check(text))

