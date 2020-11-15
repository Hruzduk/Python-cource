import os  # Импортируем библиотеку для работы с файлами (копирование, удаление и тд)
import pandas # библиотека для работы с табличными данными (csv, excel)

data_path = '../../data/'   # Указываем путь к файлам в репозитории

min_lst, max_lst, mean_lst = [], [], []   # создаем три списка для дальнейшей записи в них
# искомых данных и вывода на дисплей

for file in os.listdir(data_path):     # проходимся по списку всех файлов в указанной папке
    data_file = pandas.read_csv(data_path + file)  # считываем файл из указанной папки и записываем его в переменную
    min_val = round(data_file['Оплата по окладу'].min(), 2)  # выбираем нужную область (колонку) в файле и
    # считываем минимальное значение, округляем его и записываем в переменную
    max_val = round(data_file['Оплата по окладу'].max(), 2)  # аналогично
    mean_val = round(data_file['Оплата по окладу'].mean(), 2) # аналогично
    min_lst.append(min_val)
    max_lst.append(max_val)
    mean_lst.append(mean_val)
# добавляем переменных в созданные списки и выводим данные на экран
print(min_lst)
print(max_lst)
print(mean_lst)
