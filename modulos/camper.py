from .variables import save, getAll
#from tabulate import tabulate
import os
def create():
    os.system("cls")
    print("""
        ***********************************
         ***   FORMULARIO DEL CAMPER   ***
        ***********************************            
        """)
    save({
        "Nombre":input("Ingrese el nombre del getAll: "),
        "Apellido":input("Ingrese el apellido del getAll: "),
        "Edad":int(input("Ingrese el nombre del getAll: "))
    })
    os.system("pause")
def read():
    print(f"""
        ***********************************
         ***   FORMULARIO DEL CAMPER   ***
        ***********************************            
        """)
    print(getAll())
        
        
    os.system("pause")  
def update():
    print("El getAll se actualizo")    
def delete():
    print("El getAll se ha borrado")    
def menu():
    menu=["Guardar","Buscar","Actualizar","Eliminar","Salir"]
    while(True):
        os.system("cls")
        print("""
            ***********************************
                ***   TABLA DEL CAMPER   ***
            ***********************************            
        """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                print(":)")
                match(opc):
                    case 1:
                        create()
                    case 2:
                        read()
                    case 3:
                        update()
                    case 4:
                        delete()    
                    case 5:
                        break
        except ValueError:
            print("Usuario no sea m** meta un numero")
        finally:
            print()
            