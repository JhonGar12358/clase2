# 6. Cola de tareas
# Implementa una cola de tareas utilizando una lista. Escribe funciones para agregar una tarea y eliminar la tarea más antigua.


arrayWorks= ['Limpiar','Organizar','Sacudir','Lavar', 'Doblar']

def add(work):
    arrayWorks.append(work)
    print('--AGREGAR TAREA--')
    print(arrayWorks)

def eliminate():
    arrayWorks.pop(0)
    print('--ELIMINAR TAREA MAS ANTIGUA--')
    print(arrayWorks)

add('barrer')
eliminate()