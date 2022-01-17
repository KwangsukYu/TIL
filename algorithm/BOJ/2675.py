n = int(input())

for i in range(n) :
    N, word = input().split()
    N = int(N)
    word = str(word)
    for j in range(len(word)) :
        print(N*word[j],end='')
    print()

