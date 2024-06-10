romeniaMap = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesi': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesi': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucareste': 211},
    'Pitesi': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucareste': 101},
    'Bucareste': {'Fagaras': 211, 'Pitesi': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucareste': 90},
    'Urziceni': {'Bucareste': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def busca_em_profundidade(mapa, origem, destino, distancia, caminho=[], distancia_percorrida=0):
    caminho = caminho + [origem]
    if origem == destino and distancia_percorrida == distancia:
        return caminho

    for cidade, dist in mapa[origem].items():
        if cidade not in caminho and distancia_percorrida + dist <= distancia:
            novo_caminho = busca_em_profundidade(mapa, cidade, destino, distancia, caminho, distancia_percorrida + dist)
            if novo_caminho:
                return novo_caminho

    return None

caminho = busca_em_profundidade(romeniaMap, 'Arad', 'Bucareste', 450)
print(caminho)
caminho = busca_em_profundidade(romeniaMap, 'Sibiu', 'Bucareste', 450 - 140) 
print(caminho)
