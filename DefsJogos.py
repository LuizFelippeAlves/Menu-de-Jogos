from time import sleep
from random import choice

# ===== Defs Jogo da Velha =====

def EscolherBloco(Blocos,Posicao_L,Posicao_C,Time):
    print("Processando...")
    sleep(1)
    if Blocos[Posicao_L][Posicao_C] == "":
        Blocos[Posicao_L][Posicao_C] = Time
    else:
        print("Jogada Invalida!\nEste Bloco ja esta Ocupada\nTente outra véz!")
        sleep(2)
        return "Invalida"
    
def CondicaoVitoria(lista):
    Blocos=lista

    # Checagem em Diagonal
    if Blocos[0][0] == "X" and Blocos[1][1] == "X" and Blocos[2][2] == "X":
        return "Vitoria Do X em Diagonal"
    elif Blocos[0][0] == "O" and Blocos[1][1] == "O" and Blocos[2][2] == "O": 
        return "Vitoria Do O em Diagonal"
    
    elif Blocos[0][2] == "X" and Blocos[1][1] == "X" and Blocos[2][0] == "X":
        return "Vitoria Do X em Diagonal"
    elif Blocos[0][2] == "O" and Blocos[1][1] == "O" and Blocos[2][0] == "O":
        return "Vitoria Do O em Diagonal"
    

    # Checagem me Horizontal
    elif Blocos[0][0] == "X" and Blocos[0][1] == "X" and Blocos[0][2] == "X":
        return "Vitoria Do X em Horizontal"
    elif Blocos[0][0] == "O" and Blocos[0][1] == "O" and Blocos[0][2] == "O":
        return "Vitoria Do O em Horizontal"
    
    elif Blocos[1][0] == "X" and Blocos[1][1] == "X" and Blocos[1][2] == "X":
        return "Vitoria Do X em Horizontal"
    elif Blocos[1][0] == "O" and Blocos[1][1] == "O" and Blocos[1][2] == "O":
        return "Vitoria Do O em Horizontal"
    
    elif Blocos[2][0] == "X" and Blocos[2][1] == "X" and Blocos[2][2] == "X":
        return "Vitoria Do X em Horizontal"
    elif Blocos[2][0] == "O" and Blocos[2][1] == "O" and Blocos[2][2] == "O":
        return "Vitoria Do O em Horizontal"


    # Checagem em Vertical
    elif Blocos[0][0] == "X" and Blocos[1][0] == "X" and Blocos[2][0] == "X":
        return "Vitoria Do X em Vertical"
    elif Blocos[0][0] == "O" and Blocos[1][0] == "O" and Blocos[2][0] == "O":
        return "Vitoria Do O em Vertical"
    
    elif Blocos[0][1] == "X" and Blocos[1][1] == "X" and Blocos[2][1] == "X":
        return "Vitoria Do X em Vertical"
    elif Blocos[0][1] == "O" and Blocos[1][1] == "O" and Blocos[2][1] == "O":
        return "Vitoria Do O em Vertical"
    
    elif Blocos[0][2] == "X" and Blocos[1][2] == "X" and Blocos[2][2] == "X":
        return "Vitoria Do X em Vertical"
    elif Blocos[0][2] == "O" and Blocos[1][2] == "O" and Blocos[2][2] == "O":
        return "Vitoria Do O em Vertical"
    
    # checargem de Empate ou jogo em andamento
    else:
        if "" in Blocos[0] or "" in Blocos[1] or "" in Blocos[2]:
            return "Jogo em Andamento"
        else:
            return "Empate! Jogo encerrado"
# ===== Fim Defs Jogo da velha =====

# ===== Defs Jogo da Forca ===

def ListadePalavras():
    Palavras = [
        ("Comida", ["feijoada", "carne", "frango", "espaguete", "strogonoff", "tapioca", "coxinha", "pastel", "bauru", "Farofa", "biscoito", "bolo", "brigadeiro", "cocada", "pamonha"]),
        ("Animais", ["gato", "cachorro", "elefante", "girafa", "papagaio", "panda", "corvo", "camelo", "dromedario", "galinha", "vaca", "porco", "guaxinim", "tubarao", "peixe", "baleia", "calango", "capivara", "crocodilo", "jacare", "leopardo", "leao", "hiena", "macaco", "tigre", "cobra", "gaivota", "pelicano", "esquilo", "tartaruga"]),
        ("Objeto", ["lupa", "copo", "cadeira", "livro", "lapis", "celular", "chave", "oculos", "estojo", "caderno", "quadro", "almofada", "caixa", "prato", "garfo", "faca", "colher"]),
        ("Cor", ["azul", "vermelho", "laranja", "roxo", "verde", "amarelo", "rosa", "cinza", "preto", "ciano", "marrom", "branco", "lilas", "magenta"])
    ]
    
    dica, palavras = choice(Palavras)

    return dica, palavras

