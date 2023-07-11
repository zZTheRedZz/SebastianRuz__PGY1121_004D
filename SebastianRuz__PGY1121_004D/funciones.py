import os

def valiaOp(op):
    while(True):
        try:
            op=int(input("   Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opción entre 1 y 5")
        except ValueError:
            print("Debe ser un número entero")
    return op

def validaRut(rut):
    rut=""
    while(len(rut)<=0):
        rut=input("Ingrese rut, debe tener minimo 8 caracteres ")
        if(len(rut.strip())<8) :
            print("Debe tener 8 caracteres minimo")
            rut=""

def llenarMatriz(mat):
    p=10
    for i in range(10):
        for j in range(4):
            mat[i,0]=f"A{p}"
            mat[i,1]=f"B{p}"
            mat[i,2]=f"C{p}"
            mat[i,3]=f"D{p}"
        p-=1

def mostrarDisponibles(bus):
    os.system("cls")
    for i in range(10):
        print("\n") #salto de linea
        for j in range(4):
            if(j==1):
                print("\t",bus[i,j], end="        ")
            else:
                print("\t",bus[i,j], end="    ")
    print("\n\n")
    
def validaDepto():
    Depto=0
    while True:
        try: 
            Depto=int(input("Ingrese número de departamento 1-10: "))
            if (Depto>=1 and Depto<=10):
                break
            else:
                print(" Error.. ingrese departamento entre  1 y 10")
        except ValueError:
            print(" Error.. ingrese departamento entre  1 y 10")
    return Depto

def buscarDisponible(matriz, depto):
    for x in range(10):
        for i in range(4):
            if (depto==matriz[x,i]):
                return True
    return False 

def comprarDepto(matriz, depto):
    for x in range(10):
        for i in range(4):
            if (matriz[x,i]==depto):
                matriz[x,i]=0
