
# Declaración de una función
def nombre_funcion(id_arg1, id_arg2, id_arg3):
    pass

def saludar():
    print("Hola como estas")

def multiplicar(a,b):
    print("La multiplicación de a*b es igual a",a*b)

def imc(peso,altura):
    print("Tu imc es",peso/altura**2)
'''
    Utilizando "return" sería:
        def imc(peso,altura):
            return pes/altura**2
        
        print(imc(71,174))
                o
        indice_mc = imc(71,174)
        print(indice_mc)
'''

def comprobar_letra_mayuscula(letra : str):
    if letra.upper() == letra:
        print("La letra " + letra + " es mayuscula")
    else:
        print("La letra "+ letra +" es minuscula")

# Otra manera
def comprobar_letra_mayuscula2(letra : str):
  if letra < 'Z' and letra >= 'A':
    print("La letra " + letra + " es mayuscula")
  else:
    print("La letra "+ letra +" es minuscula")

def comprobar_digito(entrada):
    if type(entrada) in [int,float]:
        print("Es un dígito")
    else:
        print("No es un dígito")

def comprobar_caracter_especial():
    pass

def edad(n):
    if n<18:
        print("menor")
    elif 18<=n<29:
        print("joven")
    else:
        print("adulto")

# = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# TEORIA
''' 
    Estructura del programa:

        1. Importaciones 
            tipos:
                todo el módulo:
                    import math
                    import datetime
                función concreta:
                    from random import randint
                    from datetime import time, date, datetime
                    from typing import csv, namedTuple, List, Dict
                creando un alias:
                    from matplotlib import pyplot as plt
        2. Definicion de funciones
                Con def se establece la cabecera de una funcion creada por el usuario.
                Sigue la siguiente estructura:
                    def nombre_funcion(argumentos):
                        blablabla cosas cosas
                        return -> si devuelve algo
                Luego para llamar a la funcion tendremos que llamar a esta después de ser declarada
                nombre_funcion(argumentos) -> si son necesarios
        3, Funcion principal
                Parte del programa en el cual se llaman a todas las funciones
                se declara siempre con la misma estructura:

                    def main():
                        ...

                    if __name__ == "__main__":
                        main()

                Si se está ejecutando este modulo directamente se ejecuta la función principal con todos los metodos definidos dentro

    Entradas/Salidas:
        Para solicitar un dato por teclado se utiliza la funcion "input()" de la siguiente manera

            dato_pedido = tipo_del_dato_pedido(input("Introduce el dato"))
        
        De esta manera guardamos el dato pedido en una variable en la
        cual tenemos que definir el tipo y asignar un texto que saldrá por pantalla

        Para escribir algo en consola se utiliza el método "print()"

    Estructuras de control:

        Bifurcaciones:
            if, else, elif 
        Bucles:
            for, while

        Ya conozco su funcionamiento no me hacen falta escribir 
'''
# = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def main():
    # saludar()
    # multiplicar(2,3)
    # imc(71,1.74)
    comprobar_letra_mayuscula("l")
    comprobar_letra_mayuscula2("B")
    comprobar_digito(1)
    comprobar_digito("pingo")
    edad(7)
    edad(22)
    edad(932)

if __name__ == "__main__":
    main()