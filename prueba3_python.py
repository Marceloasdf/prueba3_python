from funciones import *
import os,csv
while True:
    print("""compra de gas 'GAXPLOSIVE'
        1) Registrar pedido
        2) Listar todos los pedidos
        3) Buscar pedido por rut
        4) Imprimir hoja de ruta
        5) Salir""")
    opc=validarmenu([1,2,3,4,5])
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    elif opc==4:
        opcion4(pedidos)
    elif opc==5:
        opcion5()
    
    
