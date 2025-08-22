#Crea una clase llamada Persona con atributos como nombre, edad y sexo. Agrega un metodo para imprimir

class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    
    def mostrardatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
    
p1=Persona("Juan",12,"M")
p1.mostrardatos()

