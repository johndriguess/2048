import json
import sys
import time
import bancoDeDados
import pygame

from pygame.locals import *
from copy import deepcopy
from logic import *


# iniciando pygame
pygame.init()
# carregando o arquivo json com as constantes do jogo
constante = json.load(open("constantes.json", "r"))
screen = pygame.display.set_mode(
    (constante["tamanho"], constante["tamanho"]))
my_font = pygame.font.SysFont(constante["fonte"], constante["tamanho_fonte"], bold=True)
BRANCO = (255, 255, 255)

# Função para checar se ganhou ou perdeu
def checarVitoria(matriz, status, tema, cor_texto, dificuldade, nome, score):
    # Se o status for diferente de jogar
    if status != "JOGAR":
        tamanho = constante["tamanho"]
        # Vai mostrar uma tela diferente da anterior com um tom mais escuro e transparente
        s = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
        s.fill(constante["cores"][tema]["acabou"])
        screen.blit(s, (0, 0))

        # Mostrar status se ganhou
        if status == "VENCEU":
            msg = "VOCÊ VENCEU!"
            screen.blit(my_font.render(msg, 1, cor_texto), (120, 180))
            bancoDeDados.inserirResultado(nome, score, dificuldade)

        # se for diferente de ganhou, game over
        else:
            msg = "GAME OVER!"
            screen.blit(my_font.render(msg, 1, cor_texto), (140, 180))

        # Pergunta feita ao jogador se ele quer jogar novamente
        screen.blit(my_font.render("Jogar novamente? (y/n)", 1, cor_texto), (40, 255))

        # mostrar na tela
        pygame.display.update()


        while True:
            for event in pygame.event.get():
                if event.type == QUIT or \
                        (event.type == pygame.KEYDOWN and event.key == K_n):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == K_y:
                    # 'y' is pressed to start a new game
                    matriz = novoJogo(tema, cor_texto)
                    return (matriz, "JOGAR")
    return (matriz, status)

# Função para iniciar um novo jogo
def novoJogo(tema, cor_texto):

    # limpar a matriz para iniciar um novo jogo
    matriz = [[0] * 4 for _ in range(4)]
    display(matriz, tema)

    # mostrar na tela a mensagem novo jogo
    screen.blit(my_font.render("NOVO JOGO!", 1, cor_texto), (130, 225))
    pygame.display.update()
    
    # 1 segundo para iniciar
    time.sleep(1)

    
    matriz = colocarDoisOuQuatro(matriz, iter=2)
    display(matriz, tema)
    return matriz


def reiniciar(matriz, tema, cor_texto):

    # colocar a tela mais escura
    s = pygame.Surface((constante["tamanho"], constante["tamanho"]), pygame.SRCALPHA)
    s.fill(constante["cores"][tema]["acabou"])
    screen.blit(s, (0, 0))

    screen.blit(my_font.render("REINICIAR? (y / n)", 1, cor_texto), (85, 225))
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == K_n):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == K_y:
                matriz = novoJogo(tema, cor_texto)
                return matriz

# Função para fazer a matriz
def display(matriz, tema):
    screen.fill(tuple(constante["cores"][tema]["fundo"]))
    box = constante["tamanho"] // 4
    preenchimento = constante["preenchimento"]
    for i in range(4):
        for j in range(4):
            cor = tuple(constante["cores"][tema][str(matriz[i][j])])
            pygame.draw.rect(screen, cor, (j * box + preenchimento,
                                              i * box + preenchimento,
                                              box - 2 * preenchimento,
                                              box - 2 * preenchimento), 0)
            if matriz[i][j] != 0:
                if matriz[i][j] in (2, 4):
                    text_colour = tuple(constante["cores"][tema]["escuro"])
                else:
                    text_colour = tuple(constante["cores"][tema]["claro"])
                # display the number at the centre of the tile
                screen.blit(my_font.render("{:>4}".format(
                    matriz[i][j]), 1, text_colour),
                    # 2.5 and 7 were obtained by trial and error
                    (j * box + 2.5 * preenchimento, i * box + 7 * preenchimento))
    pygame.display.update()


def playGame(tema, nome, dificuldade):
    score = 0
    # iniciar o status de "jogar"
    status = "JOGAR"
    # colocar a cor as palavras de acordo com o tema
    if tema == "claro":
        cor_texto = tuple(constante["cores"][tema]["escuro"])
    else:
        cor_texto = BRANCO
    matriz = novoJogo(tema, cor_texto)

    # loop para botar o jogo pra rodar
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == K_q):
                # se apertar 'q' o jogo para e fecha
                pygame.quit()
                sys.exit()

            # verificação se uma tecla foi apertada
            if event.type == pygame.KEYDOWN:
                # se a tecla apertada foi 'n' o jogo pede pra reiniciar
                if event.key == pygame.K_n:
                    matriz = reiniciar(matriz, tema, cor_texto)
                # se a tecla apertada não tiver no arquivo json, ele só continua e n faz nada
                if str(event.key) not in constante["keys"]:
                    continue
                # se tiver no arquivo
                else:
                    # converte a tecla lá do json em um comando que o pygame entenda
                    key = constante["keys"][str(event.key)]
                    score += 1

                # obtem um novo matriz de acordo com o movimento agindo no antigo matriz
                new_board = mover(key, deepcopy(matriz))

                # se o movimento for permitido e ocorrer
                if new_board != matriz:
                    # coloca 2 ou 4 em um espaço vazio
                    matriz = colocarDoisOuQuatro(new_board)
                    display(matriz, tema)

                    # verifica se o jogo acabou
                    status = checarStatus(matriz, dificuldade)
                    (matriz, status) = checarVitoria(matriz, status, tema, cor_texto, dificuldade, nome, score)

