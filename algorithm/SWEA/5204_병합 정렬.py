import sys
sys.stdin = open('sample_input.txt')

def divide(li):
    if len(li) == 1:
        return li

    middle = len(li) // 2

    left = divide(li[:middle])
    right = divide(li[middle:len(li)])

    return merge(left, right)

def merge(left, right):
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    i = j = 0
    while i < len(left) or j < len(right) :
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left) and j >= len(right):
            result.append(left[i])
            i += 1
        elif i >= len(left) and j < len(right):
            result.append(right[j])
            j += 1

    return result

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    sorted_list = divide(lst)
    print(f'#{tc} {sorted_list[N//2]} {cnt}')