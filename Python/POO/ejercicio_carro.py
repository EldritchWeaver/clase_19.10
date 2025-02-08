class Carro:


    def __init__(self, marca, modelo, color, rango_velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.rango_velocidad = rango_velocidad
        self.velocidad_actual = 0
        self.encendido = False


    def agregar_carro(self, marca, modelo, color, rango_velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.rango_velocidad = rango_velocidad


    def encender(self):
        self.encendido = True
        print('El carro se ha encendido...')


    def apagar(self):
        self.encendido = False
        print('El carro se ha encendido...')


    def acelerar(self):
        if self.encendido:
            print('El carro esta encendido y acelerando...')
        else:
            print("Tu' que te cree'? que estamos en Hogwards? eh?")

mi_carro = Carro('Toyota', 'Corolla', 'Azul', [0, 240])

print(mi_carro.marca, mi_carro.modelo, mi_carro.color, mi_carro.rango_velocidad)
mi_carro.acelerar()
mi_carro.encender()
mi_carro.acelerar()