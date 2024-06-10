from roteiro import Roteiro


class RoteiroOnibus(Roteiro):
    def __init__(self, qntpassageiros, saida, origem, destino, distancia = 0, paradas = None): 
        super().__init__(origem, destino, distancia, paradas)
        self.__qntpassageiros = qntpassageiros
        self.__saida = saida

    def getHorarioSaida(self):
        return self.__saida
    
    def getHorarioChegada(self):
        chegada = self.getDistancia() / 70
        for c in range(0, self.qntParadas()):
            chegada += 0.25
        hora = abs(int(chegada + int(self.__saida.split(":")[0]))) % 24
        return f"{hora}:00"
    
    def getQntPassageiros(self):
        return self.__qntpassageiros
    
    def __str__(self):
        return f"Quantidade de passageiros: {self.__qntpassageiros}, Horario de saida: {self.__saida}, Horario de chegada: {self.getHorarioChegada()}"
    
rotBus01 = RoteiroOnibus(30, "8:30", 'Arad', 'Bucareste', 418)
rotBus01.addParada(destino="Sibiu", distancia=140)
rotBus01.addParada(origem="Sibiu", destino="Fagaras", distancia=99)
rotBus01.addParada(origem="Fagaras", destino="Bucareste", distancia=211)
print(rotBus01)

