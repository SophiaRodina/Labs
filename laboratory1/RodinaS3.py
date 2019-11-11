import math
import re

print ("Родина София, КМ-94. Завдання №1 - Обчислення значення функції в залежності від значення змінної")

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

x = do_input_float("Введіть значення змінної: ")
if x <= 3:
    print(x**2 + 3*x + 9)
else:
    print(math.sin(x) / (x**2-9))
