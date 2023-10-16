import random

# Função para mover 
def mover(direcao, matriz):

    if direcao == "w":

        return paraCima(matriz)

    if direcao == "s":

        return paraBaixo(matriz)

    if direcao == "a":

        return paraEsquerda(matriz)

    if direcao == "d":

        return paraDireita(matriz)



    """
    1. Pelo oq eu entendi ele tá pegando todas as 'células' das fileiras (linhas) na matriz e depois pegando outras 'células' nas 
    fileiras (colunas), ou seja, ele tá selecionando a matriz todinha que vai ser o nosso 'tabuleiro' e varrendo ela
    2. Se o valor do titulo da janela (2048) estiver em célula da matriz, então é pra retornar que a pessoa venceu
    3. Ele está verificando se é possível juntar as células em uma só (2+2, 4+4, etc).
    4. Se não houver mais 0 (espaços vazios) na matriz, então significa que não tem mais movimentos disponíveis
    'Ah madu, mas e se não tiver mais espaço, porém tem dois 2 um do lado do outro' o if de cima assegura que o jogo não se encerre nesse caso
    pq ele vai retornar um status de JOGAR e não de WIN ou LOST.
    Outra dúvida q vc pode ter é: pq ele pega o nº do titulo da janela? simplesmente pq existem dificuldades diferentes, então é uma forma
    diminuir trabalho
    """
# função para verificar se a pessoa chegou nos 2048 ou não
def checarStatus(matriz, max_tile=2048):
    """
    Update the game status by checking if the max. tile has been obtained.

    Parameters:
        matriz (list): game matriz
        max_tile (int): tile number required to win, default = 2048
    Returns:
        (str): game status WIN/LOSE/PLAY
    """
    flat_board = [cell for row in matriz for cell in row] #1
    if max_tile in flat_board: #2
        return "VENCEU"

    for i in range(4): #3
        for j in range(4):
            if j != 3 and matriz[i][j] == matriz[i][j+1] or \
                    i != 3 and matriz[i][j] == matriz[i + 1][j]:
                return "JOGAR"

    if 0 not in flat_board: #4
        return "PERDEU"
    else:
        return "JOGAR"

""" 
5. O randint é uma funcionalidade da biblioteca random que faz escolher um nº aleátorio dentre os numero que vc dá (início,fim). Atenção
que os nº inseridos também entram no ciclo, no caso aqui o 0 e o 3 também entram.
6. Ele vai verificar se a soma de todas as linhas e colunas dá algum número que está no intervalo fechado de 0 e 2, caso sim, ele add 2
7. Caso contrário ele vai fazer uma escolha aleatória entre 2 ou 4 pra add.
"""

def colocarDoisOuQuatro(matriz, iter=1):
    for _ in range(iter):
        a = random.randint(0, 3) #5
        b = random.randint(0, 3)
        while(matriz[a][b] != 0):
            a = random.randint(0, 3)
            b = random.randint(0, 3)

        if sum([cell for row in matriz for cell in row]) in (0, 2): #6
            matriz[a][b] = 2
        else:
            matriz[a][b] = random.choice((2, 4)) #7
    return matriz


def paraEsquerda(matriz):
    contador = 0
    # initial shift
    shiftLeft(matriz)

    # merge cells
    for i in range(4):
        for j in range(3):
            if matriz[i][j] == matriz[i][j + 1] and matriz[i][j] != 0:
                matriz[i][j] *= 2
                matriz[i][j + 1] = 0
                j = 0

    # final shift
    shiftLeft(matriz)
    return matriz


""" 
Essa parte aqui é MUITO MASSA, prestenção! Essa vai ser nossa matriz de exemplo:
0 0 0 0
0 0 0 0
0 0 0 0
0 2 0 0

O def de rotateLeft faz a matriz transposta da nossa matriz (ou seja, oq é linha vira coluna e oq é coluna vira linha), então nossa matriz fica
assim ó:
0 0 0 0
0 0 0 2
0 0 0 0
0 0 0 0

Realiza o movimento p/ esquerda com o def paraEsquerda:
0 0 0 0
2 0 0 0
0 0 0 0
0 0 0 0

E depois faz a matriz tranposta de novo: SIMPLESMENTE GENIAL, BOY!
0 2 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""

def paraCima(matriz):
    matriz = rotateLeft(matriz)
    matriz = paraEsquerda(matriz)
    matriz = rotateRight(matriz)
    return matriz

# Pega a matriz atual, junta as células e 'remove' os 0 (verificar)
def paraDireita(matriz):
    shiftRight(matriz)
    for i in range(4):
        for j in range(3, 0, -1):
            if matriz[i][j] == matriz[i][j - 1] and matriz[i][j] != 0:
                matriz[i][j] *= 2
                matriz[i][j - 1] = 0
                j = 0

    # final shift
    shiftRight(matriz)
    return matriz

""" 
Seguindo as linhas de comando:
Matriz original (exemplo):
0 0 0 0
0 0 2 0
0 0 0 0
0 0 0 0

