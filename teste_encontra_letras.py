import cv2
import pytesseract #pip install pytesseract e site para baixar a api https://tesseract-ocr.github.io/tessdoc/Installation.html 
import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"Caminho da pasta do tesseract ate o arquivo .exe"



# Carregar a imagem usando OpenCV
#image_path = 'img.jpg'

def encontra_letras(img):
    image = cv2.imread(img)
    
    imagem_saida=image[250:860, 300:1000]
    #imagem_saida=image[200:1040, 100:1200]
    # Converter a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar um limiar para binarizar a imagem
    _, binary_image = cv2.threshold(gray_image, 118, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((1,1), np.uint8)
    morphed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)


    # Selecionar a região das letras conforme a sua necessidade
    letras = morphed_image[250:860, 300:1000]
    #letras = morphed_image[200:1040, 100:1200]
    
    #plt.imshow(letras,cmap='gray')
    #plt.show()

    # Usar pytesseract para reconhecer texto na região selecionada
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = pytesseract.image_to_string(letras, config=custom_config)

    # Limpar o texto reconhecido e organizar em uma matriz de letras
    lines = text.strip().split('\n')
    matrix = [list(line) for line in lines if line.strip()]

    

    #print(matrix)
    # Exibir a matriz de letras
    #for row in matrix:
    #    print(' '.join(row))

    return matrix,imagem_saida

#print(encontra_letras('img3.jpeg')[0])
