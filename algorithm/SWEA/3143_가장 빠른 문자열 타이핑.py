import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    new_A = A.replace(B, '_')       # 저장된 문자열을 아무 문자 한개로 바꿔서
    print(f'#{tc} {len(new_A)}')    # 출력