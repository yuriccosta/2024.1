class Roteiro:
    def __init__(self, origem, destino, distancia = 0, paradas = None):
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia
        
        if paradas == None:
            self.__paradas = []
        else:
            self.__paradas = paradas
            for c in paradas:
                self.__distancia += c.getDistancia()

    def getOrigem(self):
        return self.__origem
    
    def getDestino(self):
        return self.__destino
    
    def getDistancia(self):
        return self.__distancia
    
    def getParadas(self):
        return self.__paradas
    
    def qntParadas(self):
        # Contador para as paradas
        cont = 0

        # Se a lista de paradas estiver vazia, retorne 0
        for parada in self.__paradas:
            cont += 1
        return cont

    
    def searchParada(self, origem, destino):
        if origem == self.__origem:
            return True
        if destino == self.__destino:
            return True
                
        for parada in self.__paradas:
            if origem == parada.getOrigem() or origem == parada.getDestino():
                return True
            elif destino == parada.getDestino() or destino == parada.getOrigem():
                return True
            
        return False
        
    '''
    def searchLocal(self, origem=None, destino=None):
        cont = 0
        if origem is None:
            for c in self.__paradas:
                if destino == c.getDestino():
                    return cont + 1
                cont += 1'''
            
        
    def addParada(self, origem=None, destino=None, distancia=0, paradas=None):
        #tam = len(self.__paradas)            
        if paradas is None:
            paradas = []

        if paradas == []:
            
            if origem is None:
                origem = self.__origem

                if not self.searchParada(origem, destino):
                    return False
                
                parada = Roteiro(self.__origem, destino, distancia)
                self.__paradas.insert(0, parada)
            elif destino is None:
                return False
            else:
                if not self.searchParada(origem, destino):
                    return False
                
                parada = Roteiro(origem, destino, distancia)
                self.__paradas.append(parada)
                
        elif distancia == 0:
            paradastotais = []
            for parada in paradas:
                if not self.searchParada(parada.getOrigem(), parada.getDestino()):
                    return False
                paradastotais.extend(parada.getParadas())
            self.__paradas.extend(paradastotais)
        
        return True


    def __str__(self):
        if self.__paradas == []:
            return f"Roteiro de {self.__origem} a {self.__destino} com um trajeto total de {self.__distancia}km"
        else:
            text_paradas = ''
            for c in self.__paradas:
                text_paradas = text_paradas + c.__str__() + ', '
            text_paradas = text_paradas[:-2] + ']'
            return f"Roteiro de {self.__origem} a {self.__destino} passando por [{text_paradas} com um trajeto total de {self.__distancia}km"



def main():
    rot_01 = Roteiro("Arad", "Bucareste", (140 + 99 + 211))
    rot_01.addParada(destino="Sibiu", distancia=140)
    rot_01.addParada(origem="Sibiu", destino="Fagaras", distancia=99)
    rot_01.addParada(origem="Fagaras", destino="Bucareste", distancia=211)
    print("Roteiro 1:")
    print(rot_01)

    rot_02 = Roteiro("Sibiu", "Pitesti", (80 + 97))
    rot_02.addParada(destino="Rimnicu Vilcea", distancia=80)
    rot_02.addParada(origem="Rimnicu Vilcea", destino="Pitesti", distancia=97)
    print("\nRoteiro 2:")
    print(rot_02)

    rot_03 = Roteiro("Arad", "Bucareste", distancia= (140 + 80 + 97 + 101))
    rot_03.addParada(destino="Sibiu", distancia= 140)
    rot_03.addParada(paradas=[rot_02])
    rot_03.addParada(origem="Pitesti", destino="Bucareste", distancia=101)
    print("\nRoteiro 3:")
    print(rot_03)


    d1 = rot_01.getDistancia()
    d3 = rot_03.getDistancia()

    if d1 < d3:
        print("\nO roteiro 1 é mais curto que o roteiro 3")
    elif d1 > d3:
        print("\nO roteiro 3 é mais curto que o roteiro 1")
    else:
        print("\nOs roteiros 1 e 3 tem a mesma distância")


if __name__ == "__main__":
    main()