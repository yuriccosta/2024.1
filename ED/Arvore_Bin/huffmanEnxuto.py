# Programa que implementa o código de Huffman

# Importando do código que está no slide
from arvorebin import Arvore

class No:
    def __init__(self, freq, carac, esquerda=None, direita=None):
        self.freq = freq
        self.carac = carac
        self.esquerda: No = esquerda
        self.direita: No = direita
        self.pai: No = None
        
  # se nao é nulo, para cada filho, atualiza ponteiro de pai 
        if self.esquerda:
            self.esquerda.pai=self
        if self.direita:
            self.direita.pai=self


# Para alterar o metodo de printar a arvore para o tipo de no que temos
class huffman(Arvore):
        def imprimeNo(freq: int, carac: str, b: int):
            for i in range(b):
                print("     ", end='')
            if carac == "*":
                print(carac)
            elif carac == "":
                print(freq)
            else:
                print(f"{carac}:{freq}")


        def mostraArvore(a: No, b: int):
            if (a == None):
                huffman.imprimeNo(0,'*', b)
                return
            
            huffman.mostraArvore(a.direita, b+1)
            huffman.imprimeNo(a.freq, a.carac, b)
            huffman.mostraArvore(a.esquerda, b+1)


##############################################################################################################
# Etapa 1
print("Etapa 1")
texto = """e da vez que eu me perdi no caminho so consigo lembrar de tu me sorrindo sentada no portao da tua casa lembro do cd
de coco do cafe caboclo da vontade absurda de sentir teu gosto feito fumaca num quarto fechado uu tomou conta dos
quatro cantos acende o cigarro queima a brasa eu sou o quarto tu a fumaca e os cigarros foram tantos feito fumaca num
quarto fechado
tu tomou conta dos quatro cantos acende o cigarro, queima a brasa eu sou o quarto tu a fumaca e os cigarros foram tantos
e da vez que eu me perdi no caminho so consigo lembrar de tu me sorrindo sentada no portão da tua casa lembro do cd
de coco do cafe caboclo da vontade absurda de sentir teu gosto laia laia laia laia"""


# Criando um dicionário da frequência de caracteres
freq = {}
for c in texto:
    if c in freq:
        freq[c] = freq[c] + 1
    else:
        freq[c] = 1

# Printando dicionário por ordem alfabetica
for d in sorted(freq.items()):
    print(f"{d[0]}: {d[1]}")

##############################################################################################################
# Etapa 2
print("\nEtapa 2")

#Cria uma lista com a posição trocada de chave e valor do dicionário e depois ordena com o maior valor na frente
ordenado = []
for d in freq.items():
    ordenado.append([d[1], d[0]])
ordenado.sort(reverse=True)

#Faz uma pilha de Nós com base na lista ordenada criado anteriormente
stackTree = []
for c in ordenado:
    stackTree.append(No(c[0], c[1]))
    #print(stackTree[-1])
    
# Função de inserir item na pilha na ordem reversa
def insereStack(arvore: No, stack: list[No]):
    cont = 0
    for aux in stack:
        if arvore.freq > aux.freq:
            break
        else:
            cont += 1
    stack.insert(cont, arvore)


# Função para fazer a árvore de Huffman e retornar a árvore
def makeHuffmanTree(stack: list[No]) -> No:
    if len(stack) == 1:
        return stack.pop()

    # Removendo da pilha e guardando
    sunEsq = stack.pop()
    sunDir = stack.pop()

    # Colocando o de menor frequência na esquerda
    if sunEsq.freq > sunDir.freq:
        sunEsq, sunDir = sunDir, sunEsq
    # Caso sejam iguais coloca em ordem alfabetica da esquerda para direita
    elif sunEsq.freq == sunDir.freq:
        if sunEsq.carac > sunDir.carac:
            sunEsq, sunDir = sunDir, sunEsq
    
    # Fazendo nova árvore com os filhos removidos da pilha
    new = No(sunEsq.freq + sunDir.freq, "", sunEsq, sunDir)

    #Inserindo na pilha a nova arvore criada
    insereStack(new, stack)
    return makeHuffmanTree(stack)


# Salva a raiz da árvore criada
raiz = makeHuffmanTree(stackTree)

huffman.mostraArvore(raiz, 3)

##############################################################################################################
# Etapa 3
print("\nEtapa 3")
    
# Função para buscar caracter na árvore
# Vai em todos os nós da árvore até encontrar o nó com o caracter desejado ou retornar nulo
def searchNo(raiz: No, char: str) -> No:
    # Se a raiz for nula retorna nulo, significa que não encontrou
    if not raiz:
        return None
    elif raiz.carac == char:
        return raiz
    
    # Se não for o nó procurado, procura nos filhos da esquerda e direita
    # O objeto or None é o próprio objeto
    return searchNo(raiz.esquerda, char) or searchNo(raiz.direita, char)


# Função para retornar a string com o código de um determinado caractere a partir de seu objeto
def binHuffman(raiz: No) -> str:  
        if not raiz or not raiz.pai:
            return ""
        # Se o nó é filho da direita adicionamos 1 no final do retorno e o retorno da função no iníco 
        elif raiz == raiz.pai.direita:
            return binHuffman(raiz.pai) + "1"
        # Se o nó é filho da esquerda adicionamos 0 no final do retorno e o retorno da função no inicio
        else:
            return binHuffman(raiz.pai) + "0"


# Dicionário com a relação de códigos e letras
codigo_dict = {}

# Mostra o código binário de cada letra e salva no dicionário para manter a relação 
print("Código binário")

for d in sorted(freq.keys()):
    #Procura o nó da letra e gera o código de huffman
    code = binHuffman(searchNo(raiz, d))
    codigo_dict[d] = code
    print(f"{d}: {code}")

##############################################################################################################
# Etapa 4
print("\nEtapa 4")
print("\nString original:")
print(texto)

# Cria a string codificada utilizando o dicionário de códigos
code_string = ""
for c in texto:
    code_string = code_string + codigo_dict[c]

print("\nCodificado:")
print(code_string)

# Volta para a string original
# Cria uma lista com a posição trocada de chave e valor do dicionário
codigo_list = []
for d in codigo_dict.items():
    codigo_list.append([d[1], d[0]])


# Percorre a string codificada e decodifica com base na lista com a relação de códigos
decode_string = ""
code = ""
for c in code_string:
    # Como cada código é único uma hora code será igual a um código dentro da lista
    code = code + c
    for d in codigo_list:
        # Verifica se a string criada é igual a que está dentro da lista
        if d[0] == code:
            # Cria a string decodificada e reseta o code
            decode_string = decode_string + d[1]
            code = ""
            break

print("\nDe volta para o orginal:")
print(decode_string)
print("\nO texto inicial é igual ao texto decodificado:", texto == decode_string)
