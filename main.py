import json
import sys

import pygame
from pygame.locals import *

from game import playGame

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
FUNDO_MENU = (160, 82, 45)


class Botao():
    """
    Class para criar um botão no pygame.
    Pra que serve uma classe? não sei
    e oq essa em especifico faz? não sei
    """
    # inicializar o botão
    def __init__(self, cor, x, y, largura, altura, text=""):
        self.cor = cor
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.text = text

    # colocar o botão na tela
    def draw(self, win, cor_texto, font):
        desenhar_Retangulo(win, self.cor, (self.x, self.y,
                                         self.largura, self.altura))

        if self.text != "":
            text = font.render(self.text, 1, cor_texto)
            win.blit(text, (self.x + (self.largura/2 - text.get_width()/2),
                            self.y + (self.altura/2 - text.get_height()/2)))

    # checar se o mouse está sobre o botão
    def estaSobre(self, pos):
        # pos é a posição do mouse / uma tupla de coordenadas (x,y)
        if pos[0] > self.x and pos[0] < self.x + self.largura:
            if pos[1] > self.y and pos[1] < self.y + self.altura:
                return True

        return False

# Desenhar um rect com bordas circulares e liso na tela (sei nem pra onde vai aqui)
def desenhar_Retangulo(surface, cor, rect, raio=0.4):
    rect = Rect(rect)
    cor = Color(*cor)
    alpha = cor.a
    cor.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pygame.Surface(rect.size, SRCALPHA)

    circle = pygame.Surface([min(rect.size) * 3] * 2, SRCALPHA)
    pygame.draw.ellipse(circle, PRETO, circle.get_rect(), 0)
    circle = pygame.transform.smoothscale(
        circle, [int(min(rect.size)*raio)]*2)

    raio = rectangle.blit(circle, (0, 0))
    raio.bottomright = rect.bottomright
    rectangle.blit(circle, raio)
    raio.topright = rect.topright
    rectangle.blit(circle, raio)
    raio.bottomleft = rect.bottomleft
    rectangle.blit(circle, raio)

    rectangle.fill(PRETO, rect.inflate(-raio.w, 0))
    rectangle.fill(PRETO, rect.inflate(0, -raio.h))

    rectangle.fill(cor, special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

    surface.blit(rectangle, pos)


def mostrar_Menu():
    """
    O menu principal
    """
    # Criar botão para selecionar o tema claro
    tema_claro = Botao(tuple(constante["cores"]["claro"]["2048"]), 130, 275, 45, 45, "claro")
    # Criar botão para selecionar o tema escuro
    tema_escuro = Botao(tuple(constante["cores"]["escuro"]["2048"]), 180, 275, 50, 45, "escuro")
    
    # Iniciarlizar o tema
    tema = ""
    tema_selecionado = False
    
    # criar botão para selecionar dificuldade
    _2048 = Botao(tuple(constante["cores"]["claro"]["64"]), 130, 330, 45, 45, "2048")
    _1024 = Botao(tuple(constante["cores"]["claro"]["2048"]), 180, 330, 45, 45, "1024")
    _512 = Botao(tuple(constante["cores"]["claro"]["2048"]),  230, 330, 45, 45, "512")
    _256 = Botao(tuple(constante["cores"]["claro"]["2048"]), 280, 330, 45, 45, "256")

    # dificuldade
    dificuldade = 0
    dificuldade_selecionada = False
    
    # criar botão de jogar
    jogar = Botao(tuple(constante["cores"]["claro"]["2048"]), 235, 400, 50, 45, "Jogar")

    # loop do pygame para iniciar o menu
    while True:
        # cor de fundo do menu
        screen.fill(FUNDO_MENU)
        # imagem 2048 do menu
        screen.blit(pygame.transform.scale(
            pygame.image.load("images/icon.ico"), (200, 200)), (155, 50))
        # determinar qual é a fonte
        font = pygame.font.SysFont(constante["fonte"], 15, bold=True)


        palavra_tema = font.render("Tema: ", 1, BRANCO)
        screen.blit(palavra_tema, (77, 285))

        palavra_dificuldade = font.render("Dificuldade: ", 1, BRANCO)
        screen.blit(palavra_dificuldade, (30, 345))

        # Definir fontes para usar depois, a diferença das duas é apenas o tamanho
        font1 = pygame.font.SysFont(constante["fonte"], 15, bold=True)
        font2 = pygame.font.SysFont(constante["fonte"], 14, bold=True)

        # Iniciar todos os botões usando a função que a criamos antes
        tema_claro.draw(screen, PRETO, font1)
        tema_escuro.draw(screen, (197, 255, 215), font1)
        _2048.draw(screen, PRETO, font2)
        _1024.draw(screen, PRETO, font2)
        _512.draw(screen, PRETO, font2)
        _256.draw(screen, PRETO, font2)
        jogar.draw(screen, PRETO, font1)

        pygame.display.update()

        for event in pygame.event.get():
            # armazenar a posição do mouse
            pos = pygame.mouse.get_pos()

            if event.type == QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == K_q):
                # sair se o a tecla "q" foi apertada
                pygame.quit()
                sys.exit()

            # checar se um botão foi apertado
            if event.type == pygame.MOUSEBUTTONDOWN:
                # selecionar tema claro
                if tema_claro.estaSobre(pos):
                    tema_escuro.cor = tuple(constante["cores"]["escuro"]["2048"])
                    tema_claro.cor = tuple(constante["cores"]["claro"]["64"])
                    tema = "claro"
                    tema_selecionado = True

                # selecionar tema escuro
                if tema_escuro.estaSobre(pos):
                    tema_escuro.cor = tuple(constante["cores"]["escuro"]["fundo"])
                    tema_claro.cor = tuple(constante["cores"]["claro"]["2048"])
                    tema = "escuro"
                    tema_selecionado = True
                
                if _2048.estaSobre(pos):
                    _2048.cor = tuple(constante["cores"]["claro"]["64"])
                    _1024.cor = tuple(constante["cores"]["claro"]["2048"])
                    _512.cor = tuple(constante["cores"]["claro"]["2048"])
                    _256.cor = tuple(constante["cores"]["claro"]["2048"])
                    dificuldade = 2048
                    dificuldade_selecionada = True
                
                if _1024.estaSobre(pos):
                    _1024.cor = tuple(constante["cores"]["claro"]["64"])
                    _2048.cor = tuple(constante["cores"]["claro"]["2048"])
                    _512.cor = tuple(constante["cores"]["claro"]["2048"])
                    _256.cor = tuple(constante["cores"]["claro"]["2048"])
                    dificuldade = 1024
                    dificuldade_selecionada = True
                
                if _512.estaSobre(pos):
                    _512.cor = tuple(constante["cores"]["claro"]["64"])
                    _1024.cor = tuple(constante["cores"]["claro"]["2048"])
                    _2048.cor = tuple(constante["cores"]["claro"]["2048"])
                    _256.cor = tuple(constante["cores"]["claro"]["2048"])
                    dificuldade = 512
                    dificuldade_selecionada = True
                
                if _256.estaSobre(pos):
                    _256.cor = tuple(constante["cores"]["claro"]["64"])
                    _1024.cor = tuple(constante["cores"]["claro"]["2048"])
                    _512.cor = tuple(constante["cores"]["claro"]["2048"])
                    _2048.cor = tuple(constante["cores"]["claro"]["2048"])
                    dificuldade = 256
                    dificuldade_selecionada = True

                # jogar com o tema e a dificuldade selecionados
                if jogar.estaSobre(pos):
                    if tema != "" and dificuldade != 0:
                        playGame(tema, dificuldade)

                # resetar o tema e dificuldade se clicar numa área que n seja um botão
                if not jogar.estaSobre(pos) and \
                    not tema_escuro.estaSobre(pos) and \
                    not tema_claro.estaSobre(pos) and \
                    not _2048.estaSobre(pos) and \
                    not _1024.estaSobre(pos) and \
                    not _512.estaSobre(pos) and \
                    not _256.estaSobre(pos):

                    tema = ""
                    tema_selecionado = False
                    dificuldade_selecionada = False

                    tema_claro.cor = tuple(constante["cores"]["claro"]["2048"])
                    tema_escuro.cor = tuple(constante["cores"]["escuro"]["2048"])
                    _2048.cor = tuple(constante["cores"]["claro"]["2048"])
                    _1024.cor = tuple(constante["cores"]["claro"]["2048"])
                    _512.cor = tuple(constante["cores"]["claro"]["2048"])
                    _256.cor = tuple(constante["cores"]["claro"]["2048"])
                    

            # mudar a cor do botão se botar o mouse em cima
            if event.type == pygame.MOUSEMOTION:
                if not tema_selecionado:
                    if tema_claro.estaSobre(pos):
                        tema_claro.cor = tuple(constante["cores"]["claro"]["64"])
                    else:
                        tema_claro.cor = tuple(constante["cores"]["claro"]["2048"])

                    if tema_escuro.estaSobre(pos):
                        tema_escuro.cor = tuple(constante["cores"]["escuro"]["fundo"])
                    else:
                        tema_escuro.cor = tuple(constante["cores"]["escuro"]["2048"])
                
                if not dificuldade_selecionada:
                    if _2048.estaSobre(pos):
                        _2048.cor = tuple(constante["cores"]["claro"]["64"])
                    else:
                        _2048.cor = tuple(constante["cores"]["claro"]["2048"])
                    
                    if _1024.estaSobre(pos):
                        _1024.cor = tuple(constante["cores"]["claro"]["64"])
                    else:
                        _1024.cor = tuple(constante["cores"]["claro"]["2048"])
                    
                    if _512.estaSobre(pos):
                        _512.cor = tuple(constante["cores"]["claro"]["64"])
                    else:
                        _512.cor = tuple(constante["cores"]["claro"]["2048"])
                    
                    if _256.estaSobre(pos):
                        _256.cor = tuple(constante["cores"]["claro"]["64"])
                    else:
                        _256.cor = tuple(constante["cores"]["claro"]["2048"])
                
                if jogar.estaSobre(pos):
                    jogar.cor = tuple(constante["cores"]["claro"]["64"])
                else:
                    jogar.cor = tuple(constante["cores"]["claro"]["2048"])


if __name__ == "__main__":
    # ler o arquivo json
    constante = json.load(open("constantes.json", "r"))

    # iniciar o pygame
    pygame.init()

    # iniciar tela
    screen = pygame.display.set_mode(
        # tamanho especificado no arquivo json
        (constante["tamanho"], constante["tamanho"]))
    # nome que vai ficar na janela
    pygame.display.set_caption("2048")

    # icone que vai ficar na janela
    icon = pygame.transform.scale(
        # pegar a imagem que tá na pasta imagens e redimensiona-lo para ficar no tamanho certo, no caso 32x32
        pygame.image.load("images/icon.ico"), (32, 32))
    pygame.display.set_icon(icon)

    # colocar a fonte (e tamanho) de acordo com a constante do arquivo json
    my_font = pygame.font.SysFont(constante["fonte"], constante["tamanho_fonte"], bold=True)

    # mostrar o menu principal
    mostrar_Menu()