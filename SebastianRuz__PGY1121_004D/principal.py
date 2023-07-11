import os 
import numpy as np
import funciones as fn

os.system("cls")
matriz=np.empty([10,4], type(int))
fn.llenarMatriz(matriz)
os.system("cls")
rut=""
op=0
while(op!=5):
    print("******* Casa Feliz  ****** ")
    print()
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles ")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    op=fn.valiaOp(op)
    os.system("cls")

    if(op==1):
        fn.validaRut(rut)
        fn.mostrarDisponibles(matriz)
        depto=fn.validaDepto()
        letra=input("ingrese letra ")
        depto=letra+depto
        comprueba= fn.buscarDisponible(matriz,depto)
        if comprueba:    
            print("El asiento esta disponible!!")
            pagar=fn.comprarDepto(matriz, depto)
            print("\t Usted va a cancelar: ", pagar)
        else: 
            print("\t El asiento no esta disponible")
        os.system("pause")

        fn.comprarDepto(matriz,depto)

    elif(op==2):
        os.system("cls")
        fn.mostrarDisponibles(matriz)
    elif(op==3):
        print("trabajando")
    elif(op==4):
        print("trabajando")
    elif(op==5):
        break
