v = int(input()); A = int(input()); B = int(input()); C = int(input()); D = int(input())
def n(a, b):
    return a // b + 1 if a % b > 0 else a // b
k = n(A, C) ; m = n (B, D)
print (v - k if k > m else v - m)