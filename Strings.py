#Strings

#upper() 
# Se usa para convertir una cadena a mayúscula.
# Used to convert a string to uppercase.
cadena = "Soy una cadena"
print(cadena.upper())
# Output: SOY UNA CADENA

#lower()
# Devuelve una cadena en minúscula.
# Returns a lowercase string.
print(cadena.lower())
# Output: soy una cadena

#count()
# Nos dice cuantas veces aparece una subcadena en una cadena.
# Tells us how many times a substring occurs in a string.
print(cadena.count('a'))
# Output: 3

#find()
# Nos devuelve el índice de la posición donde se encuentre la subcadena. Devuelve -1 si no está.
# Returns the index of the position where the substring is found. Returns -1 if it is not.
print(cadena.find('Soy'))
# Output: 0

#startswith()
# Devuelve True o False si la cadena empieza por la subcadena especificada.
# Returns True or False if the string starts with the specified substring.
print(cadena.startswith('Soy'))
# Output: True

#endswith()
# Devuelve True o False si la cadena termina por la subcadena especificada.
# Returns True or False if the string ends with the specified substring.
print(cadena.endswith('Soy'))
# Output: False

#split()
# Separa la cadena por el carácter especificado y devuelve una lista (útil para un string separado por comas).
# Separates the string by the specified character and returns a list (useful for a comma-separated string).
cadena2 = "Hola, que, tal, todo"
print(cadena2.split(','))
# Output: ['Hola', ' que', ' tal', ' todo']

#join()
# Une los caracteres de la cadena usando el carácter especificado.
# Matches the characters in the string using the specified character.
print(",".join(cadena))
# Output: S,o,y, ,u,n,a, ,c,a,d,e,n,a

#strip()
# Quita los espacios en blanco por delante y detrás de una cadena.
# Removes leading and trailing whitespace from a string.
cadena3 = "           Soy una cadena   "
print(cadena3.strip())
# Output: Soy una cadena

#replace()
# Reemplaza una subcadena dentro de la cadena y la deuvelve.
# Replace a substring within the string and return it.
print(cadena.replace('a', 'u'))
# Output: Soy unu cudenu
