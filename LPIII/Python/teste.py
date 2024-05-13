class Animal:
    staticvar = {"id": 0}

    def __init__(self, tipo):
        self.tipo = tipo
        self.staticvar["id"] += 1

    def fala(self, fala):
        print(fala)


class Cachorro(Animal):
    def fala(self, fala="Au Au"):
        Animal.fala(self, fala)
        


humano = Animal('mamífero')

passaro = Animal('ave')

humano.fala("Olá")
passaro.fala("Crá crá")

cachorro = Cachorro("mamífero")
cachorro.fala()
print(Animal.staticvar["id"])
