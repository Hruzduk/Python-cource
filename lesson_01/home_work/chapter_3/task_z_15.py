# запрашивает колличество секунд
second = int(input("Ведите колличесво секунд:  "))

# выставляем стандартизацию
minute = 60
hour = 3600
day = 86400

# строим последовотельность
if second < 60:
    print(f"Так и будет {second} секунд")
elif 60 <= second < 3600:
    print(f"{second // minute} минут и {second % minute} секунд")
elif 3600 <= second < 86400:
    print(f"{second//hour} часов {(second % hour) // minute} минут "
          f"и {((second % hour) // minute) % minute} секунд")
elif second >= 86400:
    print(f"{second // day} дней {(second % day) // hour} часов "
          f"{(second % hour) // minute} минут и {second % minute} секунд")


