import sys
sys.stdin = open('input.txt')

icp = {'*': 2, '+': 1, '(': 3}
isp = {'*': 2, '+': 1, '(': 0}

for tc in range(1, 11):
    N = int(input())
    text = input()
    stack = []
    num_stack = []

    for i in range(N):
        try:
            num_stack.append(int(text[i]))
        except:
            if not stack:
                stack.append(text[i])
            else:
                if text[i] == ')':
                    while stack[-1] != '(':
                        num_stack.append(stack.pop())
                    stack.pop()

                elif icp[text[i]] > isp[stack[-1]]:
                    stack.append(text[i])
                else:
                    while icp[text[i]] <= isp[stack[-1]]:
                        num_stack.append(stack.pop())
                    stack.append(text[i])

    for i in range(len(num_stack)):
        try:
            stack.append(int(num_stack[i]))
        except:
            n1 = stack.pop()
            n2 = stack.pop()

            if num_stack[i] == '+':
                stack.append(n1 + n2)
            else:
                stack.append(n1 * n2)

    print(f'#{tc}', *stack)