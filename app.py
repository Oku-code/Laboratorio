'''Esta aplicacion mostrara las propiedades de la persona'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
<<<<<<< HEAD
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
=======
    def saludo(self):
        print('este es un saludo')
        

persona = Persona("juan", 26)
persona.saludo()
>>>>>>> cac2bcfc338a56c319a2910594d8c1a970c28ea2
