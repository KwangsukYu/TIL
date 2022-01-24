N = input()

number = int(N)
count = 0

if number < 10:
    number = '0' + str(number)
    count += 1

else :
    number = number//10 + number%10
    count += 1


while number == int(N):
    if int(number) < 10:
        number%10 + number
        count += 1
        if number == int(N):
            break
    else:
        number%10 + number//10
        count += 1
        if number == int(N):
            break

print(count)