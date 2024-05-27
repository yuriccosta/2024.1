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

    def __str__(self):
        return f"||{self.carac}: {self.freq}|| esq = {self.esquerda} | dir = {self.direita}"



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
teste1 = """e da vez que eu me perdi no caminho so consigo lembrar de tu me sorrindo sentada no portao da tua casa lembro do cd
de coco do cafe caboclo da vontade absurda de sentir teu gosto feito fumaca num quarto fechado uu tomou conta dos
quatro cantos acende o cigarro queima a brasa eu sou o quarto tu a fumaca e os cigarros foram tantos feito fumaca num
quarto fechado
tu tomou conta dos quatro cantos acende o cigarro, queima a brasa eu sou o quarto tu a fumaca e os cigarros foram tantos
e da vez que eu me perdi no caminho so consigo lembrar de tu me sorrindo sentada no portão da tua casa lembro do cd
de coco do cafe caboclo da vontade absurda de sentir teu gosto laia laia laia laia"""

freq = {}

# Criando um dicionário da frequência de caracteres
for c in teste1:
    if c in freq:
        freq[c] = freq[c] + 1
    else:
        freq[c] = 1


# Ordenado por ordem alfabetica
for d in sorted(freq.items()):
    print(f"{d[0]}: {d[1]}")

'''
# Ordenando pelos valores
from operator import itemgetter
ordenado = sorted(freq.items(), key=itemgetter(1))
print(ordenado)
for d in ordenado:
    print(f"{d[0]}: {d[1]}")
'''

#Ordenando pelos valores (cria uma lista com a posição trocada de chave e valor do dicionário)
ordenado = []
for d in freq.items():
    ordenado.append([d[1], d[0]])
ordenado.sort(reverse=True)
#print(ordenado)

##############################################################################################################
# Etapa 2
print("\nEtapa 2")
'''
freq["total"] = 0
for c in freq.keys():
    if c != "total":
        freq["total"] += freq[c]
print(freq["total"])
'''


#Fazendo a pilha de Nós
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
            '''
        elif arvore.freq == aux.freq:
            if arvore.carac > aux.freq:
                stack[cont].
            '''
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


raiz = makeHuffmanTree(stackTree)

huffman.mostraArvore(raiz, 2)

##############################################################################################################
# Etapa 3
print("\nEtapa 3")
    
# Função para buscar caracter na árvore
def searchNo(raiz: No, char: str) -> No:
    if not raiz:
        return None
    elif raiz.carac == char:
        return raiz
    

    return searchNo(raiz.esquerda, char) or searchNo(raiz.direita, char)

def binHuffman(raiz: No) -> str:  
        if not raiz or not raiz.pai:
            return ""
        elif raiz == raiz.pai.direita:
            return binHuffman(raiz.pai) + "1"
        else:
            return binHuffman(raiz.pai) + "0"


# Dicionário com a relação de códigos e letras
codigo = {}

# Mostra o código binário de cada letra e salva no dicionário para manter a relação
print("Código binário")
for d in sorted(freq.items()):
    code = binHuffman(searchNo(raiz, d[0]))
    codigo[d[0]] = code
    print(f"{d[0]}: {code}")

##############################################################################################################
# Etapa 4
print("\nEtapa 4")
print("\nString original:")
print(teste1)

# Cria a string codificada

code_string = ""
for c in teste1:
    code_string = code_string + codigo[c]

print("\nCodificado:")
print(code_string)

# Volta para a string original
#Cria uma lista com a posição trocada de chave e valor do dicionário
codigo_list = []
for d in codigo.items():
    codigo_list.append([d[1], d[0]])


decode_string = ""
code = ""
for c in code_string:
    code = code + c
    for d in codigo_list:
        if d[0] == code:
            decode_string = decode_string + d[1]
            code = ""
            break

print("\nDe volta para o orginal:")
print(decode_string)
