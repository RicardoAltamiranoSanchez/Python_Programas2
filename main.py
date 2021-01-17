from computador import Computadora
from raton import Raton
from teclado import Teclado
from monitor import Monitor
from ordenes import Orden
salir=False
opcion=0
while (salir!=True):
 print("Bienvenido Arme su propia computadora")
 print("Desear ingresar y/n")
 entrada=input()
 if(entrada=="Y" or entrada=="y"):
     while (opcion<6):
      print("Digite la opcion que desee")
      print("1.Escojer tipo de Ratones\n2.Escojer tipo de Teclados")
      print("3.Escojer tipo de monitor")
      print("4.Guardarlo en una orden")
      print("5.Agregando orden")
      print("6.Salir")
      opcion=int(input("Digite la opcion que desee\n"))
      if(opcion==1):
          tipo_entrada_raton=input("Digite el tipo de entrada del raton\n")
          marca_raton=input("Digite la marca del raton\n")
      elif(opcion==2):
          tipo_entrada_taclado=input("Digite el tipo de entrada del teclado\n")
          marca_teclado=input("Digite la marca del teclado\n")
      elif(opcion==3):
           marca_monitor=input("Digite la marca del monitor monitor\n")
           tamanio_monitor=input("Digite el tamanio del monitor\n")
      elif(opcion==4):
            
            print("Guardando tu orden")
            nombre=input("Ingresa tu nombre\n")
            m=Monitor(marca_monitor,tamanio_monitor)
            r=Raton(tipo_entrada_raton,marca_raton)
            t=Teclado(tipo_entrada_taclado,marca_teclado)
            c=Computadora(nombre,m,t,r)
            ordenes=[c]
            o=Orden(ordenes)
            print(o)
      elif(opcion==5):
            
            print("Arreglando en la orden ya existente")
            m=Monitor(marca_monitor,tamanio_monitor)
            r=Raton(tipo_entrada_raton,marca_raton)
            t=Teclado(tipo_entrada_taclado,marca_teclado)
            c1=Computadora(nombre,m,t,r)
            ordenes.append(c1)
            o.Agregarcomputadora(ordenes)
            print(o)    
      else:
          print("Esa opcion no existe")         
 elif(entrada=="N" or entrada=="n"):
      salir=True
 else:print("Error el ordenador no entiende ese patron")     
  
 
    
    
    