import re

print("Родина София, КМ-94. Завдання №1 - Обчислення суми арифметичної прогресії в залежності від значення змінної")

def do_input_int(msg):
    is_good = False
    while not is_good:
        a = input(msg)
        if bool(re.match('^[+]{0,1}[0-9]{1,}$', a)):
            is_good = True
            a = int(a)
        else:
            print("Error. Repeat please")
    return a

def do_input_float(msg):
    is_good = False
    while not is_good:
        a = input(msg)
        if bool(re.match('^[+-]{0,1}[0-9]{1,}(\.[0-9]{1,})?$', a)):
            is_good = True
            a = float(a)
        else:
            print("Error. Repeat please: ")
    return a

x = do_input_float("Введіть значення змінної x : ")
n = do_input_int("Введіть верхню межу додавання n : ")
last = 1
for i in range(1, n+1):
    last *= (x/(2**i))
print(last)
print("Обчислення виконане")
