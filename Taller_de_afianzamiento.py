# Autor: Antonio Betancourt 

#1 Desarrollar un programa que imprima el cuadrado del numero que el usuario ingresa mientras que el numero ingresado no sea negativo.
print("\n ==Primer Ejercicio== \n")
def primer_ejercicio(x): 
    
    if (x >= 0):
        cuadrado = x**2
        print("\nSu numero al cuadrado es: ", cuadrado)
    else:
        print("\nEl numero ingresado no puede ser negativo")
x = float(input("Ingrese un numero: "))
primer_ejercicio(x)

#2 Desarrollar un programa que dado un numero entero positivo n calcule e imprima (separados por espacios) n/2 si es par o 3n + 1 si es impar. El programa debe repetir el proceso con el numero resultado de dicha operacion mientras este sea diferente de 1. Por ejemplo para el numero 3 debe imprimir 10 5 16 8 4 2 1.
print("\n== Segundo Ejercicio ==\n")
def segundo_ejercicio(n):
    while n > 1:  
        print(n, end=" ")  
        if n % 2 == 0:
            n //= 2 
             
        else:
            n = 3 * n + 1  
    print(1)
n = int(input("Introduce un número entero positivo: "))
segundo_ejercicio(n)



#3 En 2022 el pais A tendra una poblacion de 25 millones de habitantes y el pais B de 18.9 millones. Las tasas de crecimiento anual de la poblacion seran de 2% y 3% respectivamente. Desarrollar un programa que imprima el año en que la poblacion del paıs B superara a la de A.
print("\n== Tercer Ejercicio ==\n")
def tercer_ejercicio():
    poblacion_A = 25_000_000  
    poblacion_B = 18_900_000  
    crecimiento_A = 0.02  
    crecimiento_B = 0.03  
    año = 2022  

    while poblacion_B < poblacion_A:
        poblacion_A += (poblacion_A * crecimiento_A)
        poblacion_B += (poblacion_B * crecimiento_B)
        año += 1

    print(f'La población del país B superará a la del país A en el año {año}.')
tercer_ejercicio()

#4 Diseñar una funcion que permita calcular el ́epsilon de la maquina. El epsilon de maquina es el numero decimal mas pequeno que sumado a 1 se puede representar de manera precisa en la maquina (que no es redondeado), es decir, retorna un valor diferente de 1,  ́este da una idea de la precision o numero de cifras reales que pueden ser almacenadas en la maquina. La idea es realizar un ciclo en el cual se realiza la operacion 1 +  para potencias de 2 desde  = 20 y continuando con potencias decrecientes de 2 
# = 2−1
#  = 2−2
#  = 2−3
#  = 2−4
# . . .
#hasta obtener que el resultado de la suma 1 +  no se altere.
print("\n == Cuarto Ejercicio ==\n")
def cuarto_ejercicio():
    e = 1.0  
    while (1.0 + e / 2.0) != 1.0:  
        e = e / 2.0               
    print("Épsilon de la máquina es:", e)
cuarto_ejercicio()

#5 Imprimir un listado con los numeros del 1 al 100 cada uno con su respectivo cuadrado.
print("\n== Quinto Ejercicio ==")   
def quinto_ejercicio():
    for y in range(1,101):
        cuadrado_1 = y**2
        print(f"\nSu numero {y} al cuadrado es: {cuadrado_1}")
quinto_ejercicio()
    
#6 Imprimir un listado con los numeros impares desde 1 hasta 999 y seguidamente otro listado con los numeros pares desde 2 hasta 1000.
print("\n== Sexto Ejercicio ==\n")
def sexto_ejercicio():
    print("== Listado de Pares ==\n")   
    for z in range(2,1001):
        if z % 2 == 0:
            print(z)
    print("\n== Listado de Impares ==\n")
    for z in range(1,1000):
        if z % 2 != 0:
            print(z)
sexto_ejercicio()

#7 Imprimir los numeros pares en forma descendente hasta 2 que son menores o iguales a un numero natural n ≥ 2 dado.
print("\n== Septimo Ejercicio ==\n")
def septimo_ejercicio(n1):
    print(f"\n== Numeros pares descendentes hasta el 2 desde el numero {n1} ==\n")
    for n1 in range(n1,1,-1):
        if (n1 >= 2) and (n1 % 2 == 0):
            print(n1)    
n1 = int(input("Ingrese un numero: "))
septimo_ejercicio(n1)

#8 Imprimir los numeros de 1 hasta un numero natural n dado, cada uno con su respectivo factorial.
print("\n== Octavo Ejercicio ==\n")
def octavo_ejercicio(n2):
    factorial_n2 = 1
    for n2 in range(1,n2+1):
        factorial_n2 *= n2
        print(f"El numero es: {n2} y su factorial es: {factorial_n2}")
n2 = int(input("Ingrese un numero: "))
octavo_ejercicio(n2)

#9 Calcular el valor de 2 elevado a la potencia n.
print("\n== Noveno Ejercicio ==\n")
def noveno_ejercicio(n3):
    potencia = 2**n3
    print(f"\nEl valor de {2} elevado a {n3} es igual a: {potencia}")
n3 = float(input("Escriba un numero: "))
noveno_ejercicio(n3)

#10 Leer un numero natural n, leer otro dato de tipo real x y calcular x**n
print("\n== Decimo Ejercicio ==\n")
def decimo_ejercicio():
    print(f"\nEl numero natural es: {n4}")
    print(f"\nEl numero real es: {x1}")
    potencia1 = x1**n4
    print(f"\n{x1} elevado a {n4} es: {potencia1}")
x1 = float(input("Escriba un numero: "))
n4 = int(input("\nEscriba otro numero: "))
decimo_ejercicio()

#11 Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
print("\n== Undecimo Ejercicio ==\n")
def undecimo_ejercicio():
    for tabla in range(1,10):
        print(f"\n== Tabla del {tabla} ==\n")
        for numero in range(1,11):
            print(f"{tabla} x {numero} = {tabla * numero}")
undecimo_ejercicio()