def is_palindrome(t):
    global flag

    def is_pseudo(t):
        if t == t[::-1]:
            return True
        else:
            return False
    
    i = 0
    j = len(t) - 1

    while i < j:
        if t[i] != t[j]:
            if abs(i-j) > 1:
                case_1 = is_pseudo(t[i:j])
                print(t[i:j-1])
                print(t[i:j])
                case_2 = is_pseudo(t[i+1:j+1])
                print(t[i+1:j])
                print(t[i+1:j+1])

                if case_1 and flag:
                    j -= 1
                    flag = False
                elif case_2 and flag:
                    i += 1
                    flag = False
                else:
                    print(2)
                    return
            else:
                print(2)
                return
                
        i += 1
        j -= 1
    
    if flag:
        print(0)
        return
    else:
        print(1)
        return


# 인풋
N = int(input())

for i in range(N):
    flag = True
    text = input()
    is_palindrome(text)

