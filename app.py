'''Esta aplicacion mostrara las propiedades de la persona'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
    def presentacion(self):
        '''Principal saludo'''
        print(f'Hola {self.nombre} espero que estes de buen humor hoy :)')

    
    @staticmethod
    def fecha_de_nacimiento(fecha_actual):
        birthday = self.edad - fecha_actual
        print(f'La fecha de nacimiento de {self.nombre} es: {birthday}')
        

persona = Persona("juan", 26)
persona.saludo()
persona.fecha_de_nacimiento(2021)
