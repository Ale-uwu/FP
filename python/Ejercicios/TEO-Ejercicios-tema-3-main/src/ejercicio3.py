def imprime_pares(n:int):
    print(f'imprimiendo números pares menores o iguales a {n}')
    print(" ".join([str(numero) for numero in range(1,n+1) if numero%2 == 0]))
        
imprime_pares(72)