n = int(input())

def bi(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    
    if num % 2 == 0:
        return bi(int(num/2)) + '0'
    
    else:
        return bi(int(num/2)) + '1'

print(bi(n))
