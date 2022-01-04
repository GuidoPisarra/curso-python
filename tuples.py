first_tuple = (1,2,3)
print(first_tuple)

# las tuplas no pueden ser modificadas de ninguna manera


# a traves de constructor 
second_tuple=tuple((4,5,6))
print(second_tuple)

# si se ingresa un solo elemento, python no lo considera como tupla, 
# para hacer una tupla de un solo eleemnto poner un elemento y finalizar en coma

print(second_tuple[0])

#para borrar la tupla 
del first_tuple
print(first_tuple)

#ejemplo de utilizacion de tuplas ciudades a partir de lat y longitud
locations= {
    (32.1212 , 36.1313) : "Tokyo",
    (33.121212 ,33.1313) :" Buenos Aires"
}





