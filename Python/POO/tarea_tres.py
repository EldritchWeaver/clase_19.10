"""_Tarea 3_
    Un medigo que entre a cirugia:
    medico,
    especialidad,
    operando
"""


class Medico:
    def __init__(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.tarea_actual = 'Desocupado'
        self.ocupado = False

    def cambiar_medico(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.tarea_actual = 'Desocupado'
        self.ocupado = False

    def asig_tarea(self, tareas):
        print('TAREAS:')
        for tarea in tareas:
            print(f'-{tarea}')
        tarea = input('Asigne una tarea: ')
        self.tarea_actual = tarea

        if self.tarea_actual == 'Desocupado':
            self.ocupado = False
        else:
            self.ocupado = True

    def desocupar(self):
        if self.tarea_actual:
            self.tarea_actual = 'Desocupado'
            self.ocupado = False
        else:
            pass


class Mdc_Clinica(Medico):
    def __init__(self, nombre, apellido, especialidad, clinica):
        super().__init__(nombre, apellido, especialidad)
        self.clinica = clinica

    def cambiar_medico(self, nombre, apellido, especialidad, clinica):
        super().cambiar_medico(nombre, apellido, especialidad)
        self.clinica = clinica

especialidades = [
    'Medicina General', 'Pediatria', 'Cardiologia',
    'Neurologia', 'Dermatologia', 'Gastroenterologia',
    'Oncologia', 'Ortopedia', 'Psiquiatría',
    'Ginecología y Obstetricia', 'Oftalmologia',
    'Otorrinolaringología', 'Endocrinología', 'Nefrología'
                  ]  # Son algunas especialdades que me encontre por alli

tareas = ['Consulta', 'Diagnostico', 'Tratamiento', 'Cirugia', 'Desocupado']

# TESTS:
"""
medico_uno = Medico('Jhoan', 'Martinez', especialidades[0])
medico_uno.asig_tarea(tareas)
print(medico_uno.nombre, medico_uno.apellido, medico_uno.especialidad, medico_uno.tarea_actual, medico_uno.ocupado)

medico_uno.cambiar_medico('Eleanor', 'Rigbi', especialidades[4])
medico_uno.asig_tarea(tareas)
medico_uno.desocupar()
print(medico_uno.nombre, medico_uno.apellido, medico_uno.especialidad, medico_uno.tarea_actual, medico_uno.ocupado)

medico_dos = Medico('Jhoan', 'Martinez', especialidades[10])
medico_dos.asig_tarea(tareas)
print(medico_dos.nombre, medico_dos.apellido, medico_dos.especialidad, medico_dos.tarea_actual, medico_dos.ocupado)
print(medico_uno.nombre, medico_uno.apellido, medico_uno.especialidad, medico_uno.tarea_actual, medico_uno.ocupado)
"""

print('')
medico = Mdc_Clinica('Jhoan', 'Martinez', especialidades[10], 'Frambuesa')
medico.asig_tarea(tareas)
print(medico.nombre, medico.apellido, medico.especialidad, medico.clinica, medico.tarea_actual, medico.ocupado)