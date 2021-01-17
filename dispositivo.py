class Dispositivo:
    
 def __init__(self,tipo_entrada,marca):
     self._tipo=tipo_entrada
     self._marca=marca
 def getTipo(self):
    return self._tipo     
 def setTipo(self,tipo):
    self._tipo=tipo
 def getMarca(self):
    return self._marca
 def setMarca(self,marca):
    self._marca=marca
 