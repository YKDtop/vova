try:
    numerator = 10
    donominator = 0
    result = numerator / donominator
except ZeroDivisionError:
    print ("Помилка: Ділення на нуль!")
else:
    print(f"Результат: {result}")