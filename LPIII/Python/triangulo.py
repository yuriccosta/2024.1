def desenhaTriangulo(tipo = 1, tamanho = 4):
    if tipo == 1:
        for c in range(tamanho):
            print("*" * (c + 1))
    elif tipo == 2:
        for c in range(tamanho, 0, -1):
            print("*" * (c))
    elif tipo == 3:
        for c, d in zip(range(tamanho), range(tamanho, 0, - 1)):
            print(" " * d + "*" * (c + 1))
    elif tipo == 4:
        for c, d in zip(range(tamanho), range(tamanho, 0, - 1)):
            print(" " * (c + 1) + "*" * d)


for c in range(1, 5):
    desenhaTriangulo(c, 4)
    print()
