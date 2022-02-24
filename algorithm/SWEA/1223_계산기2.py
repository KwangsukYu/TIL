import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    text = input()
    stack = []
    num_stack = []
    icp = {'+': 1, '*': 2}
    isp = {'+': 1, '*': 2}

    for i in range(N):
        try:
            num_stack.append(int(text[i]))
        except:
            if not stack:
                stack.append(text[i])

            else:

                if icp[text[i]] > isp[stack[-1]]:
                    stack.append(text[i])

                else:
                    while icp[text[i]] <= isp[stack[-1]]:
                        num_stack.append(stack.pop())
                        if not stack:
                            break
                    stack.append(text[i])

    while stack:
        num_stack.append(stack.pop())

    for i in range(len(num_stack)):
        try:
            stack.append(int(num_stack[i]))
        except:
            if num_stack[i] == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1+n2)
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
    print(f'#{tc}', *stack)

