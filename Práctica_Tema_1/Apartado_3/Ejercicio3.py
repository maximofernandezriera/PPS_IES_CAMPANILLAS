'''
Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
dentro de la siguiente lista: [6,14,11,3,2,1,15,19] . Implementa una función que se asegure que el
número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
otros programas.

Las funciones que se deben utilizar OBLIGATORIAMENTE tienen que tener las siguientes cabeceras:       

def estaEnRango(valor, minimo, maximo) 
# Devuelve True o False determinando qué valor se encuentra entre el mínimo y el máximo.

def estaEnLista(valor, lista)
# Devuelve True o False determinando si el valor está en la lista.

'''

while True:
    try:
        numeroUser = int(input("Introduce un numero de 1 al 20: "))

        lista = [6,14,11,3,2,1,15,19]

        def estaEnRango(numeroUser, minimo = 1, maximo = 20):

            if isinstance(numeroUser,int): 

                if numeroUser >= minimo and numeroUser <= maximo:
                    print(f"El numero {numeroUser} es valido")
                    return True
                else:
                    print("El valor introducido no esta dentro del rango de 1 y 20")
                    return False
            
            return False
        
        def estaEnLista(numeroUser, lista):

            if numeroUser in lista:
                print("Esta en la lista")
                return True
            else:
                print("No esta en la lista")
                return False
        
        print(estaEnRango(numeroUser))
        print(estaEnLista(numeroUser, lista))
        break

    except ValueError:
        print("El valor introducido no es un numero, por favor introduce un numero del 1 al 20")