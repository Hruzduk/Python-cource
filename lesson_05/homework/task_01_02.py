if __name__ == '__main__':
    # получаем строковое значение
    row = input("Введите ряд однозначных произвольных чисел: ")

    # формируем пустой список для дальнейшей работы с ним
    lst = []
    # проходимся фором по строке
    for i in row:
        number = i
        # переводим строковое значение в числовое и добавляем в список
        numbers = int(number)
        lst.append(numbers)
    # считаем сумму числе в списке
    summa = sum(lst)

    print(summa)