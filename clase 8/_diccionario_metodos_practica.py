# diccionario_metodos_practica.py

# 1. Comienza creando un diccionario con algunos pares clave-valor
mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print("Diccionario original:", mi_diccionario)

# 2. Crea una copia del diccionario usando el método copy()
copy = mi_diccionario.copy()
print("Copia del diccionario:", copy)

# 4. Usa el método fromkeys() para crear un nuevo diccionario con claves de una lista y un valor predeterminado
claves = ["a", "e", "i", "o", "u"]
nuevo = dict.fromkeys(claves, 0)
print("Nuevo diccionario con fromkeys():", nuevo)

# 5. Usa el método items() para obtener todos los pares clave-valor del diccionario
items = mi_diccionario.items()
print("Items del diccionario:", items)

# 6. Usa el método get() para obtener el valor de una clave específica sin causar un error si la clave no existe
valor = mi_diccionario.get("edad")
print("Valor obtenido con get('edad'):", valor)

# 7. Usa el método keys() para obtener todas las claves del diccionario
claves = mi_diccionario.keys()
print("Claves del diccionario:", claves)

# 8. Usa el método pop() para eliminar una clave y devolver su valor
valor = mi_diccionario.pop("ciudad")
print("Después de pop('ciudad'):", mi_diccionario, "- Valor eliminado:", valor)

# 9. Usa el método values() para obtener todos los valores del diccionario
valores = mi_diccionario.values()
print("Valores del diccionario:", valores)

# 10. Usa el método update() para actualizar el diccionario con otro diccionario
otro = {"pais": "España", "edad": 30}
mi_diccionario.update(otro)
print("Después de update():", mi_diccionario)

# 11. Usa el método setdefault() para obtener el valor de una clave y, si no existe, agregarla con un valor predeterminado
valor_predeterminado = mi_diccionario.setdefault("profesión", "Desconocido")
print("Después de setdefault('profesión', 'Desconocido'):", mi_diccionario)

# 12. Usa el método popitem() para eliminar y devolver el último par clave-valor añadido
ultimo = mi_diccionario.popitem()
print("Después de popitem():", mi_diccionario, "- Último item eliminado:", ultimo)

# 3. Usa el método clear() para eliminar todos los elementos del diccionario
mi_diccionario.clear()
print("Después de clear():", mi_diccionario)