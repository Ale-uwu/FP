def imprime_pares_inverso(n:int):
    print(f'imprimiendo números pares menores o iguales a {n}')
    print(" ".join(reversed([str(numero) for numero in range(1,n+1) if numero%2 == 0])))
        
imprime_pares_inverso(72)