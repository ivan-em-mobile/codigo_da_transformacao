'''
Primicia - Jogo de Cartas Viradas com Pygame, jogo incompleto para fins educacionais.
'''

import pygame
# Bibliotecas padrão
import random
# Bibliotecas do sistema 
import time
# Bibliotecas do sistema - contador
import os
# Bibliotecas do sistema - caminho de recursos
import sys
# Função para resolver caminhos de recursos

def resolver_caminho_recurso(caminho_relativo):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, caminho_relativo)

pygame.init()
LARGURA, ALTURA =800, 600
COR_FUNDO = (20, 20, 20)
COR_TEXTO = (255, 255, 255)

caminho_imagens = "imagens"
NOMES_IMAGENS = [
    "imagem1.png", "imagem2.png", "imagem3.png", 
    "imagem4.png", "imagem5.png", "imagem6.png",
]
VERSO_NOME="verso_flip.png"

TAMANHO_CARTA = (100, 100)
ALTURA_PLACAR = 50
AREA_JOGO_Y = ALTURA_PLACAR