a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

menu_list = []
for i in a:
    menu_list.append(i)
for j in b:
    menu_list.append(j)

set_menu_list = set(menu_list)

new_menu = {}
for k in set_menu_list:
    if k in a:
        new_menu[k] = a.get(k)
    elif k in b:
        new_menu[k] = b.get(k)

menu_3000 = []
price_3000 = []

for menu, price in new_menu.items():
    if price >= 3000:
        menu_3000.append(menu)
        price_3000.append(price)
result = set(zip(menu_3000, price_3000))
print(result)