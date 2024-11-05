def mayuscula(funcion):
    def envoltura(*args):
        x = args[0]  
        x = x.upper()
        return funcion(x)
    return envoltura

@mayuscula
def imprimir_saludo(x):
    print(f"Hola, {x}")


for e in ["Mateo", "David", "Bryan", "Emma"]:
    imprimir_saludo(e)
