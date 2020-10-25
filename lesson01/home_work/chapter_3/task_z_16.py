year = int(input("Введите год:  "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} высокосный и в феврале 29 дней")
elif year % 100 != 0 and year % 4 == 0:
    print(f"{year} высокосный и в феврале 29 дней")
else:
    print("Этот гон не высокосный и нем в феврале 28 дней")
