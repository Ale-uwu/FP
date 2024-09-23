lista_nombres = ["ale","jesus","olivia","caca",12,"aaaaaaaaaaaa"]
lista_edad = [19,20,19,15,20,30]

print(list(zip(lista_nombres,lista_edad)))

diccionario_edades = {nombre:edad for nombre,edad in list(zip(lista_nombres,lista_edad))}
print(diccionario_edades)