import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, nums = input().split()                       # 인풋을 문자열로 받고
    stack = []                                      # 스택 리스트 만들어준다
    top = -1                                        # top은 -1 부터
    for i in range(int(N)):                         # 문자열이기에 int(N)
        if stack == [] or nums[i] != stack[top]:    # stack이 비어있거나 nums[i]가 마지막꺼와 다르면
            stack.append(nums[i])                   # stack에 추가하고 top += 1
            top += 1
        else:                                       # 같은 경우에는 마지막껄 pop해주고
            stack.pop()                             # top -= 1
            top -= 1
    print(f'#{tc}', ''.join(stack))                 # 출력형식에 맞추어 출력