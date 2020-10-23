weight = float(input("Укажите свой вес в килограимах:  "))
hight = float(input("Укажите свой рост в метрах:  "))

index = weight / hight

if 18.5 <= index <= 25:
    print(f"Ваш индекс массы тела составляем {index: .1f} и это оптимальное значение")
elif index < 18.5:
    print(f"Ваш индекс массы тела составляем {index: .1f} и это ниже нормы")
elif index > 25:
    print(f"Ваш индекс массы тела составляем {index: .1f} и это выше нормы")
