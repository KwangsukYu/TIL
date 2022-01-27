word = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in croa:
    if i in word:
        a = word.replace(i, 'a')
        word = a

print(len(word))