data_path = '../../data/'  # прописываем путь к папке с файлами

# создаем переменную с названиеями файлов для дальнейшей обработки
file_names = ['april.csv', 'february.csv', 'march.csv']

# создаем пустые списки с искомыми значениями для каждого отдельного периода
min_total = []
max_total = []
mean_total = []

# пишем цикл для обработки каждого файла из списка файлов
for file_name in file_names:
    # путь и название файла в переменную
    file_path = data_path + file_name
    # открываем файл и записываем его в переменную
    file = open(file_path, 'r', encoding='utf8')
    # создаем список с строк читаемого файла
    file_lst = file.readlines()
    salary_lst = []
    # убераем первую строку с обработки из-за того что там только строковые значения
    # ВНИМАНИЕ НА ЕНУМЕРЕЙТ ЙОПТА! Получаем индекс строки и убераем ее с обработки если она нуевая (первая)
    for index, line in enumerate(file_lst):
        if index == 0:
            continue
        # разбиваем строку на элементы по запятой и записываем их в список для обработки
        lst = line.split(',')
        # выбераем именно 4ю колонку с ЗП, округляем и записываем в переменную, добавляем в новый список с ЗП
        salary = round(float(lst[3]), 2)
        salary_lst.append(salary)
    # ищем искомые значения для каждого периода пока идем по фору и записываем их в отдельные списки
    min_sal = min(salary_lst)
    min_total.append(min_sal)
    max_sal = max(salary_lst)
    max_total.append(max_sal)
    mean = sum(salary_lst) / len(salary_lst)
    mean_total.append(mean)
    # Закрываем файл
    file.close()

print(min_total)
print(max_total)
print(mean_total)

# Ищем искомые значения для всего периода на основании ранее найденных списков
min_total_val = min(min_total)
max_total_val = max(max_total)
mean_total_val = sum(mean_total) / len(mean_total)

print('Мы получили данные за весь периаод: ', min_total_val, max_total_val, mean_total_val, sep='\n')
