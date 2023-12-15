import os
from time import sleep
from DefsJogos import EscolherBloco, CondicaoVitoria

def StartJogoDaVelha():
    Blocos = [["","",""],
            ["","",""],
            ["","",""]]

    JogadorDaVez = "X"

    while True:

        os.system('cls')

        print("===== Jogo Da Velha =====")
        for l in Blocos:
            print(" "*5,end=" | ")
            for c in l:
                print(c,end=" | ")
            print()
        print("====="*5)
        

        print(f"É a vez do {JogadorDaVez} jogar")
        print()
        
        # Relizar jogada e retornar o rezultado dela
        try:
            Jogada = EscolherBloco(Blocos,int(input("Digite o numero da linha:"))-1,int(input("Digite o numero da Coluna:"))-1,JogadorDaVez)
        except:
            print("OPS!\nLembre-se de usar apenas valores de 1 a 3 para as linhas e colunas")
            sleep(2)
            Jogada = "Invalida"

        # Checar o resultado de uma jogada para prosegir para o proximo jogador
        if Jogada != "Invalida":
            if JogadorDaVez == "X":
                JogadorDaVez = "O"
            else:
                JogadorDaVez = "X"
        os.system("cls")

    # Checar andamento do jogo , e verificação para re-jogar ou voltar ao menu
        ChecarVitoria=CondicaoVitoria(Blocos)
        if ChecarVitoria != "Jogo em Andamento":
            print(ChecarVitoria)
            print()
            voltar = ""
            while True:
                voltar = input("Deseja Jogar outra vez? [S/N] ").upper().strip()[0]
                if voltar in "SN":
                    break
                print("Erro! Responda Apenas Com S ou N.")
            if voltar == "N":
                os.system("cls")
                break
            else:
                Blocos = [["","",""],
                        ["","",""],
                        ["","",""]]
                JogadorDaVez = "X"

