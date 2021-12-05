#clear en Linux
#cls en Windows (nt)

import os

print('hola')
print('chau')
print('que tal')
print('adios')
#if os.name == 'nt':
#    os.system('cls')
#else:
#    os.system('clear')
os.system('cls' if os.name == 'nt' else 'clear')
a = 1
print('hola' if a == 1 else 'chau')