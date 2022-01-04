demo_list=[1, "hola", 1.34, True, [1,2,3]]
colors= ["azul", "rojo", "verde"]

#con constructor
second_list=list((8,9,7))
print(demo_list)
print(colors)
print(second_list)

# poner rangos a lista
r=list (range(1,11))
print (r)


#saber de que tipo de dato es una lista

#print (dir(colors))
print (len(colors))
print (colors[0])
print(colors[-1])

print("green" in colors)
print("verde" in colors)

colors.append("anaranjado")
print(colors)
#para agregar a una lista usar extends con una lista, sino crea una lista dentro de otra
colors.extend(("amarillo", "negro"))
print (colors)
# agregar en indice
colors.insert(1, "blanco")
print (colors)
#agrergar a lo ultimo 
colors.insert (len(colors),"rosa")
print(colors)

#sacar ultimo elemento
colors.pop()
print (colors)

#sacar uno determinado
colors.remove("blanco")
print(colors)

#sacar segun indice
colors.pop(2)
print(colors)

#eliminar todos

#colors.clear()
print (colors)

#ordenados
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index("azul"))

print (colors.count("rojo"))
