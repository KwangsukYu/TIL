n = int(input())

def numbers(num):
    if num == 1:
        return f'{1}'
    else:
        return f'{numbers(num - 1)}\n{num}'

print(numbers(n))