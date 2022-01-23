C = int(input())
for case in range(C):
    num_list = list(map(int, input().split()))
    avg = (sum(num_list) - num_list[0])/num_list[0]
    students = []
    
    for i in range(1, num_list[0]+1):
        if num_list[i] > avg:
            students.append(num_list[i])

    result = round(len(students)/num_list[0]*100, 3)
    print(f'{result:.3f}%')


