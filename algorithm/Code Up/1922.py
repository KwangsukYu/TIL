n = int(input())

countbox = []
def threeN(num):
    if num == 1:
        countbox.append(1)
        return len(countbox)
    
    if num % 2 == 0:
        countbox.append(num)
        return threeN(int(num/2))
    else:
        countbox.append(num)
        return threeN(num*3+1)

print(threeN(n))