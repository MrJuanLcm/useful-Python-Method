#lists

#append()
# Añade un elemento al final de la lista.
# Add an element to the end of the list
lista = [1,2,3,4,5]
lista.append(0)
print(lista)

#extend()
# Une una lista a otra.
# Join one list to another.
lista2 = [8,9,2,0,3]
lista.extend(lista2)
print(lista)

#count()
# Como en los strings, cuenta el número de veces que aparece un elemento.
# As with strings, it counts the number of times an element appears.
lista = ['Hola', 'Hola', 'que', 'tal']
print(lista.count("Hola"))

#index()
# Devuelve el índice de un elemento en la lista. Si exite varias veces, devuelve la primera vez que aparece.
# Returns the index of an element in the list. If it exists multiple times, it returns the first occurrence.
print(lista.index("Hola"))

#insert()
# Inserta un elemento en la posición especificada
# Inserts an element at the specified position
lista.insert(2, "Soy una inserción")
print(lista)

#pop()
# Elimina el elemento cuyo índice le especifiquemos y nos lo devuelve
# Delete the element whose index we specify and which returns it to us.
print(lista.pop(1))
print(lista)

#remove()
# Borra el elemento cuyo valor le especifiquemos.
# Deletes the element whose value we specify
lista.remove("Hola")
print(lista)

#sort()
# Ordena la lista de menor a mayor
# Sort the list from smallest to largest
lista = [1,2,3,-9,18,13,-3]
lista.sort()
print(lista)

#sort()
# Podemos ordenarla de mayor a menor usando reverse en el sort
# We can order them from largest to smallest using reverse in the sort
lista.sort(reverse=True)
print(lista)
