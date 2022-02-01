x = int(input())

sum = 0
n = 0
while sum < x:
    n += 1
    sum += n
a = x - sum + n

if n % 2:
    bunja = n - a + 1
    bunmo = a
else:
    bunja = a
    bunmo = n - a + 1
print(f'{bunja}/{bunmo}')
