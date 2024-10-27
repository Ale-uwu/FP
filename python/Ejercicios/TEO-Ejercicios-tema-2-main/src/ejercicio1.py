import csv
from typing import NamedTuple
from datetime import datetime

VariacionesTemperaturas = NamedTuple("VariacionesTemperaturas",[("fecha",datetime.date),("variacion",float)])

def lee_variaciones_temperatura(fichero):
    aux = []
    with open(fichero,encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha,variacion in lector:
            fecha = datetime.strptime(fecha.strip(),"%d/%m/%Y")
            variacion = float(variacion)
            aux.append(VariacionesTemperaturas(fecha,variacion))
    return aux

def lee_variaciones_temperatura_test(fichero):
    datos = lee_variaciones_temperatura(fichero)
    print(datos[:5])

def main():
    lee_variaciones_temperatura_test("python\Ejercicios\TEO-Ejercicios-tema-2-main\data\monthly_csv.csv")

if __name__ == "__main__":
    main()