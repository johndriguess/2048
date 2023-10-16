import json
import sys
import pygame
import pygame_textinput
from pygame.locals import *
from game import playGame
import bancoDeDados

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
FUNDO_MENU = (160, 82, 45)

class Botao():
    """
    As classes em python funcionam como um conjunto universo, onde a def init é o domínio e as outras funções são os subdomínios
    TRADUÇÃO: é como se tivessemos a classe COMPUTADORES, tendo na init instancias como memória ram, marca, placa de vídeo, processador, etc.
    Essa classe em específico vai adicionar caracteristas ao botão: iniciar ele, definir tamanho, cor, fonte, ver se o mouse tá em cima ou não,
    se foi clicado ou não.

    1. O __init__ é o coisa que vai conter as propriedades da classe, ou seja, todas as propriedades que forem usadas nas outras funções vai
    vir daqui. É literalmente a função de inicialização
    - O self é o primeiro parâmetro que está presente em todos os métodos (variáveis dentro das def) de uma classe.
    """
    # inicializando características que vão ser utilizadas
    def __init__(self, cor, x, y, largura, altura, text=""): #1
        self.cor = cor
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.text = text

    # desenhando botão da tela
    def draw(self, screen, cor_texto, font):
        desenhar_Retangulo(screen, self.cor, (self.x, self.y, self.largura, self.altura)) #2

        if self.text != "":
            text = font.render(self.text, 1, cor_texto)
            screen.blit(text, (self.x + (self.largura/2 - text.get_width()/2), self.y + (self.altura/2 - text.get_height()/2))) #3

    """
    4. Basicamente oq ele tá fazendo aqui é pegando a posição (pos) do mouse e vendo se ele está dentro da área definida pro botão. Essa função
    vai devolver um tupla de coordenadas (x,y), é o mesmo esquema quando vc vai construir uma matriz ColunasXLinhas, pelo oq eu entendi. Todo esse
    sitema é baseado em coordenas.
    - Caso o mouse não esteja na área do botão, ele retorna o evendo como falso. 
    """
    # checar se o mouse está sobre o botão
    def estaSobre(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.largura: #4
            if pos[1] > self.y and pos[1] < self.y + self.altura:
                return True
        return False


# Desenhar um rect com bordas circulares e liso na tela
def desenhar_Retangulo(surface, cor, rect, raio = 0.4):
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

def pegar_Nome():
        pygame.display.set_caption("Nome do Jogador")
        font = pygame.font.SysFont(constante["fonte"], 40, bold=True)
        manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 15)
        textinput_custom = pygame_textinput.TextInputVisualizer(manager=manager, font_object=font)
        textinput_custom.cursor_width = 1
        textinput_custom.antialias = True
        textinput_custom.font_color = (0, 85, 170)
        screen = pygame.display.set_mode((500, 80))
        clock = pygame.time.Clock()
        while True:
            screen.fill((225, 225, 225))
            events = pygame.event.get()
            # Feed it with events every frame
            textinput_custom.update(events)
            # Get its surface to blit onto the screen
            screen.blit(textinput_custom.surface, (10, 10))
            # Check if user is exiting or pressed return
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    nome = textinput_custom.value
                    return nome

            pygame.display.update()
            clock.tick(30)


