#!/usr/bin/env python
# coding: utf-8

# # Tratamento de texto com OCR
# 
# <small>Material para o Encontro Virtual 4, 24/11/2021, referente à [semana 7 do curso](https://ericbrasiln.github.io/intro-historia-digital/mod2/sem7.html#)</small>

# O objetivo desse encontro virtual é debater o processo de Reconhecimento Ótico de Caracteres - em inglês Optical Character Recognition (OCR) - e a capactiação para o uso de técnicas de OCR para reconhecimento de caracteres em imagens e PDF.
# 
# Para isso teremos um tutorial e um workshop sobre o programa [gImageReader](https://github.com/manisandro/gImageReader). 
# 
# O gImageReader é um programa de código livre e aberto, gratuito, que é uma interface gráfica simples que utiliza o `tesseract-ocr`.
# 
# Seu objetivo é possibilitar diferentes estratégias para o reconhecimento de caracteres em diferentes tipos de arquivos.

# ## Exemplo usando o Tesseract
# 
# Imagem de exemplo:
# 
# ![trinidad](https://raw.githubusercontent.com/ericbrasiln/intro-historia-digital/4e41dca69dd2fd84b1728531a71b120166e86532/cclhm0069/mod2/img/IMG_4689.jpg)

# In[2]:


# exemplo de OCR com Tesseract
import cv2 # é um módulo para manipulação de imagens
import pytesseract # é uma biblioteca para reconhecimento de texto

# carregar a imagem
img_path = 'img/IMG_4689.jpg'
# ler a imagem usando o módulo cv2
img = cv2.imread(img_path)

# aplicar o OCR sobre a imagem
text = pytesseract.image_to_string(img)

# exibir o texto
print(text)

# salvar o texto em um arquivo
with open('ex_ocr_img.txt', 'w') as f:
    f.write(text)
# fechar o arquivo
f.close()


# ## Tutorial - *gImageReader* (OCR para Windows 10)

# In[8]:


from IPython.display import YouTubeVideo
YouTubeVideo("_7eqj01Hn0M", width=560, height=315)


# ## Workshop de reconhecimento de caracteres com gImageReader

# Os exemplos usados na aula podem ser acessados nos seguintes links:
# 
# 1. [Jornal do Brasil, 28 de outubro de 2002, p.1](https://github.com/ericbrasiln/intro-historia-digital/blob/4e41dca69dd2fd84b1728531a71b120166e86532/cclhm0069/mod2/ex_OCR/img_01.jpeg)
# 2. [Jornal do Brasil, 08 de janeiro de 1917, p.1](https://github.com/ericbrasiln/intro-historia-digital/blob/4e41dca69dd2fd84b1728531a71b120166e86532/cclhm0069/mod2/ex_OCR/img_02.jpeg)
# 3. [Eugene D. Genovese - Da Rebelião à Revolução](https://github.com/ericbrasiln/intro-historia-digital/blob/4e41dca69dd2fd84b1728531a71b120166e86532/cclhm0069/mod2/ex_OCR/ex_pdf.pdf)

# ## Tarefa 4
# 
# 1. Assistar o tutorial de instalação do gImageReader;
# 2. Instalar o programa no computador.
