lst = [1, 2, 3]

string = "some text"

some_int = 1

some_float = 2.3

# print(type(some_int), some_int)
# print(type(lst), lst)
# print(type(some_float), some_float)
# print(type(string), string)

lst1 = [string, some_int, some_float]

# print(len(string))

# for item in lst1:
#     print(item)

# for i in range(len(lst1)):
#     print(i, lst1[i])


# print(list(range(3)))


sum = 0

# for item in lst:
#     sum += item
#
# print(sum)
#
# lst = [1, 2, 3]

for item in lst1:
    print(item)
#
# for item in range(len(lst1)):
#     print(item)
#     # item = item * item

# print(lst)
#
# for index in [0, 1, 2]:  # range(3) == [0, 1, 2]
#     print(index)
#     # lst[index] = lst[index] ** 2
#
# print(lst)

print(lst)

total = 0
sum = 0

for index, item in enumerate(lst):
    lst[index] = item * item
    total = total + 1
    sum = sum + lst[index]

# print(lst)
# print(total)
# print(sum)



sum = 0
counter = 0

while sum > -1:
    sum = sum + 2

    counter += 1

    if counter == 100:
        break


print(sum)