def mostrar_ranking(dificuldade):
    screen.fill(FUNDO_MENU)
    font = pygame.font.SysFont(constante["fonte"], 60, bold=True)
    palavra_ranking = font.render(f"{dificuldade} RANKING: ", 1, BRANCO)
    if dificuldade > 1000:
        screen.blit(palavra_ranking, (0,0))
    else:
        screen.blit(palavra_ranking, (20,0))

    font = pygame.font.SysFont(constante["fonte"], 35, bold=True)
    ranking = bancoDeDados.top3(dificuldade=dificuldade)

    if ranking[1]['name'] == None and ranking[1]['score']:
        _1 = font.render("1. Sem entrada", 1,BRANCO)
        screen.blit(_1, (0, 150))
    else:
        _1 = font.render(f"1. {ranking[1]['name']} => Score: {ranking[1]['score']}", 1, BRANCO)
        screen.blit(_1, (0, 150))

    if ranking[2]['name'] == None and ranking[2]['score']:
        _2 = font.render("2. Sem entrada", 1,BRANCO)
        screen.blit(_2, (0, 250))
    else:
        _2 = font.render(f"2. {ranking[2]['name']} => Score: {ranking[2]['score']}", 1, BRANCO)
        screen.blit(_2, (0, 250))

    if ranking[3]['name'] == None:
        _3 = font.render("3. Sem entrada", 1,BRANCO)
        screen.blit(_3, (0, 350))
    else:
        _3 = font.render(f"3. {ranking[3]['name']} => Score: {ranking[3]['score']}", 1, BRANCO)
        screen.blit(_3, (0, 350))


    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(0.5)


def mostrar_Menu(nome):
    """
    O menu principal
    """
    # Criar botão para selecionar o tema claro
    tema_claro = Botao(tuple(constante["cores"]["claro"]["2048"]), 130, 275, 45, 45, "claro")
    # Criar botão para selecionar o tema escuro
    tema_escuro = Botao(tuple(constante["cores"]["escuro"]["2048"]), 180, 275, 50, 45, "escuro")

    # Iniciarlizar o tema, vazio e como False, pois ainda não foi escolhido.
    tema = ""
    tema_selecionado = False

    # criar botão para selecionar dificuldade
    _2048 = Botao(tuple(constante["cores"]["claro"]["64"]), 130, 330, 45, 45, "2048")
    _1024 = Botao(tuple(constante["cores"]["claro"]["2048"]), 180, 330, 45, 45, "1024")
    _512 = Botao(tuple(constante["cores"]["claro"]["2048"]),  230, 330, 45, 45, "512")
    _256 = Botao(tuple(constante["cores"]["claro"]["2048"]), 280, 330, 45, 45, "256")

    # dificuldade, vazio e como False, pois ainda não foi escolhido.
    dificuldade = 0
    dificuldade_selecionada = False

    # criar botão de jogar
    jogar = Botao(tuple(constante["cores"]["claro"]["2048"]), 235, 400, 50, 45, "Jogar")

    # criar botão para botar o nome
    ranking = Botao(tuple(constante["cores"]["claro"]["2048"]), 300,400,55,45,"Ranking")

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
        ranking.draw(screen, PRETO,font1)
        #nome_botao.draw(screen, PRETO, font2)

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
                    if tema_selecionado and dificuldade_selecionada:
                        playGame(tema, nome, dificuldade)

                if ranking.estaSobre(pos):
                    if dificuldade_selecionada:
                        mostrar_ranking(dificuldade)

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

                if ranking.estaSobre(pos):
                    ranking.cor = tuple(constante["cores"]["claro"]["64"])
                else:
                    ranking.cor = tuple(constante["cores"]["claro"]["2048"])

if __name__ == "__main__":
    # ler o arquivo json
    constante = json.load(open("constantes.json", "r"))

    """ 
    1. Comando pra iniciar o pygame.
    2. Definindo tamanho da janela (o tamanho é uma variável que tá dentro do arquivo json).
    3. Título que vai ficar na parte de cima da janela.
    4. Redimensionando a imagem pra ficar no tamanho certo (32x32) e utilizar como ícone
    5. Setando o ícone em si.
    6. Setando fonte (arquivo json), tamanho (arquivo json) e colocando ela em negrito.
    """
    nome = pegar_Nome()
    pygame.init() #1
    screen = pygame.display.set_mode((constante["tamanho"], constante["tamanho"])) #2
    pygame.display.set_caption("2048") #3
    icon = pygame.transform.scale(pygame.image.load("images/icon.ico"), (32, 32)) #4
    pygame.display.set_icon(icon) #5
    my_font = pygame.font.SysFont(constante["fonte"], constante["tamanho_fonte"], bold=True) #6
    # mostrar o menu principal
    mostrar_Menu(nome)