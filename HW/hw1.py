# 1.1
# 1) Установите Python и PyCharm

# 2) Напишите и запустите программу.которая выводит строку "Hello world!"
# print("Hello world!")

# 3) Напишите программу, которая на входе получает имя пользователя, сохраняет его в переменную
# user_name и выводит строку "Hello {user_name}!"
# name = input("Введите ваше имя: ")
# print(f"Hello, {name}")

# 4) Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую
# операцию(на ваше усмотрение), и выводит “Результат = {результат}”.
# number1 = int(input("Введите первое слагаемое: "))
# number2 = int(input("Введите второе слагаемое: "))
# print(f"Результат = {number1 + number2}")

# 1.2
# 1) Напишите программу, чтобы вывести:
# *********
# *       *
# *       *
# *********
# 1)
# a = "*********"
# b = "*       *"
# print(a)
# print(b)
# print(b)
# print(a)
# 2)
# print("""
# *********
# *       *
# *       *
# *********
# """)
# 3)
# number = int(input("Введите сторону квадрата: "))
# print(number * "  *")
# print((("  *" + (number - 2) * "   " + "  *\n") * (number - 2)) + number * "  *")

# 1.3. **
# Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
# Пример:
# Input: 3498
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8
# number = int(input("Введите четырёхзначное число: "))
# thousands = number // 1000
# hundreds = number % 1000 // 100
# dozens = number % 100 // 10
# units = number % 10
# print("Тысячи - " + str(thousands))
# print("Сотни - " + str(hundreds))
# print("Десятки - " + str(dozens))
# print("Единицы - " + str(units))