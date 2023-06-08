#sets

#add()
# Añade un elemento al conjunto. Recordemos que los conjuntos solo tienen elementos únicos, por lo que si está repetido no lo añadirá.
# Add an element to the set. Let's remember that the sets only have unique elements, so if it is repeated it will not add it.
conjunto = set()
conjunto.add(3)
conjunto.add(5)
conjunto.add(1)
conjunto.add(4)
conjunto.add(6)
conjunto.add(1)
print(conjunto)
# Output: {1, 3, 4, 5, 6}

#discard()
# Elimina un elemento si existe.
# Removes an item if it exists.
conjunto.discard(1)
print(conjunto)
# Output: {3, 4, 5, 6}

#issubset()
# Comprueba si un conjunto pertenece a otro, es decir, si todos sus elementos están en el otro conjunto.
# Checks if a set belongs to another, that is, if all its elements are in the other set
conjunto2 = {4,6}
print(conjunto2.issubset(conjunto))
# Output: True

#union()
# Junta dos conjuntos
# Match two sets
conjunto3 = {1,2,8}
conjunto4 = conjunto2.union(conjunto3)
print(conjunto4)
# Output: {1, 2, 4, 6, 8}

#diference()
# Encuentra los elementos no comunes entre conjuntos.
# Find the non-common elements between sets.
print(conjunto.difference(conjunto3))
# Output: {3, 4, 5, 6}
