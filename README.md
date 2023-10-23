
# Jogo: **2048**

Bem-vindo ao repositório do jogo 2048, desenvolvido como parte do projeto da disciplina de Algoritmos no curso de Ciências da Computação da UEPB no período 2022.1. Este projeto é uma implementação do famoso jogo 2048, onde o jogador combina blocos numéricos para alcançar a maior pontuação possível.

## Sobre o Projeto

O objetivo deste projeto foi aplicar os conceitos e algoritmos estudados durante o curso de Algoritmos. O 2048 é um jogo que desafia os jogadores a usarem estratégia e lógica para combinar blocos numéricos e alcançar o número 2048 ou, se possível, ir além. Esta implementação foi desenvolvida em python e demonstra a aplicação prática dos algoritmos aprendidos.

## Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python) 
![SQLite](https://img.shields.io/badge/SQLite-000?style=for-the-badge&logo=sqlite&logoColor=07405E)
## Como Jogar
 * **Abrindo o jogo** - *Nome do Jogador*  

    Ao executar o arquivo ***main.py***, será exibida a janela para informar o nome do jogador, basta digitar o nome desejado e apertar **ENTER**

    |![Nome do Jogador](https://drive.google.com/uc?export=view&id=1C_Sc1PI5IwaOPiRoBlRJ0U6UXADFTWc8)|
    |----------|

* **Abrindo o jogo** - *Menu Principal*
    
    Após passar da aba de escolha de nome, será exibido o menu principal do jogo, onde você poderá escolher um tema entre claro ou escuro, e uma dificuldade do jogo, embora o jogo se chame de *2048* optei por disponibilizar mais variedades de pontuações para mais inclusividade.

    |![Menu_Principal](https://drive.google.com/uc?id=1B_jPeqHx1w4Fuj3xsHeYHs_B8D0CxyTy)|
    |----------|

* **Começando a Jogar** - *Selecionando Tema e dificuldade*
    
    Para selecionar qualuqer opção basta clicar com o ***botão esquerdo do mouse***. Quando um *Tema* ou *Dificuldade* é selecionado, você tem uma resposta imediata, a opção fica com uma cor diferente das demais, não é possível selecionar dois temas ao mesmo tempo, nem duas dificuldades, para cancelar a seleção basta clicar em qualquer lugar do menu. 
    
    OBS: **O jogo só iniciará se for selecionado um tema e uma dificuldade**

    |![Tema e Dificuldade](https://drive.google.com/uc?id=1iWG8yJckT6LFxeujBtTu_Bg9VgP34QDH)|
    |----------|

* **Começando a Jogar** - *Novo Jogo*
    
    Ao selecionar o tema e a dificuldade e clicar em jogar, será exibido essa tela de novo jogo!  

    |![Novo Jogo](https://drive.google.com/uc?id=1EzcN3G47REaFXDXiCUboZ5YKGhBgGv69)|
    |----------|
    |***Novo Jogo**: Tema: Claro - Dificuldade: 256*|

* **Começando a Jogar** - *Regras do 2048*

    **Tabuleiro**: O jogo é jogado em um tabuleiro de 4x4, o que significa que você terá 16 células no total para jogar.

    **Números iniciais**: No início do jogo, você terá dois quadrados no tabuleiro, cada um com um número 2 neles. Esses números podem ser 2, 4.

    |![Tabuleiro Inicial](https://drive.google.com/uc?id=1rIfpEGnB1CmSy0eD1u7AkZXcIN4IyUVn)|
    |----------|
    |***Tabuleiro Inicial** - 4x4 com apenas dois números* |

    **Movimentos**: Você pode deslizar os números para cima, baixo, esquerda ou direita no tabuleiro. Todos os números se movem na direção escolhida o máximo possível, até que atinjam a borda do tabuleiro ou encontrem outro número. Quando dois números iguais se tocam durante um movimento, eles se combinam em um único número com o valor da soma dos dois números. Por exemplo, se você mover um 2 para um 2 adjacente, eles se combinarão em um 4.

    **W**: Para cima ↑| **S**: Para baixo ↓ | **D**: Para direita → | **A**: Para esquerda ←.

    |![Tabuleiro Movimentado](https://drive.google.com/uc?id=1x41LjwKDp3Ty4ikrFdhd70Vcis7eUrZp)|
    |----------|
    |***Tabuleiro Movimentado** - movimento W para cima ↑*|

    **Objetivo**: O objetivo do jogo é combinar números para alcançar o valor de 2048 (ou menos dependendo da dificuldade que você escolheu) em uma única célula.

    **Fim do jogo**: O jogo termina quando o tabuleiro está cheio e não há movimentos possíveis que possam combinar números ou com você atingindo o valor escolhido na dificuldade
 
    | VENCEU | PERDEU |
    |----------|----------|
    |![Você Venceu!](https://drive.google.com/uc?id=180MkRCcG_EOb69f2WViBvL8iO-xYWUr4)|![Game Over!](https://drive.google.com/uc?id=1nXLm9kQu8O97cPM92333f5wQN6Q7yxCZ)|


### Entre em contato comigo: 

[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=GitHub&logoColor=0000)](https://github.com/johndriguess/)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=gmail&logoColor=f00)](mailto:johndriguess@gmail.com)

### Adicionais 
* Agradecemos por visitar o nosso repositório e esperamos que você se divirta jogando o 2048 e explorando o código-fonte por trás deste projeto.
