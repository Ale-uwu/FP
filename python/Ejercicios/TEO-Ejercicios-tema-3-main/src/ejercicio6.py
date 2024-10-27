def calcula_precios(precio:float,listaEdades:list)->list:
    descuentoPrecio = 0.5
    aux = []
    for edad in listaEdades:
        if 19<edad<65:
            aux.append(precio*descuentoPrecio)
        else:
            aux.append(precio)
    print(f'Precios de las entradas para las personas con edades {" ".join([str(edad) for edad in listaEdades])}, (Precio normal de la entrada: {precio}€)')
    print(f'{" ".join([str(p) for p in aux])}')
    return aux

calcula_precios(62,[4,35,234,1,234,33,11,16,19,28,18,18,18])