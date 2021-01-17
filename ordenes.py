class Orden:
    id_orden=0
    def __init__(self,computadora):
        Orden.id_orden+=1
        self.__computadora=computadora
        self.__id_orden=Orden.id_orden
    def Agregarcomputadora(self,computadora):
        self.__computadora.append(computadora)    
    def __str__(self):
        lista_computadora=""
        for lista in self.__computadora:
              lista_computadora=lista.__str__()+"\n"
              
        return "Orden:"+str(self.id_orden)+"\n"+lista_computadora+"\n"
