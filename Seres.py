class Seres():
    codigo = ''
    nombre = ''
    # Parametro self para hacer referencia a un método propio de la clase
    def asignar_nombre(self,nombre):
        self.nombre = nombre
    def extraer_nombre(self):
        return self.nombre

    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre
    def __init__(self,nombre):
        self.nombre = nombre


#Prueba de la herencia
class Vivos(Seres):
    pass

#Creando una instancia de clases
pp = Seres('Rayner')
print(pp.nombre)
pp.asignar_nombre('Poty')
print(pp.nombre)
print(dir(pp))