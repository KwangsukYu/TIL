import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    n1, n2 = len(str1), len(str2)     # 각 문자열의 길이를 측정하고
    for i in range(n2 - n1 + 1):      # 반복 횟수 = 큰 문자열 - 작은 문자열 + 1 ex) 5, 2 01 12 23 34
        if str1 == str2[i:i+n1]:      # 인덱스로 한칸씩 옮겨가면서 비교
            print(f'#{tc} {1}')       # 맞으면 1
            break
    else:
        print(f'#{tc} {0}')           # 아니면 for - else 로 0

# 3143

#

def brute_force(pattern, text):
    i = j = 0                         # j는 pattern, i는 text의 idx

    p = len(pattern)
    t = len(text)

    while j < p and i < t:            # 페탄의 인덱스와 전체 인덱스의 길이 조절
        if pattern[j] != text[i]:
            i -= j
            j = -1                    # 뒤에서 +1 을 하면 0이 되어서 처음부터 찾음
        i += 1
        j += 1

        if j == p:
            return 1
        else:
            return 0
