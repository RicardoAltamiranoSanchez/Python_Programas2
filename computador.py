from raton import Raton
from teclado import Teclado
from monitor import Monitor

class Computadora:
    contador_computadora=0
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora+=1
        self.__monitor=monitor
        self.__nombre=nombre
        self.__id_computadora=Computadora.contador_computadora
        self.__teclado=teclado
        self.__raton=raton
        
    def __str__(self):
        return "Id_Computadora:"+str(self.__id_computadora)+"    Nombre:"+self.__nombre+"\n"+self.__monitor.__str__()+"\n"+self.__teclado.__str__()+"\n"+self.__raton.__str__()
    def getNombre(self):
        return self.__nombre;
    def setNombre(self,nombre):
        self.__nombre=nombre
        #Monitor
    def getMarca_Monitor(self):
        return self.__monitor.__marca
    def setMarca_Monitor(self,marca):
        self.__monitor__marca=marca  
    def getTamanio_Monitor(self):
        return self.__monitor.__tamanio
    def setTamnio_Monitor(self,tamanio):
        self.__monitor.__tamanio=tamanio    
  ##dispositivos
    def getTipo_Raton(self):
        return self.__raton._tipo     
    def setTipo_Raton(self,tipo):
        self.__raton._tipo=tipo
    def getMarca_Raton(self):
        return self.__raton._marca
    def setMarca_Raton(self,marca):
        self.__raton._marca=marca 
   #Teclado
    def getTipo_Teclado(self):
         return self.__teclado._tipo     
    def setTipo_Teclado(self,tipo):
         self.__teclado._tipo=tipo
    def getMarca_Teclado(self):
         return self.__teclado._marca
    def setMarca_Teclado(self,marca):
         self.__teclado._marca=marca          
        
             
#m=Monitor("jdjdj",289.9)
#r=Raton("Estandar","Intel")
#t=Teclado("Normal","Samsung")
#c=Computadora("Ricardo",m,t,r)
#print(c)        
        