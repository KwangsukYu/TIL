n, k = input().split()

def jinsu_changer(num, jinsu):
    jinsu_list = '0123456789ABCDEF'
    if num < jinsu:
        return str(jinsu_list[num])
    else: 
        return jinsu_changer(int(num/jinsu), jinsu) + jinsu_changer(int(num % jinsu), jinsu)


print(jinsu_changer(int(n), int(k)))