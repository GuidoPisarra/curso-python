my_string= "hola mundo 1"

#con dir se puede ver lo que puede hacer con una variable
print(dir (my_string))

print(my_string.upper())
print(my_string.title())
print(my_string.capitalize())
print(my_string.replace("hola","holaaaaa"))
print(my_string.replace("hola","holaaaaa").upper())

print(my_string.count("o"))

print(my_string.startswith("hola"))
print(my_string.endswith("do"))

# divide donde se encuentra un espacio en blanco (por defecto)
print(my_string.split())
# divide donde se encuentra un caracter
print(my_string.split("o"))
#posicion
print(my_string.find("o"))

# longitud
print(my_string.__len__())
print(len(my_string)) 

print(my_string.index("o"))

print(my_string.isalnum())
print(my_string.isalpha())

print (my_string[2])
print (my_string[-1])

print ("prueba "+ my_string)

print (f"prueba { my_string}")

