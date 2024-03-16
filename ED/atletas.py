class Atleta:
    def __init__(self, id, n_ouro, n_prata, n_bronze, nome):
        self.id = id
        self.n_ouro = n_ouro
        self.n_prata = n_prata
        self.n_bronze = n_bronze
        self.nome = nome

    def comparar_conqui(self, atleta2):
        if self.n_ouro > atleta2.n_ouro:
            return self.id
        elif self.n_ouro < atleta2.n_ouro:
            return atleta2.id
        elif self.n_prata > atleta2.n_prata:
            return self.id
        elif self.n_prata < atleta2.n_prata:
            return atleta2.id
        elif self.n_bronze > atleta2.n_bronze:
            return self.id
        elif self.n_bronze < atleta2.n_bronze:
            return atleta2.id
        
        return "empate"
    def busca_id(self, id):
        if self.id == id:
            return True
        
        return False


atletanum = int(input())

vatletas = []
for c in range(0, atletanum):
    atleta = input()
    atleta = atleta.split()
    medalha = input()
    medalha = medalha.split()
    vatletas.append(Atleta(int(atleta[0]), int(medalha[0]), int(medalha[1]), int(medalha[2]), atleta[1]))

consultanum = int(input())

for c in range(0, consultanum):
    compara = input()
    compara = compara.split()
    for d in vatletas:
        if d.busca_id(int(compara[0])):
            for j in vatletas:
                if j.busca_id(int(compara[1])):
                    print(d.comparar_conqui(j))
