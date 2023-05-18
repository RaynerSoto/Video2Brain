#Creando un archivosss
def crear_archivos():
    archivo = open('datos.dat','w')
    archivo.close()

#La a es de append por lo tanto el no va a sobreescribir el archivo, sino que lo va a añadir
def escribir_archivo():
    archivo = open('datos.txt','a')
    archivo.write('Rayner Alejandro Soto Martinez')

#Sin embargo el w sobreescribe el archivo completo
def escribir_archivo_w():
    archivo = open('datos.txt', 'w')
    archivo.write('Alexa Putellass')

#Listado de líneas
def leer_archivo():
    archivo = open('datos.txt','r')
    for linea in archivo.readlines():
        print(linea)
    archivo.close()
leer_archivo()