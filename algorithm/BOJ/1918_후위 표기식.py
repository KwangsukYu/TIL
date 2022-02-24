def icp_priority(n):
    if n == '(':
        return 3
    elif n == '/' or n == '*':
        return 2
    else:
        return 1

def isp_priority(n):
    if n == '/' or n == '*':
        return 2
    elif n == '(':
        return 0
    else:
        return 1

text = input()        
stack1 = []
stack2 = []
op = ['-', '+', '/', '*', '(', ')']

for i in range(len(text)):
    if not text[i] in op:
        stack1.append(text[i])
    else:
        if not stack2:
            stack2.append(text[i])
        
        else:
            if text[i] == ')':
                while stack2[-1] != '(':
                    stack1.append(stack2.pop())
                stack2.pop()
            
            elif icp_priority(text[i]) > isp_priority(stack2[-1]):
                stack2.append(text[i])
            
            else:
                while icp_priority(text[i]) <= isp_priority(stack2[-1]):
                    stack1.append(stack2.pop())
                    if not stack2:
                        break
                stack2.append(text[i])

while stack2:
    stack1.append(stack2.pop())

print(''.join(stack1))

