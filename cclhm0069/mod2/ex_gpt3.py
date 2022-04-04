# programa para calcular a média de um aluno

import os
import sys

# função inserir as notas
def inserir_notas():
    notas = []
    for i in range(0,4):
        notas.append(float(input("Digite a nota: ")))
    return notas

# função para calcular a média
def calcular_media(notas):
    media = 0
    for i in range(0,4):
        media += notas[i]
    media = media / 4
    return media

# função para exibir a média
def exibir_media(media):
    print("A média é: ", media)

# chamar as funções
notas = inserir_notas()
media = calcular_media(notas)
exibir_media(media)
