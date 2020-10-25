central_pizza = str('"Центральная пицерия"')
coffee = str('"Кофе за углом"')
italian = str('"Блюда от итальянской мамы"')
kitchen = str('"Кухня шеф-повара"')

print("Пожалуйста, ответье будут ли на ужине (да / нет):  ")
vegetarians = str(input("Вегетарианци?  "))
vegans = str(input("Веганы?  "))
out_gluten = str(input("Приверженци безглютеновой диеты? "))

if vegetarians == str("нет") and vegans == str("нет") and out_gluten == str("нет"):
    print(f'{central_pizza}, {coffee}, {italian}, {kitchen} и "Изысканные гамбургеры от Джо"')
else:
    if vegetarians == str("да") and vegans == str("да") and out_gluten == str("да"):
        print(f'{coffee} "и" {kitchen}')
        if vegetarians == str("да") and vegans == str("нет") and out_gluten == str("нет"):
            print(f'{italian}')
            if vegetarians == str("да") and vegans == str("нет") and out_gluten == str("да"):
                print(f'{central_pizza}')

# изрядно высушило мозг