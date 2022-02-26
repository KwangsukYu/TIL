while True:
    T = input()
    if T == '0': break
    print('yes' if T == T[::-1] else 'no')