cil_5k=12500
cil_12k=25500
pedidos=[]
def opcion1():
    cont_cil5k=0
    cont_cil12k=0
    total=0
    print("Registrar pedido")
    rut=int(input("ingrese su rut (sin guion ni digito verificador): "))
    nombre=validarnombre()
    direccion=input("Ingrese su direccion: ")
    comuna=validarcomuna()
    respuesta=int(input("eliga cuantos cilindro de 5kg desea, si no lo desea escriba 0: "))
    cont_cil5k=cont_cil5k+respuesta
    print(f"contador{cont_cil5k}")

    resp=int(input(f"eliga cuantos cilindro de 12kg desea, si no lo desea escriba 0(${cil_12k}): "))
    cont_cil12k=cont_cil12k+resp

    pedido={"rut":rut,"nombre":nombre,"direccion":direccion,"comuna":comuna,"n_cil5k":cont_cil5k,"n_cil12k":cont_cil12k} #falta total
    pedidos.append(pedido)  


    print("Pedido exitoso!")

def opcion2():
    if not pedidos:
        print("no hay pedidos")
    else:
        print("listar todos los pedidos")
        for x in pedidos:
            print("Rut: ",x["rut"])
            print("Nombre: ",x["nombre"])
            print("Direccion: ",x["direccion"])
            print("Comuna: ",x["comuna"])
            print("numero de cilindros 5k: ",x["n_cil5k"])
            print("numero de cilindros 12kg: ",x["n_cil12k"])

def opcion3():
    print("buscar pedido por rut")
    if not pedidos:
        print("no hay ruts porque no hay pedidos")
    else:
        rut_buscar=int(input("ingrese rut a buscar: " ))
        for x in pedidos:
            if rut_buscar==x["rut"]:
                print("Rut: ",x["rut"])
                print("Nombre: ",x["nombre"])
                print("Direccion: ",x["direccion"])
                print("Comuna: ",x["comuna"])
                print("numero de cilindros 5k: ",x["n_cil5k"])
                print("numero de cilindros 12kg: ",x["n_cil12k"])
            else:
                print("no se encontro el Rut")


def opcion4(pedidos):
    import csv
    print("imprimir hoja de ruta")
    nom_archivo=input("que nombre desea ponerle al archivo? ")+".csv"
    print("cual de los sectores esta usted? (Santiago, Pirque, Puente alto)")
    with open(nom_archivo,"a",newline="") as archivo:
        escritor_csv=csv.writer(archivo)
        escritor_csv.writerows(archivo)


def opcion5():
    print("Adios!")
    exit()
#### funciones de validacion
def validarnombre():
    nombre=input("Ingrese su nombre: ")
    if nombre.isalpha():
        return nombre
    else:
        print("nombre no valido")

def validarcomuna():
    comuna=input("Ingrese su comuna: ")
    if comuna.isalpha():
        return comuna
    else:
        print("comuna no valida")

def validarmenu(lista_opciones):
    opc=int(input("Ingrese opcion: "))
    if opc in (lista_opciones):
        return opc
    else:
        print("opcion no valida")
    