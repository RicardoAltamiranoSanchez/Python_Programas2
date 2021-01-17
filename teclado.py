from dispositivo import Dispositivo
class Teclado (Dispositivo):
    contador_teclado=0
    def __init__(self,tipo_entrada,marca):
        super().__init__(tipo_entrada,marca)
        Teclado.contador_teclado+=1
        self.__id_teclado=Teclado.contador_teclado
    def __str__(self):
        return"Id_Teclado:"+str(self.__id_teclado)+"   Tipo:"+self.getTipo()+"   Marca:"+self.getMarca()   
