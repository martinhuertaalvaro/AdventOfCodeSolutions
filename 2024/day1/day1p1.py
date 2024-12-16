l = []
r = []

# Leer el archivo
with open('day1.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        numeros = linea.strip().split()
        
        if len(numeros) == 2:
            l.append(int(numeros[0]))
            r.append(int(numeros[1]))
l.sort()
r.sort()

total = 0
for i in range(len(l)):
    total += (abs(l[i]-r[i]))

print(total)