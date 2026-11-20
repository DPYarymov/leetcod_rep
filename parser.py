# Парсер
import os
import time

spisok = []
for adres, dirs, files in os.walk('C:\\programming\\Test'):
    for file in files:
        full = os.path.join(adres, file)
        if 'plane' in full:
        #        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)
print(spisok)
