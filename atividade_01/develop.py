import cv2
import mahotas

def contagemDeElementos(caminhoDaImagem):
    imagem = cv2.imread(caminhoDaImagem)
    
    if imagem.shape[2] == 3:
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        imagemCinza = imagem
    
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  
    suave = cv2.blur(imagemCinza, (7, 7)) 
    
    T = mahotas.thresholding.otsu(suave) 
    bin = suave.copy() 
    bin[bin > T] = 255 
    bin[bin < 255] = 0 
    bin = cv2.bitwise_not(bin)  
    
    bordas = cv2.Canny(bin, 70, 150)
    
    (lixo, imagemBinaria) = cv2.findContours(bordas.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    if len(imagemBinaria.shape) == 3:
        linhas, colunas, _ = imagemBinaria.shape
    else:
        linhas, colunas = imagemBinaria.shape

    grafo = {}

    for linha in range(linhas):
        for coluna in range(colunas):
            if imagemBinaria[linha][coluna] == 255:  
                vizinhos = []
                for nlinha in range(max(0, linha - 1), min(linhas, linha + 2)):
                    for ncoluna in range(max(0, coluna - 1), min(colunas, coluna + 2)):
                        if imagemBinaria[nlinha][ncoluna] == 255 and (nlinha, ncoluna) != (linha, coluna):
                            vizinhos.append((nlinha, ncoluna))
                grafo[(linha, coluna)] = vizinhos

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

caminhoDaImagens = [ "img1.jpeg", "img2.jpeg", "img3.jpeg", "img4.jpeg", "img11.jpeg", "img22.jpeg", "img33.jpeg", "img44.jpeg" ]

for caminho in caminhoDaImagens:
    numeroDeElementos = contagemDeElementos(caminho)
    print(f"A imagem {caminho} contém {numeroDeElementos} elementos.")
