# Polimorfismo
# Es la capacidad de un objeto de comportarse de diferentes formas
# Va a tener diferente comportamiento dependiendo de la situacion

class Restaurante:

    def __init__(self, nombre, categoria, precio):
        print('Yo me ejecuto automaticamente cuando creas un objeto de la clase')
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def agregar_restaurante(self, nombre):
        self.nombre = nombre
        print(f'Agregando restaurante "{self.nombre}"...')

    def mostrar_informacion(self):
        print(f'El nombre del restaurante es "{self.nombre}" y es de categoria "{self.categoria}"..')

restaurante = Restaurante("El pollo loco", "Comida casual", 50)
restaurante.mostrar_informacion()

# Herencia

class Hotel(Restaurante):

    def __init__(self, nombre, categoria, precio, numero_habitaciones, piscina):
        super().__init__(nombre, categoria, precio)
        self.numero_habitaciones = numero_habitaciones
        self.tiene_piscina = piscina  # Almacenar como booleano

    def get_piscina(self):
        return self.piscina

# Reescribir el metodo mostrar_informacion y debe llamarse igual

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Numero de habitaciones: {self.numero_habitaciones}')
        print(f'Tiene piscina: {'Si' if self.tiene_piscina else 'No'}')

print('')
hotel = Hotel('Vermellon', '5 Estrellas', 800, 100, True)
hotel.mostrar_informacion()