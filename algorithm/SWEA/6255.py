data = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}
price = []
for value in data.values():
    price.append(value)

set_price = sorted(price, reverse=True)

for i in set_price:
    for j in data:
        if i == data[j]:
            print(f'{j}: {data[j]}')