# ===== Fim Defs Jogo da Forca =====

# ===== Defs Blackjack =====

def CriarBaralho(naips):

    baralhos = []

    for naip in naips:
        for valor in range(2,11):
            baralhos.append(f"{valor} de {naip}")
        for valor in ["J","Q","K","A"]:
            baralhos.append(f"{valor} de {naip}")
    return baralhos


def ComprarCarta(baralho,cartaEmJogo):

    while True:
        destribuircarta = choice(baralho)
        if destribuircarta not in cartaEmJogo:
            return destribuircarta


def CalcularPontos(mao):
    
    pontos = []

    for carta in mao:
        if carta[0] in ["J","Q","K"]:
            pontos.append(10)
        elif carta[0] not in ["J","Q","K","A"]:
            pontos.append(int(carta[0]))
        else:
            if carta[0] == "A":
                pontos.append(11)
        if "A" in mao:
            if sum(pontos) > 21:
                pontos.remove(11)
                pontos.append(1) 
    return sum(pontos)


def VerificarJogo(ponto):
    if ponto <= 20:
        return "Em Jogo"
    elif ponto == 21:
        return "Mao Fechada em 21!"
    elif ponto > 21:
        return "Alem Do Limite"
    

def MostrarMao(Mesa,Jogador):

    print(f'{f"BlackJack":=^40}')
    print("Mâo da mesa: ")
    for carta in Mesa:
        print(carta)
    print("="*40)

    print("Sua Mão:")
    for carta in Jogador:
        print(carta)
    print("="*40)

def ResultadoJogo(pontosmesa,pontosjogador,maojogador,maomesa):
    if pontosjogador > 21:
        resultado = "Você perdeu, ultrapassou 21 pontos."
    elif pontosmesa > 21:
        resultado = "Parabéns, você ganhou! a mesa ultrapassou 21 pontos."
    elif pontosjogador > pontosmesa:
        resultado = "Parabéns, você ganhou!"
    elif pontosjogador < pontosmesa:
        resultado = "Você perdeu, a mesa tem uma pontuação maior."
    else:
        resultado = "Empate!"


    print("Sua mão:", maojogador, "Pontuação:", pontosjogador)
    print("Mão da mesa:", maomesa, "Pontuação:", pontosmesa)
    print(resultado)

# ===== Fim Defs Blackjack =====

# ===== Defs Corrida de Bolihas =====

RED   = "\033[1;31mO\033[m"  
BLUE  = "\033[1;34mO\033[m"
CYAN  = "\033[1;36mO\033[m"
GREEN = "\033[0;32mO\033[m"

def avancarBolas(bolas,corrida):
    
    bola = choice(bolas)

    p1 = f"{bola}----"
    p2 = f"-{bola}---"
    p3 = f"--{bola}--"
    p4 = f"---{bola}-"
    p5 = f"----{bola}"
    p0 = f"-----"

    if bola == RED:
        cor = 0
    elif bola == BLUE:
        cor = 1
    elif bola == CYAN:
        cor = 2
    elif bola == GREEN:
        cor = 3

    partida = "Emjogo"
    posicao = 0

    while True:
        if p1 in corrida[cor][posicao]:
            corrida[cor][posicao] = p2
            break
        elif p2 in corrida[cor][posicao]:
            corrida[cor][posicao] = p3
            break
        elif p3 in corrida[cor][posicao]:
            corrida[cor][posicao] = p4
            break
        elif p4 in corrida[cor][posicao]:
            corrida[cor][posicao] = p5
            break
        elif p5 in corrida[cor][posicao]:
            corrida[cor][posicao] = p0
            posicao += 1
            if corrida[cor][posicao] != "#":
                corrida[cor][posicao] = p1
            else:
                corrida[cor][posicao] = f"{bola}"
                partida = f"--= Vitoria da bolinha {bola} =--"
            break
        else:
            posicao += 1
    return corrida,partida

# ===== Fim Defs Corrida de Bolihas =====