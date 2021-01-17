class Monitor:
    contador_monitor=0
    def __init__(self,marca,tamanio):
        Monitor.contador_monitor+=1
        self.__marca=marca
        self.__tamanio=tamanio
        self.__id_monitor=Monitor.contador_monitor
    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca  
    def getTamanio(self):
        return self.__tamanio
    def setTamnio(self,tamanio):
        self.__tamanio=tamanio
    def __str__(self):
        return "Id_Monitor"+str(self.__id_monitor)+"    Marca:"+self.getMarca()+"   Tamaño"+str(self.getTamanio())
