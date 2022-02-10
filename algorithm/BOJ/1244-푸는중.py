from ast import Try


S = int(input())
switch = list(map(int, input().split()))
students = int(input())

def female(num, swc):
    cnt = 0
    for i in range(1, len(swc)+1):
        if swc[num-1-i] + swc[num-1+i] == 1:
            break
        else:
            if num-1-i == 0 or num-1+i == len(swc):
                break
        cnt +=1
    
    if swc[num-1] == 1:
        swc[num-1] = 0
    else:
        swc[num] = 1

    for i in range(1, cnt + 1):
        if swc[num-1-i] == 1:
            swc[num-1-i] = 0
        else:
            swc[num-i] = 1

        if swc[num-1+i] == 1:
            swc[num-1+i] = 0
        else:
            swc[num+i] = 1    

        
    return swc
print(female(3, [0, 1, 1, 1, 0, 1, 0]))

for i in range(students): # male 1 female 2
    student, number = map(int, input().split())
    # 남학생            
    if student == 1:    
        for i in range(1, S + 1):
            if i % number == 0:
                if switch[i-1] == 0:
                    switch[i-1] = 1
                else:
                    switch[i-1] = 0
    else: # 0 1 *1 1 0 1 0 1
        switch = female(number, switch)

print(*switch)


