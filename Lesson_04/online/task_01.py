# имя файла
FILENAME = "messages.txt"
# определяем пустой список
messages = list()

for i in range(6):
    message = input("Введите строку " + str(i + 1) + ": ")
    messages.append(message + "\n")

# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)


print("Считанные сообщения")
new_lst = []
with open(FILENAME, "r") as file:
    content = file.read()
    print(content)
new_lst = content
# print(new_lst)

