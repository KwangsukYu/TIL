n = int(input())

def numbers(num):
    if num == 1:
        return f'{1}'
    else:
        return f'{num}\n{numbers(num - 1)}'

print(numbers(n))