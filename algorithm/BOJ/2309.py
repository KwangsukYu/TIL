cm = []
tot = 0
for i in range(9):
    nanzang2 = int(input())
    cm.append(nanzang2)
    tot += nanzang2

def find_spy(li):
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            else:
                if li[i] + li[j] == tot - 100:
                    li[i] = li[j] = 0
                    return li
cm = find_spy(cm)

for i in range(8, 0, -1):
    for j in range(0, i):
        if cm[j] > cm[j+1]:
            cm[j], cm[j+1] = cm[j+1], cm[j]

for i in cm:
    if i == 0:
        continue
    else:
        print(i)
