
def factorial():
    n = int(input("mete un numero niño: "))
    res = 1
    for i in range(1,n):
        res *= i+1
        n+=1
    return res