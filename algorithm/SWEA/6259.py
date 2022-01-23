sentence = input()

count_dict = {
    'LETTERS' : 0,
    'DIGITS' : 0
}

for i in sentence:
    if 'a' <= i <= 'z':
        count_dict['LETTERS'] += 1
    elif 'A' <= i <= 'Z':
        count_dict['LETTERS'] += 1
    elif i in list(map(str, (range(1,10)))):
        count_dict['DIGITS'] += 1

for k, v in count_dict.items():
    print(k, v)

