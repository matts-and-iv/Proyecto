# PROBLEMA 1
"""
Descripción del ejercicio:

    El objetivo es que los estudiantes usen un ciclo for para imprimir los números del 1 al 10.
    Instrucciones para los estudiantes:
    Usa un ciclo for para recorrer un rango de números.
    Imprime cada número en una nueva línea.
"""

#  Implemente su solución acá
for e in range(1,11):
    print(e)


# PROBLEMA 2
"""
Descripción del ejercicio:

El objetivo es que los estudiantes usen un ciclo for para recorrer una lista de nombres e imprimir cada uno de ellos.
Instrucciones para los estudiantes:

    Crea una lista con varios nombres.
    Usa un ciclo for para recorrer la lista.
    Imprime cada nombre en una nueva línea.
"""
#  Implemente su solución acá
nombres = ["Sancho", "Chiquitín", "Jacky", "SamZ"]
for j in nombres:
    print(j)

# PROBLEMA 3
"""
Descripción del ejercicio:

El objetivo es que los estudiantes generen una secuencia de números (por ejemplo, los números pares del 2 al 20) utilizando un ciclo for.
Instrucciones para los estudiantes:

    Usa un ciclo for para generar los números pares del 2 al 20.
    Imprime cada número en una nueva línea.
"""
#  Implemente su solución acá
for e in range(21):
    if(e%2==0):
        print(e)


# PROBLEMA 4
"""
Descripción del ejercicio:

El objetivo es que los estudiantes utilicen un ciclo while para imprimir los números del 1 al 10.
Instrucciones para los estudiantes:

    Define una variable inicializada en 1.
    Usa un ciclo while que continúe hasta que la variable sea mayor que 10.
    Imprime la variable en cada iteración y luego incrementa su valor.
"""
#  Implemente su solución acá
count = 1
while(count<=10):
    print(count)
    count += 1



# PROBLEMA 5
"""
# Simulación de un do-while en Python
numero = 0

while True:
    numero = int(input("Ingresa un número mayor que 0: "))
    if numero > 0:
        break  # Si la condición se cumple, salimos del bucle
"""

# Ejecuta el código y comenta qué es un do-while y qué permite.
numero = 0

while True:
    numero = int(input("Ingresa un número mayor que 0: "))
    if numero > 0:
        break  # Si la condición se cumple, salimos del bucle


#MATEO SANCHO DIVE