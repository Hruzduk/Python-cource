lst_1 = []

for i in range(3):
    number = int(input())
    lst_1.append(number)

file = open('file.txt', 'w')

for index, number in enumerate(lst_1):
    file.write(str(index) + " " + str(number) + '\n')

# file.writelines([str(item) for item in lst_1])

file.close()