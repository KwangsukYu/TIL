N = int(input())

for i in range(N):
    list = input()
    total = 0
    count = 0
    for j in range(len(list)):
        if list[j] == 'O':
            count = count + 1       # 푸는 법은 알았는데 왜 코드를 못짜니!
            total = count + total   # 머리로는 이렇게 짜라고 생각은 했는데 짜는 법이 안 떠올라서 구글링 해봄...
        else:
            count = 0
    print(total)            
