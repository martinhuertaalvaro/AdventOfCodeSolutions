from collections import Counter

l = []
r = []

# Leer el archivo
with open('day1.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        numeros = linea.strip().split()
        
        if len(numeros) == 2:
            l.append(int(numeros[0]))
            r.append(int(numeros[1]))

conteo_l = Counter(l)
conteo_r = Counter(r)
total = 0

for i in range(len(l)):
    total += l[i] * conteo_r.get(l[i], 0)

    
print(total)