class Carro:

    def __init__(self, marca, modelo, color, rango_velocidad):
        self.__marca = marca
        self.__modelo = modelo
        self.color = color
        self.rango_velocidad = rango_velocidad
        self.velocidad_actual = 0
        self.encendido = False

# Los Getters y Setters son metodos que nos permiten aceder (GET)
# o modificar (SET) los atributos de un objeto desde fuera de la clase

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

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
print(mi_carro.get_marca(), mi_carro.get_modelo(), mi_carro.color, mi_carro.rango_velocidad)

mi_carro.marca = 'Nissan'
mi_carro.set_marca('Nisan')
print(mi_carro.get_marca(), mi_carro.get_modelo(), mi_carro.color, mi_carro.rango_velocidad)


#Llama a un metodo el objeto
mi_carro.encender()
mi_carro.acelerar()
