# Запрашиваем сумму каждого товара и присваиваем ему переменную
a = float(input('Пожалуйста, введите сумму первого товара:  '))
b = float(input('Пожалуйста, введите сумму второго товара:  '))
c = float(input('Пожалуйста, введите сумму третьего товара:  '))
d = float(input('Пожалуйста, введите сумму четвертого товара:  '))
e = float(input('Пожалуйста, введите сумму пятого товара:  '))

# Вычисляем накопительну стоимость
total = a + b + c + d + e

# Вычитаем налог в 7%
discont = total * 0.07

# Итоговая сумма
items = total + discont

# Выводим полученные данные
print(f'Сумма ваших товаров состаляет: {total: .2f}')
print(f'Сумма налога состаляет: {discont: .2f}')
print(f'К оплате: {items: .2f}')