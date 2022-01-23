fruit = ['   apple    ','banana','  melon']

result = {}
for i in fruit:
    result[i.strip()] = len(i.strip())
print(result)