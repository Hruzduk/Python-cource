months = 12

lst = [0.] * months

min_val, min_month = 0, 0
max_val, max_month = 0, 0

for month in range(1, months + 1):
    print('Введите количество осадков за месяц ', month, ': ')
    val = float(input())
    lst[month] = val
    if val < min_val != 0:
        min_val = val
        min_month = month
    elif val > max_val:
        max_val = val
        max_month = month


sum = sum(lst)
average = sum / len(lst)
# maximum = max(lst)
# minimum = min(lst)
print(f'Всего за год выпало: {sum:.2f} осадков')
print(f'Среднемесячный уровень осадков составил: {average:.2f}')
print(f'Максимальный уровень осадков в {max_month} месяце и он составил: {max_val:.2f}')
print(f'Минимальный уровень осадков в {min_month} месяце и он составил:{min_val:.2f}')
