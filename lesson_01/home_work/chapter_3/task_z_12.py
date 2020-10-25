discount_1 = 0.1
discount_2 = 0.2
discount_3 = 0.3
discount_4 = 0.4
price_1 = 99

items = int(input("Сколько програмных пакетов Вы приобрели?  "))
price_2 = items * price_1

if items <= 0:
    print("Вы купили ни одного програмного пакета")
elif 0 < items < 10:
    print(f"Ваша цена составит, {price_2: .2f} $")
elif 10 <= items <= 19:
    print(f"Ваша цена составит, {(price_2) - ((price_2) * discount_1): .2f}$")
    print(f"Скидка составила {price_2 * discount_1: .2f}$")
elif 20 <= items <= 49:
    print(f"Ваша цена составит, {(price_2) - ((price_2) * discount_2): .2f}$")
    print(f"Скидка составила {price_2 * discount_2: .2f}$")
elif 50 <= items <= 99:
    print(f"Ваша цена составит, {(price_2) - ((price_2) * discount_3): .2f}$")
    print(f"Скидка составила {price_2 * discount_3: .2f}$")
elif items >= 100:
    print(f"Ваша цена составит, {(price_2) - ((price_2) * discount_4): .2f}$")
    print(f"Скидка составила {price_2 * discount_4: .2f}$")
