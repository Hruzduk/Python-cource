# делаем запрос на ввод номера кармана
carman = int(input('Введите номер кармана от 0 до 36  '))

# прописываем систему причинно-следственной связи
if carman < 0 or carman > 36:
    print("Вы ввели не коректное начение")
elif 1 <= carman <= 10 and carman % 2 != 0:
    print("Цвет кармана красный")
elif 1 <= carman <= 10 and carman % 2 == 0:
    print("Цвет кармана черный")
elif 11 <= carman <= 18 and carman % 2 != 0:
    print("Цвет кармана черный")
elif 11 <= carman <= 18 and carman % 2 == 0:
    print("Цвет кармана красный")
elif 19 <= carman <= 28 and carman % 2 != 0:
    print("Цвет кармана красный")
elif 19 <= carman <= 28 and carman % 2 == 0:
    print("Цвет кармана черный")
elif 29 <= carman <= 36 and carman % 2 != 0:
    print("Цвет кармана черный")
elif 29 <= carman <= 36 and carman % 2 == 0:
    print("Цвет кармана красный")