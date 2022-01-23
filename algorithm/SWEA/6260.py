sentence = input()

count_dict = {
    'UPPER CASE' : 0,
    'LOWER CASE' : 0
}

for i in sentence:
    if 'a' <= i <= 'z':
        count_dict['LOWER CASE'] += 1
    elif 'A' <= i <= 'Z':
        count_dict['UPPER CASE'] += 1


for k, v in count_dict.items():
    print(k, v)