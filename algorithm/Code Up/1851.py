n = int(input())

def stars(num):
    if num == 1:
        return '*'
    else:
        return '*' + stars(num-1)

print(stars(n))