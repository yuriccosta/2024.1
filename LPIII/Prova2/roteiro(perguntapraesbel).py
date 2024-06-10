class Roteiro:
    def __init__(self, origem, destino, distancia = 0, paradas = []):
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia
        '''
        if paradas == None:
            self.__paradas = []
        else:'''
        self.__paradas = paradas

    def getOrigem(self):
        return self.__origem
    
    def getDestino(self):
        return self.__destino
    
    def getDistancia(self):
        return self.__distancia
    
    def getParadas(self):
        # Contador para as paradas
        cont = 0

        # Se a lista de paradas estiver vazia, retorne 0
        if self.__paradas == []:
            return 0
        else:
            # Para cada parada na lista de paradas
            for c in self.__paradas:
                # Adicione 1 ao contador (para a parada atual)
                cont += 1
                # E adicione o número de paradas dentro da parada atual
                cont += c.getParadas()

        # Retorne o contador
        return cont
        
    '''
    def searchLocal(self, origem=None, destino=None):
        cont = 0
        if origem is None:
            for c in self.__paradas:
                if destino == c.getDestino():
                    return cont + 1
                cont += 1'''
            
        
    def addParada(self, origem=None, destino=None, distancia=0, paradas = []):
        #tam = len(self.__paradas)
        '''
        if paradas is None:
            paradas = []
        '''
        if paradas == []:
            if origem is None:
                parada = Roteiro(self.__origem, destino, distancia)
                print("caso 1")
                self.__paradas.append(parada)
            elif destino is None:
                parada = Roteiro(origem, self.__destino, distancia)
                print("caso 2")
                self.__paradas.append(parada)
            else:
                parada = Roteiro(origem, destino, distancia)
                print("caso 3")
                self.__paradas.append(parada)
        elif distancia == 0:
            print("caso 4")
            self.__paradas.extends(paradas)
        
'''
    def __str__(self):
        if self.__paradas == []:
            return f"Roteiro de {self.__origem} a {self.__destino} com um trajeto total de {self.__distancia}km"
        else:
            return f"Roteiro de {self.__origem} a {self.__destino} passando por {self.getParadas()}, com um trajeto total de {self.__distancia}km"

'''





rot_01 = Roteiro("Arad", "bucareste", (140 + 99 + 211))
rot_01.addParada(destino="Sibiu", distancia=140)
rot_01.addParada(origem="Sibiu", destino="Fagaras", distancia=99)
print(rot_01.__paradas[0].paradas)
