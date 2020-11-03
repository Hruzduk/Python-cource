month = 12

lst = [0] * month

for index in range(month):
    print('Введите количество осадков за месяц ', index + 1, ': ')
    lst[index] = float(input())

sum = sum(lst)
avarage = sum / len(lst)
maximum = max(lst)
minimum = min(lst)
print(f'Всего за год выпало: {sum:.2f} осадков')
print(f'Среднемесячный уровень осадков составил: {avarage:.2f}')
print(f'Максимальный уровень осадков составил: {maximum:.2f}')
print(f'Минимальный уровень осадков составил:{minimum:.2f}')
