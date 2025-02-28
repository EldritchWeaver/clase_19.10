class Restaurante:

    def __init__(self, nombre='Restaurante', categoria='Ninguna', precio='Ninguno'):
        print('Yo me ejecuto automaticamente cuando creas un objeto de la clase')
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def agregar_restaurante(self, nombre):
        self.nombre = nombre
        print(f'Agregando restaurante "{self.nombre}"...')

    def mostrar_informacion(self):
        print(f'Nombre: "{self.nombre}", Categoría: "{self.categoria}", Precio: "{self.precio}"')

    def guardar_datos(self):
        if self.nombre != 'Restaurante':  # Evitar guardar instancias vacías
            with open(self.nombre + '.txt', 'w') as archivo:
                archivo.write(f'{self.nombre} \n')
                archivo.write(f'{self.categoria} \n')
                archivo.write(f'{self.precio} \n')

            print(f'Datos guardados en {self.nombre}.txt')
        else:
            print("Error: Restaurante sin nombre")

    def cargar_datos(self, nombre_archivo):
        try:
            with open(nombre_archivo + '.txt', 'r') as archivo:
                contenido = archivo.readlines()

                if len(contenido) >= 3:  # Verificar que existe el minimo de datos guardados
                    self.nombre = contenido[0].rstrip()
                    self.categoria = contenido[1].rstrip()
                    self.precio = contenido[2].rstrip()
                else:
                    print("Archivo incompleto")
        except FileNotFoundError:
            print(f'El archivo: {nombre_archivo}.txt no existe.')


    def leer_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo + '.txt', 'r') as archivo:
                contenido = archivo.read()  # Lee todo el contenido
                print(contenido)  # Imprime el contenido del archivo creado en la parte de 
        except FileNotFoundError:
            print(f'El archivo: {nombre_archivo} no existe.')  # Error si el archivo no existe

#restaurante = Restaurante("El pollo loco", "Comida casual", 50)
restaurante = Restaurante()
restaurante.mostrar_informacion()
restaurante.cargar_datos('El pollo loco')
restaurante.mostrar_informacion()
#restaurante.guardar_datos()
restaurante.leer_archivo('El pollo loco')