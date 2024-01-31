from .variables import save, getAll,camper
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
        "Nombre":input("Ingrese el nombre del camper: "),
        "Apellido":input("Ingrese el apellido del camper: "),
        "Edad":int(input("Ingrese el nombre del camper: "))
    })
    os.system("pause")
def read(codigo=None):
    os.system("cls")
    print(f"""
        ***********************************
         ***   FORMULARIO DEL CAMPER   ***
        ***********************************            
        """)
    if(codigo==None):
        for i,val in enumerate(getAll()):
            print(f"""
        _______________________
        Codigo: {i+1}
        Nombre: {val.get("Nombre")}
        Apellido: {val.get("Apellido")}
        Edad: {val.get("Edad")}
        Genero: {val.get("Genero")}
        ________________________
        """)
    else:
        val=getAll()[codigo-1]
        print(f"""
        _______________________
        Codigo: {codigo}
        Nombre: {val.get("Nombre")}
        Apellido: {val.get("Apellido")}
        Edad: {val.get("Edad")}
        Genero: {val.get("Genero")}
        ________________________
        """)
    os.system("pause")
        
        
    os.system("pause")  
def update():
    bandera=True
    while(bandera):
        os.system("cls")
        read()
        print("""
            **********************************
             ***   ACTUALIZAR UN CAMPER   ***
            **********************************           
        """)
        codigo=int(input("Cual es el codigo del camper que desea eliminar?:\n"))
        read(codigo)  
        print("""
        ¿Esta seguro que desea actualizar el camper?
                1. Si
                2. No
                3. Cancelar
        """)
        opc=int(input())
        match(opc):
            case 1:
                val = {
                "Nombre":input("Ingrese el nombre del camper: "),
                "Apellido":input("Ingrese el apellido del camper: "),
                "Edad":int(input("Ingrese el nombre del camper: "))
                }
                camper[codigo-1]=val
                bandera = False
                os.system("cls")
                print(f"""
                El camper fue actualizado
                _______________________
                Codigo: {codigo}
                Nombre: {val.get("Nombre")}
                Apellido: {val.get("Apellido")}
                Edad: {val.get("Edad")}
                Genero: {val.get("Genero")}
                ________________________
                """)
                os.system("pause")
                bandera=False
            case 3:
                bandera = False
def delete():
    bandera=True
    while(bandera):
        os.system("cls")
        read()
        print("""
            **********************************
            ***   ELIMINAR UN CAMPER   ***
            **********************************           
        """)
        codigo=int(input("Cual es el codigo del camper que desea eliminar?:\n"))
        read(codigo)
        
        print("""
        ¿Esta seguro que desea eliminar el camper?
                1. Si
                2. No
                3. Cancelar
        """)
        opc=int(input())
        match(opc):
            case 1: 
                val=camper.pop(codigo-1)
                os.system("cls")
                print(f"""
                El camper fue eliminado
                _______________________
                Codigo: {codigo}
                Nombre: {val.get("Nombre")}
                Apellido: {val.get("Apellido")}
                Edad: {val.get("Edad")}
                Genero: {val.get("Genero")}
                ________________________
                """)
                os.system("pause")
                bandera=False
            case 3:
                bandera=False
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
            