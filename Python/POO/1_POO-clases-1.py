class Restaurante():
    def agregar_restaurante(self, nombre):
        self.nombre = nombre
        print(f'Agregando restaurante "{self.nombre}"...')
    def eliminar_restaurante(self, nombre):
        self.nombre = nombre
        print(f'Eliminado restaurante "{self.nombre}"...')


# Instanciar la clace, el nombre de la variable tu lo elijes
restaurant = Restaurante()  # Aqui ya estamos creando un objeto y creamos una instancia del mismo
print(restaurant)

# Para ejecutar un metodo:
restaurant.agregar_restaurante('El caballo sediento')  # Aqui estamos
restaurant.eliminar_restaurante('El caballo sediento')  # Aqui estamos