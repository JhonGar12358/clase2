# 7. Contar elementos únicos
# Escribe una función que tome una lista y devuelva la cantidad de elementos únicos en ella.
   
list = [1, 1, 5, 6, 6, 8, 9, 7 ]


def elementosUnicos(lists):
    i = 0

    while i< len(lists):
        j = i + 1
        while j < len(lists):
            if lists[i] == list[j]:
                lists.pop(j)
                lists.pop(i)
                i = 0
                j = i + 1 
            else:
                j += 1
        i += 1
    return lists

print(elementosUnicos(list))


































# def count(array):
#     num = len(array)
#     print('--CONTAR ELEMENTOS--')
#     print(num)

# arrayWorks= ['Limpiar','Organizar','Sacudir','Lavar', 'Doblar']
# count(arrayWorks)