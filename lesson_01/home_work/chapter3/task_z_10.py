x = 5
y = 10
z = 50

print("Ваша цель собарть один рубль! ")
first_5 = int(input("Сколько пятикопеечных монет Вы хотите внести? "))
first_10 = int(input("Сколько десятикопеечных монет Вы хотите внести? "))
first_50 = int(input("Сколько пятидесятикопеечных монет Вы хотите внести? "))

summa = (5 * first_5) + (10 * first_10) + (50 * first_50)

if summa == 100:
    print("Великолепно! Вы собрали ровно одио рубль!")
elif summa > 100:
    print("Не верно, Вы собарли больше рубля.")
elif summa < 100:
    print("Не верно, Вы собрали меньше одного рубля.")