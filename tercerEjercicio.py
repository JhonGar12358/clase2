

persona = {}

def agregar(persona, nombre, edad, calificaciones):

    persona[nombre] = {
        'edad' : edad,
        'calificaciones' : calificaciones
    }
    print(persona)


agregar(persona,'sebastian', 20, 4.5)
agregar(persona,'davis', 20, 4.5)


# def eliminar(estudiante, numero):

#     persona