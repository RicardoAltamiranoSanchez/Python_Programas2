from dispositivo import Dispositivo
class Raton  (Dispositivo):
    contador_raton=0
    def __init__(self,tipo_entrada,marca):
        super().__init__(tipo_entrada,marca)
        Raton.contador_raton+=1
        self.__id_Raton=Raton.contador_raton
    def __str__(self):
        return"Id_Raton:"+str(self.__id_Raton)+"    Tipo:"+self.getTipo()+"  Marca:"+self.getMarca()
    
     