import re

print("Родина София, КМ-94. Завдання №1 - Обчислення суми арифметичної прогресії в залежності від значення змінної")

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

running = True
while True:
    N = do_input_float("Введіть значення змінної: ")
    K = N/3
    if K % N == 0 :
        print (K//N+1)
        print ("Введення недопустиме")
        running = False
    else:
        print (int(K+1))
        print ("Обчислення закінчене")
