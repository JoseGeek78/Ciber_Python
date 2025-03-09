# El primero argmento es el archivo y el segundo el número de copias. ['gusano.py', '2']

import  shutil
import sys

if len(sys.argv) == 2:
    for num in range(0, int(sys.argv[1])):
        shutil.copy()