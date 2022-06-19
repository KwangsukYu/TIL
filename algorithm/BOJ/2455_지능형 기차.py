max_v = 0
in_train = 0
while True:
    Out, In = map(int,input().split())

    if In == 0:
        break
    
    in_train -= Out
    in_train += In
    if in_train > max_v:
        max_v = in_train
print(max_v)
