#Funciones sin parámetros
def imprimir_cadena1():
    print('Hola')

#Funcion con parámetros
def imprimir_cadena(cadena):
    print(cadena)

#Función con parámetros por defecto
#Los parámetros se ponen de derecha a izquierda por eso es que es b=0
def suma(a,b = 0):
    return a+b

def buscar_pares(valor):
    for i in valor:
        if i%2==0:
            print(i)
