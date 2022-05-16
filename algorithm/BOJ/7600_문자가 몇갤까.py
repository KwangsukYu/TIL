from msilib import text


while True:
    t = input()
    if t == '#':
        break
    
    lower_t = t.lower()
    text_set = set()
    for i in range(len(lower_t)):
        if lower_t[i].isalpha() and ord(lower_t[i]) not in text_set:
            text_set.add(ord(lower_t[i]))
    
    print(len(text_set))
    