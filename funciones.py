numeros = [1, 2, 3, 4, 5, "hola"]


#while True:
#    numero = input("Introduce un número: ")
#    if numero == "q" or numero == "Q":
#        break
#    numeros += numero

def imprimirNumeros(lista):
    for i in lista:
        print(i)

def imprimirNumeros2(lista):
    for i in range(len(lista)):
        print(lista[i])

coordenadas = [
    [1, 2],
    [2, 2, 3]
]

imprimirNumeros(numeros)
imprimirNumeros2(numeros)

for coordenada in coordenadas:
    salida = ""
    for valor in coordenada:
        salida+= str(valor) + ", "
    print(salida)