# вводим колличесво итераций цикла и переменную суммы багов
days = 5
sum = 0
# запрашиваем колличесво ошибок за каждый день и прописываем цикл for
for i in range(days):
    errors = int(input("How many bugs in day?  "))
    sum = sum + errors
print("You have ", sum, "bugs")

