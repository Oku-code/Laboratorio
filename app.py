'''Esta aplicacion mostrara las propiedades de la persona'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
    def saludo(self):
        '''Principal saludo'''
        print(f'Hola {self.nombre} espero que estes de buen humor hoy :)')
        

persona = Persona("juan", 26)
persona.saludo()