1. rotateLeft vai fazer a matriz transposta e inverter:
0 0 0 0                 0 0 0 0       
0 0 0 0                 0 0 0 0 
0 2 0 0                 0 0 2 0 
0 0 0 0                 0 0 0 0 

2. Vai fazer um movimento pra esquerda e atualizar a matriz retirando o 0:
0 0 0 0
0 0 0 0
2 0 0 0
0 0 0 0

3. Se o rotateLeft pega da esquerda p/ direita, o right pega da direita p/ esquerda.
0 0 0 0
0 0 0 0
0 0 0 0
0 0 2 0
"""
def paraBaixo(matriz):
    matriz = rotateLeft(matriz)
    matriz = paraEsquerda(matriz)
    shiftRight(matriz)
    matriz = rotateRight(matriz)
    return matriz

""" 
Essa explicação vai ser longa e eu sugiro que vc desenhe uma matriz 4x4 com 0 pra entender melhor 
Quando vc movimenta um nº (pra cima, pra baixo, pra direita ou pra esquerda) oq nós queremos é que esse nº mude de posição e substitua 
um 0 qualquer. Então nós precisamos meio que 'atualizar' a matriz pra tirar o 0 que tava na posição e colocar o nº ,por exemplo.

<------
0 0 0 2     vou fazer um movimento pra esquerda, por exemplo   
0 0 0 0
0 0 0 0
0 0 0 0

2 0 0 0     o 0 que tava naquela canto a gente tira e coloca o nº 2
0 0 0 0
0 0 0 0
0 0 0 0

Pois então, cada função shif<Alguma coisa> é justamente pra fazer esse trabalho, ele pega as linhas (no caso da direita e esquerda),
varre os elementos que são diferentes de 0, adiciona eles numa lista e preenche o resto com 0 pra poder manter o tamanho certinho

1. A lista atualizada com matriz depois do movimento e o contador pra adicinar os 0 depois
2. Mesmo esquema de sempre pra varrer todas as linhas e colunas da matriz, olhando elemento por elemento ele vai verificar se tem algum
nº diferente de 0
3. Se tiver um 2, por exemplo, ele vai add esse 2 na lista de nums e vai adicionar +1 ao contador, isso vai se repetir 4 vezes (por conta do 
tamanho da matriz) 
4. Aqui ele atualiza a linha da matriz (já que os movimentos da direita e esquerda só vão alterar as linhas)
5. Preenche com 0 pra manter o tamanho da matriz: se tinha 3 nº diferentes de 0, então o nosso contador carrega o valor 3 que vai ser multiplicado
por 0 e adicionado a matriz (se vc não lembra como funciona a adição de elementos com o extend, dá uma olhadinha que vai fazer sentido)

ESSE MESMO PROCESSO VAI ACONTECER NO shiftRight!!!!!
"""
# remove os 0 quando vc movimentar o nº p/ esquerda
def shiftLeft(matriz):
    for i in range(4):
        nums, count = [], 0 #1
        for j in range(4):
            if matriz[i][j] != 0: #2
                nums.append(matriz[i][j]) #3
                count += 1
        matriz[i] = nums #4
        matriz[i].extend([0] * (4 - count)) #5


# remove os 0 quando vc movimentar o nº p/ direita
def shiftRight(matriz):
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if matriz[i][j] != 0: 
                nums.append(matriz[i][j])
                count += 1
        matriz[i] = [0] * (4 - count)
        matriz[i].extend(nums)

""" 
Esse negócio aqui faz uma coisa diferente 
1. Ele vai fazer a matriz transposta
2. Depois inverter a sequencia. Vai ficar algo tipo assim

MATRIZ ORIGINAL         MATRIZ DEPOIS DA FUNÇÃO
[5, 9, 2, 0]                [1, 2, 3, 5]
[3, 5, 0, 4]                [2, 4, 5, 9]
[2, 4, 8, 3]                [7, 8, 0, 2]
[1, 2, 7, 6]                [6, 3, 4, 0]

"""
def rotateLeft(matriz):
    b = [[matriz[j][i] for j in range(4)] for i in range(3, -1, -1)]
    return b

""" 
pega a matriz transposta e inverte
0 0 0 0                0 0 0 0
2 0 0 0     ---->      0 0 0 2       
0 0 0 0                0 0 0 0
0 0 0 0                0 0 0 0
"""
def rotateRight(matriz):
    b = rotateLeft(matriz)
    b = rotateLeft(b)
    return rotateLeft(b)
