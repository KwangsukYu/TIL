beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
print(f'{beer}            # 인상 전')
for name, price in beer.items():
    beer[name] = price*1.05

print(f'{beer}  # 인상 후')