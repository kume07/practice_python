import random
import string

length = int(input("Введіть довжину пароля: "))

# Символи для пароля: великі та малі літери, цифри, спецсимволи
characters = string.ascii_letters + string.digits + string.punctuation

# Генерація випадкового пароля
password = ''.join(random.choice(characters) for i in range(length))

print("Ваш згенерований пароль:", password)
