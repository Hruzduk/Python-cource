# запрос пройденого пути и потраченого топлива
large = float(input('Введите пройденое растояние в километраж, пожалуйста: '))
bac = float(input('Введите колличество затраченых литорв: '))

# вычитаем расход
lit = large /   bac

# выводим данные
print(f'Ваш расход составил: {lit: .1f}')