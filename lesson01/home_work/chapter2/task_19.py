# запрос стоимости еды
price = float(input('Введите стоимость блюда с меню, пожалуйста: '))

# вычитаем размер чаевых - 18%
# вычитаем стоимость налога от продажи - 7%
tea = price * 0.18
gov = price * 0.07

# просчитываем итоговую стоимость и выводим данные
total = price + tea + gov
print(f'чаевые: {tea: .1f}')
print(f'налог: {gov: .1f}')
print(f'Всего: {total: .1f}')