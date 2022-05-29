menu_a = 2000; menu_b = 2000

for i in range(5):
    menu = int(input())
    if i < 3:
        if menu < menu_a:
            menu_a = menu
    else:
        if menu < menu_b:
            menu_b = menu

print(menu_a + menu_b - 50)
