# запрос мужского и женского пола
a = int(input('Сколько людей мужского пола? '))
b = int(input('Сколько людей женского пола? '))
c = a + b

d = (a / c) * 100
e = (b / c) * 100
print(f'Мужчин: {d:.1f} процентов')
print(f'Женщин: {e:.1f} процентов')