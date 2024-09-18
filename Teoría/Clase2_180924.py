
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
# saludar()
# multiplicar(2,3)
# imc(71,1.74)