mi_variable = 'Franco'
print(mi_variable)


for n in range(1,10):
    print(n)

print('')

m = 1
while (m < 10):
    print(m)
    m += 1

print('')


estaciones = ('verano', 'otoño', 'invierno', 'primavera')
for estacion in estaciones:
    print(estacion)

print('')

for indice,epoca in enumerate(estaciones):
    print('Estamos en ',epoca,' que es representada por el numero ',(indice+1))


print('')

for n in range(1,10):
    print(n)
    if (n == 5):
        break

print('Se termina el bucle cuando llega al break')

for n in range(1,10):
    if (n == 5):
        continue
    print(n)

print('Ignoro la vuelva del bucle')