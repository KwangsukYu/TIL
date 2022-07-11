t = list(input())

for i in range(len(t)):
    if t[i].isupper():
        t[i] = t[i].lower()
    else:
        t[i] = t[i].upper()

print(''.join(t))