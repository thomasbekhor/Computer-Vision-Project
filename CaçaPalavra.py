import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
from teste_encontra_letras import encontra_letras
from teste_encontra_palavras import encontra_palavras


letra=encontra_letras('img.jpeg')
letras=letra[0]

#plt.imshow(letra[1])
#plt.show()

palavras=encontra_palavras('img.jpeg')


def busca_palavras_na_matriz(matriz, palavras):
    def buscar_palavra(matriz, palavra):
        linhas = len(matriz)
        colunas = len(matriz[0])
        
        def buscar_direcao(l, c, dl, dc):
            posicoes = []
            for i in range(len(palavra)):
                nl, nc = l + dl * i, c + dc * i
                if not (0 <= nl < linhas and 0 <= nc < colunas) or matriz[nl][nc] != palavra[i]:
                    return False, []
                posicoes.append((nl, nc))
            return True, posicoes

        for l in range(linhas):
            for c in range(colunas):
                if matriz[l][c] == palavra[0]:
                    for dl, dc in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                        encontrada, posicoes = buscar_direcao(l, c, dl, dc)
                        if encontrada:
                            return True, posicoes
        
        return False, []

    resultados = {}
    posicoes_encontradas = {}
    for palavra in palavras:
        encontrada, posicoes = buscar_palavra(matriz, palavra)
        resultados[palavra] = encontrada
        if encontrada:
            
            posicoes_encontradas[palavra] = posicoes
    
    return resultados, posicoes_encontradas

def destacar_palavras_na_imagem(imagem, posicoes_encontradas):
    # Definir uma lista de cores
    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), 
    (128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0)]
    
    cor_index = 0  # Índice para selecionar cores
    
    for palavra, posicoes in posicoes_encontradas.items():
        cor = cores[cor_index % len(cores)]  # Selecionar a cor usando o índice
        cor_index += 1  # Incrementar o índice para a próxima palavra
        
        for (linha, coluna) in posicoes:
            start_point = (coluna * 50 + 30, linha * 50 + 25)  # Ajuste de deslocamento em x e y
            end_point = ((coluna + 1) * 50 + 30, (linha + 1) * 50 + 25)  # Ajuste conforme necessário
            imagem = cv2.rectangle(imagem, start_point, end_point, cor, 2)
    
    return imagem


resultados, posicoes_encontradas = busca_palavras_na_matriz(letras, palavras)

for palavra, encontrada in resultados.items():
    print(f'{palavra}: {"Encontrada" if encontrada else "Nao encontrada"}')

imagem_destacada = destacar_palavras_na_imagem(letra[1], posicoes_encontradas)

plt.imshow(cv2.cvtColor(imagem_destacada, cv2.COLOR_BGR2RGB))
plt.show()
