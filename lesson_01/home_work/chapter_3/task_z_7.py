# Запрашиваем введение 2х цветов для смешивания
print("Основные цвета: красный, синий и желтый. Выберите два")
color_name_1 = str(input("Введите первый основной цвет: "))
color_name_2 = str(input("Введите второй основной цвет: "))

# Проводим сравнение и строим цепочку
if color_name_1 == str("красный") and color_name_2 == str('желтый'):
    print("Вторичный цвет - оранжевый")
elif color_name_1 == str("желтый") and color_name_2 == str('красный'):
    print("Вторичный цвет - оранжевый")
elif color_name_1 ==str("красный") and color_name_2 == str("синий"):
    print("Вторичный цвет - фиолетовый")
elif color_name_1 ==str("синий") and color_name_2 == str("красный"):
    print("Вторичный цвет - фиолетовый")
elif color_name_1 ==str("синий") and color_name_2 == str("желтый"):
    print("Вторичный цвет - зеленый")
elif color_name_1 ==str("желтый") and color_name_2 == str("синий"):
    print("Вторичный цвет - зеленый")
else:
    print("Вы ввели не коректное значение основного цвета")