# запрашиваем вводніе данніе
p = float(input("Какую сумму Вы внесли в начале?  "))
r_1 = float(input("Под какой годовой процент Вы создали депозит?  "))
n = int(input("Какая частота начисления ежегодного дохода в год? *ежемесячно - 12, а ежеквартально - 4 "))
t = int(input("За сколько лет сделать просчет? "))

# конвертация в дроби
r_2 = r_1 / 100

# проводим прочет алгоритма
a = p * ((1 + (r_2 / n))) ** (n * t)

# вывод результатов
print(f'По истечению указанного времени на Вашем счету будет сумма в {a: .1f} попугая')