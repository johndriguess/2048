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
    Daqui pra baixo entendi NADA
"""

def checarStatus(matriz, max_tile=2048):
    """
    Update the game status by checking if the max. tile has been obtained.

    Parameters:
        matriz (list): game matriz
        max_tile (int): tile number required to win, default = 2048
    Returns:
        (str): game status WIN/LOSE/PLAY
    """
    flat_board = [cell for row in matriz for cell in row]
    if max_tile in flat_board:
        # game has been won if max_tile value is found
        return "VENCEU"

    for i in range(4):
        for j in range(4):
            # check if a merge is possible
            if j != 3 and matriz[i][j] == matriz[i][j+1] or \
                    i != 3 and matriz[i][j] == matriz[i + 1][j]:
                return "JOGAR"

    if 0 not in flat_board:
        return "PERDEU"
    else:
        return "JOGAR"


def colocarDoisOuQuatro(matriz, iter=1):

    for _ in range(iter):
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        while(matriz[a][b] != 0):
            a = random.randint(0, 3)
            b = random.randint(0, 3)

        if sum([cell for row in matriz for cell in row]) in (0, 2):
            matriz[a][b] = 2
        else:
            matriz[a][b] = random.choice((2, 4))
    return matriz


def paraEsquerda(matriz):

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


def paraCima(matriz):

    matriz = rotateLeft(matriz)
    matriz = paraEsquerda(matriz)
    matriz = rotateRight(matriz)
    return matriz


def paraDireita(matriz):

    # initial shift
    shiftRight(matriz)

    # merge cells
    for i in range(4):
        for j in range(3, 0, -1):
            if matriz[i][j] == matriz[i][j - 1] and matriz[i][j] != 0:
                matriz[i][j] *= 2
                matriz[i][j - 1] = 0
                j = 0

    # final shift
    shiftRight(matriz)
    return matriz


def paraBaixo(matriz):

    matriz = rotateLeft(matriz)
    matriz = paraEsquerda(matriz)
    shiftRight(matriz)
    matriz = rotateRight(matriz)
    return matriz


def shiftLeft(matriz):

    # remove 0's in between numbers
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if matriz[i][j] != 0:
                nums.append(matriz[i][j])
                count += 1
        matriz[i] = nums
        matriz[i].extend([0] * (4 - count))


def shiftRight(matriz):

    # remove 0's in between numbers
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if matriz[i][j] != 0:
                nums.append(matriz[i][j])
                count += 1
        matriz[i] = [0] * (4 - count)
        matriz[i].extend(nums)


def rotateLeft(matriz):

    b = [[matriz[j][i] for j in range(4)] for i in range(3, -1, -1)]
    return b


def rotateRight(matriz):

    b = rotateLeft(matriz)
    b = rotateLeft(b)
    return rotateLeft(b)
