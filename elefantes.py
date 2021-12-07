import time
import psutil
import os
import random

def elefante(nro,mediciones):
    colores = ['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[37m','\033[90m','\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m']
    reset='\033[0m'
    m = mediciones
    os.system("clear")
    print('{}{} elefantes se balanceaban sobre la tela de una araña...{}'.format(random.choice(colores),nro, reset))
    print(random.choice(colores)+r""" 
                        ____
                   .---'-    \
      .-----------/           \
     /           (         ^  |   __    Draculinio, el canal de los programadores...
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\).
    """+reset)
    print('{}como veian que resistia fueron a llamar a otro elefante...{}'.format(random.choice(colores),reset))
    uso_cpu = psutil.cpu_percent()
    porc_memoria = psutil.virtual_memory()[2]
    uso_mem = psutil.virtual_memory()[3]

    print('\n{}ACTUAL: {}'.format(colores[0],reset))
    print('{}Porcentaje actual de uso de CPU: {}{}'.format(colores[2],reset,uso_cpu))
    print('{}Porc. Memoria: {}{}'.format(colores[2],reset,porc_memoria))
    print('{}Memoria en uso: {}{}'.format(colores[2],reset,uso_mem))

    if uso_cpu > m['max_cpu_percent']:
        print('\n{}-->Record de uso de CPU!{}'.format(colores[5],reset))
        m['max_cpu_percent'] = uso_cpu
        m['it_max_cpu_percent'] = nro
    elif uso_cpu< m['min_cpu_percent']:
        print('\n{}-->Record de uso minimo de CPU! {}'.format(colores[5],reset))
        m['min_cpu_percent'] = uso_cpu
        m['it_min_cpu_percent'] = nro
    if porc_memoria > m['max_memory_perc']:
        print('\n{}-->Record de porcentaje uso maximo de memoria!{}'.format(colores[5],reset))
        m['max_memory_perc'] = porc_memoria
        m['it_max_memory_perc'] = nro
    elif porc_memoria< m['min_memory_perc']:
        print('\n{}-->Record de porcentaje uso maximo de memoria!{}'.format(colores[5],reset))
        m['min_memory_perc'] = porc_memoria
        m['it_min_memory_perc'] = nro
    if uso_mem > mediciones['max_memory_use']:
        print('\n{}-->Record de uso maximo de memoria!{}'.format(colores[5],reset))
        m['max_memory_use'] = uso_mem
        m['it_max_memory_use'] = nro
    elif uso_mem< m['min_memory_use']:
        print('\n{}-->Record de uso minimo de memoria!{}'.format(colores[5],reset))
        m['min_memory_use'] = uso_mem
        m['it_min_memory_use'] = nro
    m['sum_cpu_percent']+=uso_cpu
    m['sum_mem_percent']+=porc_memoria
    print('\n{}HISTORICO: {}'.format(colores[0],reset))
    print('{}Porcentaje MAXIMO de uso de CPU: {}{} (Elefantes: {})'.format(colores[12],reset,m['max_cpu_percent'],m['it_max_cpu_percent']))
    print('{}Promedio uso CPU: {}{}'.format(colores[11],reset,m['sum_cpu_percent']/nro))
    print('{}Porcentaje MINIMO de uso de CPU: {}{} (Elefantes: {})'.format(colores[12],reset,m['min_cpu_percent'],m['it_min_cpu_percent']))
    print('{}Porcentaje MAXIMO de memoria usada: {}{} (Elefantes: {})'.format(colores[12],reset,m['max_memory_perc'], m['it_max_memory_perc']))
    print('{}Promedio uso Memoria: {}{}'.format(colores[11],reset,m['sum_mem_percent']/nro))
    print('{}Porcentaje MINIMO de memoria usada: {}{} (Elefantes: {})'.format(colores[12],reset,m['min_memory_perc'], m['it_min_memory_perc']))
    print('{}Uso MAXIMO de memoria: {}{} (Elefantes: {})'.format(colores[12],reset,m['max_memory_use'],m['it_max_memory_use']))
    print('{}Uso MINIMO de memoria usada: {}{} (Elefantes: {})'.format(colores[12],reset,m['min_memory_use'],m['it_min_memory_use']))
    if nro%50==0:
        print('          {}SUSCRIBANSE AL CANAL!!!!!!!!!!!!{}'.format(colores[5],reset))
        print('           {}SUSCRIBANSE AL CANAL!!!!!!!!!!!!{}'.format(colores[0],reset))
        print('            {}SUSCRIBANSE AL CANAL!!!!!!!!!!!!{}'.format(colores[1],reset))
        #time.sleep(5)
    #time.sleep(1)
    #elefante_recursivo(nro+1, m)
    return m

mediciones = {
    'it_max_cpu_percent': 0,
    'max_cpu_percent' : 0.0,
    'it_min_cpu_percent': 0,
    'min_cpu_percent' : 9999999999.99,
    'it_max_memory_perc': 0,
    'max_memory_perc' : 0.0,
    'it_min_memory_perc': 0,
    'min_memory_perc' : 100.0,
    'it_max_memory_use': 0,
    'max_memory_use' : 0,
    'it_min_memory_use': 0,
    'min_memory_use' : 999999999999999999999999999999999,
    'sum_cpu_percent':0,
    'sum_mem_percent':0
    }

nro = 1
while True:
    mediciones = elefante(nro, mediciones)
    nro+=1