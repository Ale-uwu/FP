from collections import namedtuple
import csv
from datetime import datetime
from typing import NamedTuple

#Libro = namedtuple("Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")
Libro = NamedTuple("Libro",[("isbn",str),("titulo",str),("autor",str),("fecha_publicacion",datetime.date),("precio",float),("disponible",bool)])


def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


# TODO: Implemente las funciones solicitadas en el enunciado
def autores_disponibles(libros:list[Libro], inicial):
    autoresDisponibles = []
    for libro in libros:
        if libro.autor[0] == inicial and libro.disponible == True:
            autoresDisponibles.append(libro.autor)
    return autoresDisponibles

def titulos_baratos_actuales(libros:list[Libro]):
    titulosBaratosActuales = []
    for libro in libros:
        if libro.precio < 20 and libro.fecha_publicacion.year >= 2001:
            titulosBaratosActuales.append(libro.titulo)
    return titulosBaratosActuales

def media_precios(libros:list[Libro], palabra:str):
    auxPrecioLibrosContienenPalabra = []
    mediaPrecios = None
    for libro in libros:
        if palabra in libro.titulo:
            auxPrecioLibrosContienenPalabra.append(libro.precio)
    if len(auxPrecioLibrosContienenPalabra) != 0:
        mediaPrecios = sum(auxPrecioLibrosContienenPalabra)/len(auxPrecioLibrosContienenPalabra)
    return mediaPrecios

def libro_mas_reciente(libros:list[Libro]):
    libroMasReciente = libros[0]
    for libro in libros:
        if libro.fecha_publicacion > libroMasReciente.fecha_publicacion:
            libroMasReciente = libro
    return libro

if __name__ == "__main__":
    libros = lee_libros("python\Ejercicios\TEO-Ejercicios-tema-3-main\data\libreria.csv")
    print(f"Se han leído {len(libros)} libros.\n")

    print(f"Autores disponibles: {autores_disponibles(libros, "M")}\n")
    print(f"Titulos baratos actuales: {titulos_baratos_actuales(libros)}\n")
    print(
        f"Media de precios de libros con la palabra 'El': {media_precios(libros, "El")}\n"
    )
    print("Libro más reciente:", libro_mas_reciente(libros))
