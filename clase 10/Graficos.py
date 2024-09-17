# Vamos a generar un gráfico de línea primero
# Gráfico de Líneas con Matplotlib
# Importar la biblioteca Matplotlib
import matplotlib.pyplot as plt

# Crear datos para el gráfico de línea
dias = [1, 2, 3, 4, 5, 6, 7]  # Días de la semana
temperaturas = [22, 24, 19, 21, 23, 20, 18]  # Temperaturas en grados Celsius

# Crear gráfico de línea
plt.plot(dias, temperaturas)

# Añadir títulos y etiquetas
plt.title('Temperaturas durante la semana')  # Título del gráfico
plt.xlabel('Días')  # Etiqueta para el eje X
plt.ylabel('Temperatura (°C)')  # Etiqueta para el eje Y

# Mostrar gráfico
plt.show()


# Crea tu propio Gráfico de Líneas con Matplotlib

# Ahora vamos a crear un gráfico de barras usando datos nuevos.

# Importar la biblioteca Matplotlib
import matplotlib.pyplot as plt

# Crear los datos
# En este caso, vamos a mostrar la cantidad de libros leídos por 5 amigos en un mes
amigos = ['Juan', 'María', 'Pedro', 'Ana', 'Luis']
libros_leidos = [3, 5, 2, 4, 6]

# Crear tu propio gráfico de barras
# Usa la función plt.bar() para hacer el gráfico de barras
# Rellena la función plt.bar() con los datos de 'amigos' y 'libros_leidos'

plt.bar(amigos, libros_leidos)

# Añadir títulos y etiquetas
# Usa plt.title() para añadir un título al gráfico, algo como: "Libros leídos por amigos en un mes"
# Usa plt.xlabel() para poner una etiqueta para los amigos, algo como: "Amigos"
# Usa plt.ylabel() para poner una etiqueta para la cantidad de libros leídos, algo como: "Libros leídos"

plt.title("Libros leídos por amigos en un mes")
plt.xlabel("Amigos")
plt.ylabel("Libros leídos")

# Mostrar el gráfico
# Finalmente, usa plt.show() para que se muestre el gráfico.

plt.show()


# Crea tu propio Gráfico de pastel con Matplotlib

# Ahora vamos a crear un gráfico de barras usando datos nuevos.

# Crear los datos
# Representaremos las actividades diarias de una persona
actividades = ['Dormir', 'Comer', 'Trabajar', 'Estudiar', 'Ocio']
horas = [8, 2, 8, 3, 3]  # Horas dedicadas a cada actividad en un día

# Crear gráfico de pastel
plt.pie(horas, labels=actividades, autopct='%1.1f%%', startangle=90)

# Añadir un título
plt.title('Distribución de tiempo diario')

# Mostrar gráfico
plt.show()