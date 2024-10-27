def imprime_diccionario(diccionario:dict):
    for clave,valor in diccionario.items():
        print(f'{clave} ==> {valor}')

precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5
}

imprime_diccionario(precios_productos)