
if __name__ == '__main__':
    # запрашиваем строковые значения у пользователя
    date = input('Введите дату в формате: дд/мм/гггг: ')

    # разбиваем строковое значение по разделителю и записываем в список
    lst = date.split('/')

    # проходимся по списку для сравнения второго елемента и присвоения его переменной month
    
    if lst[1] == '01':
        month = 'января'
        print(lst[0],  month, lst[2])
    elif lst[1] == '02':
        month = 'февраля'
        print(lst[0], month, lst[2])
    elif lst[1] == '03':
        month = 'марта'
        print(lst[0], month, lst[2])
    elif lst[1] == '04':
        month = 'апреля'
        print(lst[0], month, lst[2])
    elif lst[1] == '05':
        month = 'мая'
        print(lst[0], month, lst[2])
    elif lst[1] == '06':
        month = 'июня'
        print(lst[0], month, lst[2])
    elif lst[1] == '07':
        month = 'июля'
        print(lst[0], month, lst[2])
    elif lst[1] == '08':
        month = 'августа'
        print(lst[0], month, lst[2])
    elif lst[1] == '09':
        month = 'сентября'
        print(lst[0], month, lst[2])
    elif lst[1] == '10':
        month = 'октября'
        print(lst[0], month, lst[2])
    elif lst[1] == '11':
        month = 'ноября'
        print(lst[0], month, lst[2])
    elif lst[1] == '12':
        month = 'декабря'
        print(lst[0], month, lst[2])
    else:
        print("incorrect value")