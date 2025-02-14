class Restaurante:
    def agregar_restaurante(self, nombre):
        self.nombre = nombre
        print(f'Agregando restaurante "{self.nombre}"...')

    def eliminar_restaurante(self, nombre):
        self.nombre = nombre
        print(f'Eliminado restaurante "{self.nombre}"...')

    def mostrar_informacion(self):
        print(f'El nombre del restaurante es "{self.nombre}"...')


# Instanciar la clace, el nombre de la variable tu lo elijes
restaurant_one = Restaurante()  # Aqui ya estamos creando un objeto y creamos una instancia del mismo
restaurant_two = Restaurante()
restaurant_three = Restaurante()
print(restaurant_one)
print(restaurant_two)
print(restaurant_three)

# Para ejecutar un metodo:
restaurant_one.agregar_restaurante('El caballo sediento')  # Aqui estamos
restaurant_one.mostrar_informacion()
restaurant_one.eliminar_restaurante('El caballo sediento')  # Aqui estamos
