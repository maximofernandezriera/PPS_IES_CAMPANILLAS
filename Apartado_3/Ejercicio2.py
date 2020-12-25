'''
Crea un programa que genere un número aleatorio del 1 al 10. El usuario tendrá que adivinarlo, y
el programa tras cada intento le indicará al usuario si el número es más alto, bajo o si ha acertado.
La lógica para dar la respuesta al usuario deberá estar incluida en una función a la que se llamará
tras cada intento.
Nota: Para la creación del número aleatorio, utiliza el siguiente código:

from random import randint, uniform,random

numero = randint(0,10)

'''

# Generador de numero ramdom entre el 0 y el 10

from random import randint, uniform,random

numero = randint(0,10)

# Inicio de mi código

numeroUser = int(input("Introduce un numero de 0 a 10: "))

def adivinaelnumero(numero, numeroUser):

    while numero != numeroUser:

        if numeroUser > 10: 
            print ("El numero introducido es mayor que 10, por favor introduce un numero de 0 a 10")
            numeroUser = int(input("Introduce de nuevo un numero del 0 al 10: "))
        if numeroUser < 0: 
            print ("El numero introducido es menor que 0, por favor introduce un numero de 0 a 10") 
            numeroUser = int(input("Introduce de nuevo un numero del 0 al 10: "))

        if numero > numeroUser: print ("El numero que has introducido es más bajo que el numero creado por el programa, ¡Intentalo de nuevo!")
        if numero < numeroUser: print ("El numero que has introducido es más alto que el numero creado por el programa, ¡Intentalo de nuevo!")

        numeroUser = int(input("Introduce de nuevo un numero del 0 al 10: "))

        if numero == numeroUser:
            print("¡Has acertado!, Enhorabuena!")
            break

    else:
        print ("¡Has acertado a la primera!, Enhorabuena!")

adivinaelnumero(numero,numeroUser)