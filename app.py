'''Esta aplicacion mostrara las propiedades de la persona'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
    def saludo(self):
        print('este es un saludo')
        

persona = Persona("juan", 26)
persona.saludo()