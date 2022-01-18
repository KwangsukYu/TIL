list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list2 = [-1] * 26
word = input()

for i in range(26):
    for j in range(len(word)):
        if list1[i] == word[j]:
            list2[i] += 1+j
            break

for l in range(26):
    print(list2[l], end=' ')