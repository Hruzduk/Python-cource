# запрашиваем величину покупки
items = float(input('Введите сумму покупки, пожалуйста:  '))

# вычисляем федеральный налог в 5%
# и региональный в 2,5%
goverment_1 = (items * 0.05)
goverment_2 = (items * 0.025)

# общий налог с продаж
goverment_3 = goverment_1 + goverment_2

# общая сумма покупки
total_price = goverment_3 + items

# выводим на экран с округлением до 2х знаков
print(f'Федеральный налог: {goverment_1: .2f}')
print(f'Региональный налог: {goverment_2: .2f}')
print(f'Общая сумма налога: {goverment_3: .2f}')
print(f'Итоговая сумма к оплате: {total_price: .2f}')
