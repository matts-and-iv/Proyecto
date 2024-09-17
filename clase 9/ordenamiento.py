import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Variable global para controlar si la ejecución continúa
run_program = True

# Función de Bubble Sort
def bubble_sort(arr, draw_array, delay):
    n = len(arr)
    for i in range(n):
        if not run_program:
            break  # Salir si se presiona 'q'
        for j in range(0, n-i-1):
            if not run_program:
                break  # Salir si se presiona 'q'
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_array(arr, ['red' if x == j or x == j+1 else 'blue' for x in range(len(arr))])
            plt.pause(delay)

# Función de Selection Sort
def selection_sort(arr, draw_array, delay):
    z = len(arr)
    for e in range(z):
        if not run_program:
            break
        min_idx = e
        for j in range(e+1, z):
            if not run_program:
                break 
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[e], arr[min_idx] = arr[min_idx], arr[e]
        draw_array(arr, ['red' if x == e or x == min_idx else 'blue' for x in range(len(arr))])
        plt.pause(delay)


# Función de Insertion Sort
def insertion_sort(arr, draw_array, delay):
    for i in range(1, len(arr)):
        if not run_program:
            break
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            if not run_program:
                break
            arr[j + 1] = arr[j]
            j -= 1
            draw_array(arr, ['red' if x == j or x == j+1 else 'blue' for x in range(len(arr))])
            plt.pause(delay)
        arr[j + 1] = key
        draw_array(arr, ['red' if x == i else 'blue' for x in range(len(arr))])    
        plt.pause(delay)

# Función para manejar eventos de teclado
def on_key_press(event):
    global run_program
    if event.key == 'q':  # Si se presiona 'q', detener la ejecución
        print("Se presionó 'q'. Finalizando el programa...")
        run_program = False

# Función para dibujar el array
def draw_array(arr, color_array):
    plt.clf()
    plt.bar(range(len(arr)), arr, color=color_array)
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.title("Visualización de Algoritmo de Ordenación")

# Configuración inicial de la lista a ordenar
array = np.random.randint(1, 100, size=20)
delay = 0.1

# Configurar la gráfica
fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', on_key_press)  # Conectar el evento de teclado
plt.ion()  # Activar modo interactivo
draw_array(array, ['blue' for _ in range(len(array))])
plt.show()

# Aquí el estudiante puede seleccionar el algoritmo a ejecutar.
bubble_sort(array, draw_array, delay)
#selection_sort(array, draw_array, delay)
#insertion_sort(array, draw_array, delay)

# Finalizar la visualización
plt.ioff()
plt.show()
