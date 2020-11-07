# todo

import random


def main():
    lst = [random.randint(0, 9) for i in range(7)]
    print(lst)

    lst_2 = []
    n = float(input("Input n  "))
    # lst_2 = [item for item in lst if item > n]
    for item in range(len(lst)):
        if n < lst[item] > 0:
            lst_2.append(lst[item])
    print(lst_2)



main()