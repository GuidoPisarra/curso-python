#string
print('hola mundo')
print('''hola mundo''')
print("""hola""")
print("hola")
print("hola"+ " a todos")
print(type("hola"))

#numeros

#integer
print(type(1))
#float
print(type(1.5))
print (4+4); print (4*4); print (4/4); print (4-4)

#boolean
print(type(True))
True
False

#list
print(type([10, 20, 30, 55]))
print([10, 20, 30, 55])
print(["hola","a","todos"])
print([10, 20, 3.5, True,"anda"])

# Tuplas (seria una lista constante) se pone entre ()
print(type((10, 20, 30, 55)))
print((10, 20, 30, 55))

# diccionario agrupan datos que pertenecen a una misma entidad (una especie de registro)
print(type({
    "name":"Guido",
    "surname":"Pisarra",
    "nickname":"Guidin",
}))

print({
    "name":"Guido",
    "surname":"Pisarra",
    "nickname":"Guidin",
    "age":35,
    "heigth":1.72,
})

# tipo None, es el que no esta definido aun (typo "vacio")
None 