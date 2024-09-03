# lista_metodos_practica.py

# 1. Comienza creando una lista con algunos números
mi_lista = [3, 1, 4, 1, 5, 9]
print("Lista original:", mi_lista)

# 2. Aplica el método append() para agregar un número al final de la lista
mi_lista.append(7)
print("Después de append():", mi_lista)

# 3. Crea una copia de la lista usando el método copy()
copia_lista = mi_lista.copy()
print("Copia de la lista:", copia_lista)

# 4. Usa el método count() para contar cuántas veces aparece el número 1 en la lista
num_unos = mi_lista.count(1)
print("Número de veces que aparece 1:", num_unos)

# 5. Inserta el número 10 en la posición 2 de la lista usando el método insert()
mi_lista.insert(2, 10)
print("Después de insert(2, 10):", mi_lista)

# 6. Invierte el orden de la lista usando el método reverse()
mi_lista.reverse()
print("Después de reverse():", mi_lista)

# 7. Elimina la primera aparición del número 1 de la lista usando el método remove()
mi_lista.remove(1)
print("Después de remove(1):", mi_lista)

# 8. Ordena la lista en orden ascendente usando el método sort()
mi_lista.sort()
print("Después de sort():", mi_lista)

# 9. Elimina y devuelve el último elemento de la lista usando el método pop()
ultimo_elemento = mi_lista.pop()
print("Después de pop():", mi_lista, "- Último elemento:", ultimo_elemento)

# 10. Extiende la lista agregando los elementos de otra lista [7, 8, 9] usando el método extend()
otra_lista = [7, 8, 9]
mi_lista.extend(otra_lista)
print("Después de extend([7, 8, 9]):", mi_lista)

# 11. Encuentra el índice de la primera aparición del número 4 en la lista usando el método index()
indice_cuatro = mi_lista.index(4)
print("Índice de la primera aparición de 4:", indice_cuatro)

# 12. Elimina todos los elementos de la lista usando el método clear()
mi_lista.clear()
print("Después de clear():", mi_lista)