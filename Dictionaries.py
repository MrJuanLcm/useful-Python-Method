#dictionaries

#get()
# Busca un valor a partir de su clave.
# Looks up a value from its key.
diccionario = {'Nombre':'Ana','Edad':35,'Profesion':'Administrativo'}
print(diccionario.get('Edad'))
# Output: 35

#keys()
# Genera una lista con las claves del diccionario.
# Generates a list with the dictionary keys.
print(diccionario.keys())
# Output: dict_keys(['Nombre', 'Edad', 'Profesion'])

#values()
# Una lista con los valores del diccionario.
# A list with the values from the dictionary.
print(diccionario.values())
# Output: dict_values(['Ana', 35, 'Administrativo'])

#items()
# Devuelve las duplas clave/valor del diccionario en formato lista.
# Returns the key/value pairs from the dictionary in list format.
print(diccionario.items())
# Output: dict_items([('Nombre', 'Ana'), ('Edad', 35), ('Profesion', 'Administrativo')])

#pop()
# Elimina una clave/valor en un diccionario.
# Delete a key/value in a dictionary.
diccionario.pop('Nombre')
print(diccionario.items())
# Output: dict_items([('Edad', 35), ('Profesion', 'Administrativo')])
