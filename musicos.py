from instrumentos import *

class Musico:

    def __init__(self, nombre):
        self.nombre =nombre
        self.instrumento = None

    def asignar_instrumento(self,instrumento):
        self.instrumento = instrumento

    def afinar_instrumento(self):
        return self.instrumento.afinar()

    def tocar_instrumento(self):
        return self.instrumento.tocar()
