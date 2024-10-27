def indica_primera_aparicion(lista:list,valor):
    validarValor = -1
    if valor in lista:
        validarValor = lista.index(valor)
        print(f' Posicion de {valor} en la lista {lista}: {validarValor}')

indica_primera_aparicion(["árbol","coche","casa"],"casa")