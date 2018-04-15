usd = 57
euro = 60
mnt = 38
jpy = 1.75

money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 400, евро - 401, тугрик - 402, йен - 403): "))

if currency == 400:
    cache = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cache = round(money / euro, 2)
    print("Валюта: евро")
elif currency == 402:
    cache = round(money / mnt, 2)
    print("Валюта: тугрик")
elif currency == 403:
    cache = round(money / jpy, 2)
    print("Валюта: йен")
else:
    cache = 0
    print("Неизвестная валюта")

print("К получению:", cache)