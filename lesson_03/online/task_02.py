num_1 = int(input('Введите число '))
num_2 = int(input('Введите число '))
num_3 = int(input('Введите число '))
num_4 = int(input('Введите число '))
num_5 = int(input('Введите число '))
num_6 = int(input('Введите число '))
num_7 = int(input('Введите число '))
num_8 = int(input('Введите число '))
num_9 = int(input('Введите число '))
num_10 = int(input('Введите число '))

lst_1 = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]
lst_2 = []
for i in enumerate(lst_1):
    if i % 2 != 0:
        lst_2.append(i)
print(lst_2)


