lista = ["Sena", "Ignacio" , 19] 
print(lista) 
print(lista[2])

tupla = ("Sena" , "Ignacio" , 99) #No se modifica

lista[2] = 20

# tupla[2] = 3 NO se puede
print(lista[2] , tupla[2])

conjunto = {"Sena" , "Ignacio"}
print(conjunto)
# print(conjunto[1]) No se puede acceder por indice, no permite repitidos

diccionario = {
    'nombre' : "Ignacio",
    'edad' : 19,
    'apellido' : "Sena"
} #como mapa en java

print(diccionario['nombre'])