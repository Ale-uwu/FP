from Clase2_180924 import imc
import math

def estado_nutricional():
    peso = float(input("Introduce el peso: "))
    altura = float(input("Introduce tu altura: "))
    if peso <0 or altura <0:
        print("nenio que dise que no funsiona asi no me poedes dar cosas negativas")
        peso = float(input("Venga nenio el peso otra ve: "))
        altura = float(input("y la altura: "))
    val_imc = imc(peso,altura)
    print("Tu imc es de ", val_imc)
    if(val_imc<18.5):
        print("tienes poco peso")
    elif(18.5<=val_imc<25):
        print("tas gut")
    elif(25<=val_imc<30):
        print("sobrepeso")
    else:
        print("tas muy gordo")

#estado_nutricional()

def categoria_huracan(velocidad):
    if 118<= velocidad <= 152:
        return 1
    elif 153<= velocidad <= 176:
        return 2
    elif 177<= velocidad <= 208:
        return 3
    elif 209<= velocidad <= 248:
        return 4
    elif 249<= velocidad:
        return 5
    else:
        return -1

def categoria_huracan_test(velocidad):
    categoria = categoria_huracan(velocidad)
    if -1 == categoria:
        print("la velocidad no es válida")
    else:
        print("La categoría del huracán es: ", categoria)

def sumar_pares(n1,n2):
    sum = 0
    for i in range(n1,n2+1):
        if i % 2 == 0:
            sum += i
    return sum

def tabla_multiplicar(n):
    #return [n*i for i in range(1,11)]
    return [f'{n} x {i} = {n*i}' for i in range(1,11) ]

def tabla_multiplicar_test(n):
    for elemento in tabla_multiplicar(n):
        print(elemento)

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura


def volumen_cilindro_pre():
    radio = float(input("Introduce radio: "))
    altura = float(input("intorudce altrua: "))
    print("El volumen es ",volumen_cilindro(radio,altura))
if __name__ == "__main__":
    #categoria_huracan_test(0)
    #print(sumar_pares(7,58))
    #tabla_multiplicar_test(exp(exp(1)))
    #volumen_cilindro_pre()
    pass