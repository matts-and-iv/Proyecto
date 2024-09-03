# set_metodos_practica.py

# 1. Comienza creando un set con algunos números
mi_set = {1, 2, 3, 4, 5}
print("Set original:", mi_set)

# 2. Aplica el método add() para agregar un número al set
mi_set.add(9)
print("Después de add():", mi_set)

# 3. Crea una copia del set usando el método copy()
copia_set = mi_set.copy()
print("Copia del set:", copia_set)

# 4. Usa el método pop() para eliminar y devolver un elemento arbitrario del set
elemento = mi_set.pop()
print("Después de pop():", mi_set, "- Elemento eliminado:", elemento)

# 5. Aplica el método union() para unir el set con otro set {6, 7, 8}
otro_set = {6, 7, 8}
union_set = mi_set.union(otro_set)
print("Después de union({6, 7, 8}):", union_set)

# 6. Verifica si el set actual es un superset de {1, 2} usando issuperset()
es_superset = mi_set.issuperset({1, 2})
print("¿Es superset de {1, 2}?", es_superset)

# 7. Verifica si {2, 3} es un subset del set actual usando issubset()
es_subset = mi_set.issubset({2, 3})
print("¿Es {2, 3} un subset?", es_subset)

# 8. Encuentra la intersección del set actual con {3, 4, 5, 6} usando intersection()
interseccion = mi_set.intersection({3, 4, 5, 6})
print("Intersección con {3, 4, 5, 6}:", interseccion)

# 9. Encuentra la diferencia entre el set actual y {1, 2} usando difference()
diferencia = mi_set.difference({1,2})
print("Diferencia con {1, 2}:", diferencia)

# 10. Verifica si el set actual es disjunto con {7, 8, 9} usando isdisjoint()
es_disjunto = mi_set.isdisjoint({7,8,9})
print("¿Es disjoint con {7, 8, 9}?", es_disjunto)

# 11. Usa el método discard() para eliminar un elemento del set sin generar error si no existe
mi_set.discard(4)
print("Después de discard():", mi_set)

# 12. Elimina todos los elementos del set usando clear()
mi_set.clear()
print("Después de clear():", mi_set)