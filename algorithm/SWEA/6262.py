word = input()

word_dict = {}

for i in word:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] += 1

for key, value in word_dict.items():
    print(f'{key},{value}')