list = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = ascending[::-1]

if list == ascending :
    print('ascending')
elif list == descending :
    print('descending')
else :
    print('mixed')
