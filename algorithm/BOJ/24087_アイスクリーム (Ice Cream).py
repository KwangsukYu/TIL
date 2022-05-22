S = int(input()); A = int(input()) ; B = int(input())

height = S - A
if height <= 0:
    print(250)
    exit()

cost = height // B if height % B == 0 else height // B + 1

print(250 + cost*100)