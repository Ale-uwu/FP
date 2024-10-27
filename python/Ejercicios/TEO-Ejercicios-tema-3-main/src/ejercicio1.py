from datetime import datetime,date
def fecha_en_intervalo(fecha:date,fecha_min:date,fecha_max:date)->bool:
        aux = True
        if fecha_min != None and fecha_max != None:
                aux = fecha_min < fecha < fecha_max
        elif fecha_max == None and fecha_min != None:
                aux = fecha_min < fecha
        elif fecha_min == None and fecha_max != None:
                aux = fecha < fecha_max
        return aux

if __name__ == "__main__":
    fecha_prueba = date(2024, 10, 2)

    # Caso 1: fecha dentro del intervalo
    print(fecha_en_intervalo(fecha_prueba, date(2024, 1, 1),date(2024, 12, 2)))  # True

    # Caso 2: fecha fuera del intervalo (menor que fecha_min)
    #fecha_min = 
    print(fecha_en_intervalo(fecha_prueba, date(2024, 10, 3), date(2024, 12, 31)))  # False

    # Caso 3: fecha fuera del intervalo (mayor que fecha_max)
    print(fecha_en_intervalo(fecha_prueba,None, date(2024, 9, 30)))  # False

    # Caso 4: sin límite inferior (fecha_min es None)
    print(fecha_en_intervalo(fecha_prueba, None, date(2024, 9, 30)))  # False

    # Caso 5: sin límite superior (fecha_max es None)
    print(fecha_en_intervalo(fecha_prueba, date(2024, 1, 1), None))  # True

    # Caso 6: sin límites (fecha_min es None y fecha_max es None)
    print(fecha_en_intervalo(fecha_prueba, None, None))  # True