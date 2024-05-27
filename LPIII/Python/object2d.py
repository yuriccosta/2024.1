class obj2D():
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y

    def setA(self, x, y):
        self.__x = x
        self.__y = y

    def getA(self):
        return self.__x, self.__y
    
    def getArea(self):
        return 0
    
    def getPerimetro(self):
        return 0
    
    def __str__(self):
        return f"ObjetoGeometrico2D, Vértice A em {self.getArea}, Área = 0,0, Perímetro = 0.0"

class Retangulo(obj2D):
    def __init__(self, x1 = 0.0, y1 = 0.0, x2 = 1.0, y2 = 1.0):
        obj2D(x1, y1)
        self.__x2 = x2
        self.__y2 = y2
    
    def getArea(self):
        return abs((self.__x - self.__x2) * (self.__y * self.__y2)) 


obj = Retangulo(1,2,3,4)
print(obj.getA())
