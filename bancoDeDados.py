""" 
1. IMPORTANTE: o SQLite é difernte do SQL, nele dá pra criar uma database local, sem precisar de um servidor. Nesse caso, é melhor usar pq não
vamos lidar com um grande volume de acessos.
2. Essa função 
3. Isso daqui cria uma conexão entre esse arquivo (que vai mexer na tabela, adicionar coisas e tals) e a database em si (onde as informações vão
ficar registradas).
4. Variável responsavel por inserir a tabela, mexer nos registros, etc.
"""
from __future__ import annotations

import sqlite3 #1
from numpy import source #2
banco = sqlite3.connect('primeiroTeste.db') #3
cursor = banco.cursor() #4

''' 
5. Esses comandos são executados uma única vez pra poder inicializar a database e criar a tabela com os parâmetros.
6. A maneira de escrever os comandos pra manipular a database é diferente.
7. CREATE TABLE: cria uma tabela, INSERT INTO <nome da tabela>: inserir na tabela tal, VALUES: valores na ordem que foi escrita em cima.
8. O resto é os registros (dados) que a tabela vai receber, aí precisa colocar o identificador e o tipo (text = texto, integer = inteiro).
'''

cursor.execute("CREATE TABLE IF NOT EXISTS ranking(nome text, score integer, dificuldade text)")
banco.commit()


"""
9. Comando pra pegar o top3 jogadores com maior score e printar .
10. O assert é uma variável de verificação: se ela for verdadeira não acontece nada, mas se a condição dela não for satisfeita, ela vai levantar
o erro de AssertionError.
11. Pega os registros com os 3 maiores scores e organiza eles por ordem decrescente (do maior para o menor).
12. Ele vai pegar cada elemento de source (que são os top3 jogadores), varrer um por um (ciclo de 3) e adicionar espaços vazios se não tiver
os 3 jogadores.
13. Vai retornar o rankind bunitin ex: 1: nome | score.
"""
def top3(count: int = 0, dificuldade: str = "2048") -> dict[int: tuple[None | str], int]: #9
    try: #10
        assert -1 <= count <= 3
    except AssertionError:
        raise ValueError('Invalid argument count, must be no more than 3 and no less than -1')
    cursor.execute(f"SELECT nome, max(score) score FROM ranking WHERE dificuldade = \"{dificuldade}\" GROUP by nome ORDER by score ASC LIMIT 3")  #11
    source = cursor.fetchall()
    espaçamento = [source[i] for i in range(len(source)) if len(source) >= 1] + [(None, -1)] * (3 - len(source)) #12
    resultado = {i: dict(name = espaçamento[i - 1][0], score = espaçamento[i - 1][1]) for i in range(1, 4)} #13
    return resultado if count == 0 else resultado[count]

""" 
14. Função p/ inserir o (registro) nome e o score de cada jogador na tabela.
15. O commit é um comando que confirma a inserção dos dados (registros) previamente "preenchidos".
"""
def inserirResultado(nome: str, score: int, dificuldade: str) -> None: #14
    cursor.execute(f'INSERT INTO ranking (nome, score, dificuldade) VALUES (\"{nome}\", {score}, \"{dificuldade}\")')
    banco.commit() #15 
