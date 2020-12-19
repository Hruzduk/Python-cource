if __name__ == '__main__':

    # формируем словарь через соотвецтвия числово и строкового значения месяца
    dist = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
            '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
            '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
    # запрос данных
    date = input('Введите дату в формате: дд/мм/гггг: ')
    # разбиваем по разделителю и формируем список
    lst = date.split('/')
    # вводим переменную с сылкой по месяцу
    a = lst[1]
    # проверяем коректность значения месяца и его наличие в словаре с дальнейшим воводом
    if a in dist.keys():
        print(lst[0], dist[a], lst[2])
    else:
        print("Вы ввели не верное значение")