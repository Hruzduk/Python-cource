sos = 10
bread = 8

# запрашиваем колличесво учасников пикника и желаемых хот-догов
people = int(input("Сколько людей Вы ожидаете?  "))
hot_dog = int(input("По сколько хот-догов нужно приготовить? "))

# высчитываем упаковк и остатки
sum_hot_dog = people * hot_dog

upak_sos = sum_hot_dog // sos
upak_bread = sum_hot_dog // bread
ost_sos = sum_hot_dog % sos
ost_bread = sum_hot_dog % bread

if sum_hot_dog == 0:
    print("Вам не нужно покупать продукты")
else:
    print("Вам нужно ", upak_sos, 'упаковок сосисок')
    print(upak_bread, 'упаковок буловек.')
print("Так же у Вас останется лишних", ost_sos, "сосисок и ", ost_bread, "булок")
