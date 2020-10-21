# 48 = 1.5 * sugar
# 48 = 1 * butter
# 48 = 2.75 * powder

x = int(input('Сколько булочек Вы хотите испечь? '))
cakes_num = 48

sugar = 1.5 * x / cakes_num
butter = 1 * x / cakes_num
powder = 2.75 * x / cakes_num

print(f"для {x} булок нужно:")
print(f"{sugar: .2f} стакана сахара")
print(f"{butter: .2f} стакана масла")
print(f"{powder: .2f} стакана муки")