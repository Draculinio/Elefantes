import time
import os
import random

def fibo(n):
    if n<0:
        raise ValueError('Solo nrs positivos')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        nm1 = 1
        nm2 = 0
        for i in range(2,n):
            sum = nm1 + nm2
            nm2 = nm1
            nm1 = sum
        return nm1
term = 0
colores = ['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[37m','\033[90m','\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m']
reset='\033[0m'
while True:
    os.system("clear")
    print('{}Calculando nrs de la serie de Fibonacci!!!!!{}'.format(random.choice(colores),reset))
    start = time.time()
    f = fibo(term)
    end = time.time()
    total_time = end - start
    print(random.choice(colores)+r"""
                   ____
                 () _  \
                    |__ \
                   /_____\
   SUSCRIBANSE     \o o)\)_______
        A          (<  ) /#######\
    DRACULINIO   __{'~` }#########|
                /  (   _}_/########|
               /   {  / _|#/ )####|
              /   \_~/ /_ \  |####|
             \______\/  \ | |####|
              \__________\|/#####|
            snd |__[X]_____/ \###/ 
                /___________\
                 |    |/    |
                 |___/ |___/
                _|   /_|   /
               (___,_(___,_)
    """+reset)
    print('{} FELIZ NAVIDAD Les desea su amigo Draculinio!!!!{}'.format(random.choice(colores),reset))
    print('{}TERMINO {}{}'.format(random.choice(colores),term,reset))
    print('{}Numero {}{}'.format(random.choice(colores),f,reset))
    print('{}Tiempo: {}{}'.format(random.choice(colores),total_time,reset))
    file = open('fibo.txt',"w")
    file.write('Termino: {}\n'.format(term))
    file.write('Resultado: {}\n'.format(f))
    file.write('Tiempo: {}\n'.format(total_time))
    file.close()
    term +=1
