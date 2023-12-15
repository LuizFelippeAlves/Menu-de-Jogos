from random import randint
import os

def StartJogoDaAdivinhacao():
    num = randint(0,100)
    Tentativas = 0

    os.system("cls")

    print("====="*10)
    print("Bem vindo ao jogo da adivinhacao!\nTente adivinhar o numero que estou pensando.")
    print("====="*10)

    while True:

        Palpite = int(input("De um Palpite de um numero de 0 a 100 : "))

        if Palpite > num:
            print(f"\nERROU!\nO numero que estou pensando é Menor que {Palpite}")
            print("-----"*10)
            Tentativas+=1
        elif Palpite < num:
            print(f"\nERROU!\nO numero que estou pensando é Maior que {Palpite}")
            print("-----"*10)
            Tentativas+=1
        elif Palpite == num:
            print(f"\nParabens! Voce acertou, o numero que eu estava pensando éra {num}")
            print(f"\nVoce teve {Tentativas} tentativas ate acertar")
            print("-----"*10)
            voltar = ""
            while True:
                voltar = input("\nDeseja Jogar outra vez? [S/N] ").upper().strip()[0]
                if voltar in "SN":
                    break
                print("Erro! Responda Apenas Com S ou N.")
            if voltar == "N":
                os.system("cls")
                break
            else:
                Tentativas = 0
                num = randint(0,100)
                os.system("cls")
                print("====="*10)
                print("Ok! Vamos mais uma vez")
                print("====="*10)


