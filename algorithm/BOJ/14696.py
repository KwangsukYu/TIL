# 별이 있고 갯수가 다르면 별이 많은쪽 승
# 별이 같고 동그라미가 다르면 동그라미 많은 쪽 승
# 별 동 같, 네모 만흥쪽 승
# 별 동 네 같, 세모 많은 쪽 승
# 다 같으면 무승부
# 별 동 네 세 4 3 2 1

T = int(input())
for i in range(T):
    a = [0]*4
    b = [0]*4
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A[0] = B[0] = 0
    
    for i in A:
        if i == 0:
            continue
        else:
            a[-i] += 1

    for i in B:
        if i == 0:
            continue
        else:
            b[-i] += 1

    for i in range(4):
        if a[i] > b[i]:
            print('A')
            break
        elif a[i] < b[i]:
            print('B')
            break
    else:
        print('D')

