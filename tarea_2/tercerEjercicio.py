# 3. Diccionario de estudiantes
# Crea un diccionario que almacene información sobre estudiantes (nombre, edad, calificaciones). Escribe funciones para agregar un estudiante, eliminar un estudiante y mostrar la información de un estudiante específico.


persona = {}

def agregar(persona, nombre, edad, calificaciones):

    persona[nombre] = {
        'edad' : edad,
        'calificaciones' : calificaciones,
    }
    print(persona)



agregar(persona,'david', 23, 4.5)
agregar(persona,'sebas', 21, 4.8)
agregar(persona,'camila', 20, 4.3)

def eliminar(persona, nom):
    if nom in persona:
        del persona[nom]
        print('Estudiante Eliminado')
    else:
        print('No se encuentra el nombre')

nom = int(input('--Eliminar persona-- \nIngresa el nombre de la persona: '))
eliminar(persona, nom)

print(persona)
