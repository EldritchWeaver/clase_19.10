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

    def guardar_datos(self):
            with open(self.nombre + '.txt', 'w') as archivo:
                archivo.write(str(self.nombre) + '\n')
                archivo.write(str(self.categoria) + '\n')
                archivo.write(str(self.precio) + '\n')

            print(f'Archivo: {self.nombre} ha sido creado exitosamente y sus datos se han guardado.')

    def leer_archivo(self):
        try:
            with open(self.nombre + '.txt', 'r') as archivo:
                contenido = archivo.read()  # Lee todo el contenido
                print(contenido)  # Imprime el contenido del archivo creado en la parte de 
        except FileNotFoundError:
            print(f'El archivo: {self.nombre} no existe.')  # Error si el archivo no existe

restaurante = Restaurante("El pollo loco", "Comida casual", 50)
# restaurante.mostrar_informacion()
restaurante.guardar_datos()
restaurante.leer_archivo()