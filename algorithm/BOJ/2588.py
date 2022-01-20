A = input()
B = input()

for i in range(-1, -len(B)-1, -1):
    print(int(A) * int(B[i]))


print(int(A) * int(B) )