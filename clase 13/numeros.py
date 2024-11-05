def verificar_par_impar(funcion):
    def envoltura(*args, **kwargs):
        x = args[0]  
        if x % 2 == 0:
            print("El número es par")
        else: 
            print("El número es impar")
        return funcion(*args, **kwargs)
    return envoltura

@verificar_par_impar
def imprimir_numero(x):
    print(f"El número es {x}", end="\n")



lst = [3,56,77,3,2,106,87,32]
for e in lst:
    imprimir_numero(e)