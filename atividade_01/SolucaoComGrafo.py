import cv2
import numpy

# Função para contar elementos em uma imagem usando lógica de grafos

def contagemDeElementos(caminhoDaImagem):
    # Carregar a imagem
    imagem = cv2.imread(caminhoDaImagem, cv2.IMREAD_GRAYSCALE)

    # Binarizar a imagem (considerando elementos como regiões brancas)
    valorDoLimiar, imagemBinaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY) # Nesse caso não preciso usa o valor do limiar 

    # Dimensões da imagem
    linhas, colunas = imagemBinaria.shape

    # Criar um grafo não direcionado
    grafo = {}

    # Construir o grafo
    for linha in range(linhas):
        for coluna in range(colunas):
            if imagemBinaria[linha][coluna] == 255:  # Se o pixel é branco (elemento)
                vizinhos = []
                for nlinha in range(max(0, linha - 1), min(linhas, linha + 2)):
                    for ncoluna in range(max(0, coluna - 1), min(colunas, coluna + 2)):
                        if imagemBinaria[nlinha][ncoluna] == 255 and (nlinha, ncoluna) != (linha, coluna):
                            vizinhos.append((nlinha, ncoluna))
                grafo[(linha, coluna)] = vizinhos

    # Contagem de componentes conexas usando DFS iterativo
    visitados = set()
    numeroDeElementos = 0

    for vertice in grafo:
        if vertice not in visitados:
            pilha = [vertice]
            while pilha:
                verticeAtual = pilha.pop()
                if verticeAtual not in visitados:
                    visitados.add(verticeAtual)
                    pilha.extend(vizinho for vizinho in grafo[verticeAtual] if vizinho not in visitados)
            numeroDeElementos += 1

    return numeroDeElementos

# Lista de caminhos das imagens
caminhoDaImagens = [ "img1.jpeg", "img2.jpeg", "img3.jpeg", "img4.jpeg"]

# Contar elementos em cada imagem e imprimir o resultado
for caminho in caminhoDaImagens:
    numeroDeElementos = contagemDeElementos(caminho)
    print(f"A imagem {caminho} contém {numeroDeElementos} elementos.")
