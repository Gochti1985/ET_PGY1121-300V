import numpy as np
import os
import re
menu = ["mostra ubicacion","comprar entradas ","ver listado de asistentes","mostrar ganancias","salir"]
asientos = np.arange(1,101).reshape(10,10)
patron_rut = r'\n{7,8}-\W'

def contriur_menu(x):
    for a,b in enumerate(x):
        print(f"{a+1} {b}")
    choice = input("elija una opcion\n")
    os.system('cls')
    return choice

def analizar(x):
    global menu,asientos,patron_rut
    if x=="1":
        print("mostrar asientos\n")
        print(str(asientos).replace("["," ").replace("]"," ").replace("0","x"))

    elif x=="2":
        while True:
            try:
                rut = input("\ningrese el rut del asistenteen formato 12345678-9:\n")
                re.search(patron_rut, rut).group()
                os.system('cls')
                ans = int(input("ingresa entrada a comprar:"))
                if ans in asientos and np.where(asientos == ans)!=0:
                    asientos[np.where(asientos ==ans)] = 0
                    print("entrada vendida correctamente")
                except:
                print("formato incorrecto ingrese denuevo")
        
                


                
            
            


           


              
        