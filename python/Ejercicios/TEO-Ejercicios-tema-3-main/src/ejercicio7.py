import random

def juego_adivina_numero(maximo):
    intento = str()
    numAAdivinar = random.randint(1,maximo)
    print(f'DEBUG {numAAdivinar}')
    while(intento != numAAdivinar):
        intento = int(input("Dime un numerito: "))
        if 1 <= intento < maximo:
            if intento!=maximo:
                continue
        else:
            print(f'tu eres tonto? me tienes que dar un numero entre el 1 y el {maximo}')
    print("ole has ganao")
juego_adivina_numero(10)