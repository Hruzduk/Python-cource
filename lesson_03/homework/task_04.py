numbers = 20
lst = [0] * numbers

for i in range(numbers):
    print("Input number ", i +1, ':')
    lst[i] = float(input())

little = min(lst)
maxim = max(lst)
summa = sum(lst)
averega = summa / len(lst)

print(f'Вы ввели: {lst}')
print(f'Максимальное значение: {maxim}')
print(f'Минимальное значение: {little}')
print(f'Среднее арифметическое значение: {averega}')