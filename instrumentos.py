
class Instrumento:

    def afinar(self):
        pass
    
    def tocar(self):
        pass

    def mostrar(self):
        return "Instrumento: " + str(type(self)).split(".")[-1][:-2]


class Guitarra(Instrumento):

    def afinar(self):
        return "Afinando guitarra "
    
    def tocar(self):
        return "Tocando guitarra "

class Saxo(Instrumento):

    def afinar(self):
        return "Afinando saxo "
    
    def tocar(self):
        return "Tocando saxo "

class Chelo(Instrumento):

    def afinar(self):
        return "Afinando chelo "
    
    def tocar(self):
        return "Tocando chelo "
    
class Bateria(Instrumento):
    def afinar(self):
        return "Afinando bateria "
    
    def tocar(self):
        return "Tocando bateria "