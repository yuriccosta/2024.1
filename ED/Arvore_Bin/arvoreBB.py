# Arvore de busca binária

class No:
    def __init__(self, nome, cpf, esquerda=None, direita=None):
        self.esquerda: No = esquerda
        self.direita: No = direita 
        self.nome: str = nome
        self.cpf: int = cpf
        self.nivel = 1
        

# Função para buscar na árvore binária a partir do cpf
def searchBB(raiz, cpf):
    # Se a raiz for nula ou o cpf for igual ao cpf da raiz
    if raiz is None or raiz.cpf == cpf:
        return raiz
    elif cpf > raiz.cpf:
        # Se o cpf que queremos buscar for maior que o no atual vamos para a direita
        return searchBB(raiz.direita, cpf)
    else:
        # Se o cpf que queremos buscar for menor que o no atual vamos para a esquerda
        return searchBB(raiz.esquerda, cpf)
    

# Função para inserir na árvore binária com base no cpf
def insertBB(raiz, nome, cpf):
    if raiz is None:
        return No(nome, cpf)
    if cpf > raiz.cpf:
        # Se o cpf que queremos inserir for maior que o no atual vamos para a direita
        raiz.direita = insertBB(raiz.direita, nome, cpf)
        # Quando retornar atualizamos o nivel do criado
        raiz.direita.nivel = raiz.nivel + 1
    else:
        # Se o cpf que queremos inserir for menor que o no atual vamos para a esquerda
        raiz.esquerda = insertBB(raiz.esquerda, nome, cpf)
        # Quando retornar atualizamos o nivel do criado
        raiz.esquerda.nivel = raiz.nivel + 1 

    return raiz



def main():
    N = int(input())
    raiz = None

    while N > 0:
        choice = input().split()
        # Se a escolha for de inserir
        if choice[0] == 'I':
            cpf = int(choice[1])
            nome = input()
            raiz = insertBB(raiz, nome, cpf)

        # Se a escolha for de buscar
        elif choice[0] == 'B':
            cpf = int(choice[1])
            busca = searchBB(raiz, cpf)

            print(f"{busca.nome} {busca.nivel}")

        N -= 1

if __name__ == '__main__':
    main()
