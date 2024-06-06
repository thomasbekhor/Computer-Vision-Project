import cv2
import pytesseract #pip install pytesseract e site para baixar a api https://tesseract-ocr.github.io/tessdoc/Installation.html 

import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"Caminho da pasta do tesseract ate o arquivo .exe"

# Carregar a imagem usando OpenCV

def encontra_palavras(image_path):

    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar um limiar para binarizar a imagem
    _, binary_image = cv2.threshold(gray_image, 118, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((1,1), np.uint8)
    morphed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # Selecione a região das palavras conforme a sua necessidade
    #letras = binary_image[250:860, 300:1000]
    palavras=morphed_image[850:1000, 70:1700]
    #palavras=morphed_image[1000:1200, 70:1700]


    #plt.imshow(morphed_image,cmap='gray')
    #plt.show()

    #plt.imshow(palavras,cmap='gray')
    #plt.show()

    # Usar pytesseract para reconhecer texto
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(palavras, config=custom_config)

    # Limpar o texto reconhecido e organizar em uma lista de palavras
    lines = text.strip().split('\n')
    words = []
    for line in lines:
        words_in_line = line.split(' ')  # Usar dois espaços para separar as palavras
        for word in words_in_line:
            if word.strip():  # Ignorar palavras vazias
                words.append(word.strip())

    # Remover pontos finais das palavras
    cleaned_words = [word.replace('.', '') for word in words]

    # Exibir a lista de palavras limpas
    return cleaned_words


#print(encontra_palavras('img3.jpeg'))