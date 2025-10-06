# Autor: Antonio Betancourt 

#1 Desarrollar un programa que imprima el cuadrado del numero que el usuario ingresa mientras que el numero ingresado no sea negativo.
def primerejercicio(x): 
    x = int(input("Ingrese un numero: "))
    if (x >= 0):
        cuadrado = x**2
        print("Su numero al cuadrado es: ", cuadrado)
    else:
        print("El numero ingresado no puede ser negativo")

#2 Desarrollar un programa que dado un numero entero positivo n calcule e imprima (separados por espacios) n/2 si es par o 3n + 1 si es impar. El programa debe repetir el proceso con el numero resultado de dicha operacion mientras este sea diferente de 1. Por ejemplo para el numero 3 debe imprimir 10 5 16 8 4 2 1.

def segundoejercicio(n):
    while n != 1:  
        print(n, end=" ")  
        if n % 2 == 0:
            n /= 2  
        else:
            n = 3 * n + 1  
    print(1)

n = int(input("Introduce un número entero positivo: "))
segundoejercicio(n)



#3 En 2022 el pais A tendra una poblacion de 25 millones de habitantes y el pais B de 18.9 millones. Las tasas de crecimiento anual de la poblacion seran de 2% y 3% respectivamente. Desarrollar un programa que imprima el año en que la poblacion del paıs B superara a la de A.

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



