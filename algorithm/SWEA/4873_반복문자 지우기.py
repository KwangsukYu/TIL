import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    text = input()
    lst = []

    for i in range(0, len(text)):
        try:                        # 첫 번째 부터 -1로 비교하니 에러 처리를 위함
            if text[i] == lst[-1]:
                lst.pop()
            else:
                lst.append(text[i])

        except IndexError:
            lst.append(text[i])

    print(f'#{tc} {len(lst)}')

