import cv2
from PIL import Image


metodos = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
]

imagem = cv2.imread("bdcaptcha/2.png")

# transformar a imagem em escala de cinza

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)     # converter cor

i = 0
for metodo in metodos:
    i += 1
    # funcao threshold retorna duas informacoes como resposta
    _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, metodo or cv2.THRESH_OTSU)   # limites
    # salva a imagem:
    cv2.imwrite(f'testesmetodo/imagem_tratada_{i}.png', imagem_tratada)

imagem = Image.open("testesmetodo/imagem_tratada_3.png")
# (opcional) - metodo PILLOW para converter para tons de cinza:
imagem = imagem.convert("P")
# copia da imagem
imagem2 = Image.new("P", imagem.size, (255, 255, 255))

# x = colunas
# y = linhas
for x in range(imagem.size[1]):
    for y in range(imagem.size[0]):
        cor_pixel = imagem.getpixel((y, x))
        if cor_pixel < 115:
            imagem2.putpixel((y, x), (0, 0, 0))

imagem2.save("testesmetodo/imagemfinal.png")

