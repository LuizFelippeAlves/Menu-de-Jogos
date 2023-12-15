import os
from time import sleep
from Jogo_da_velha import StartJogoDaVelha
from Jogo_da_forca import StartJogoDaForca
from Jogo_da_adivinhacao import StartJogoDaAdivinhacao
from Jogo_Pedra_Papel_Tesoura import StartJogoPPT
from Jogo_BlackJack import StartBlackJack
from Jogo_Corrida_de_Bolinha import startCorridadeBolinha

import JogosInfo

listaDejogos = ["Jogo da Velha","Jogo da Forca","Jogo da Adivinhacao","Jogo do Pedra, Papel e Tesoura","BlackJack","Corrida de Bolinhas"]
listaDejogos.append("Sair")

while True:
    os.system("cls")

    print(f"{'Opções':=^40}")
    for jogo in listaDejogos:
        print(f"{listaDejogos.index(jogo)+1} - {jogo}")
    print("="*40)

    opcao = int(input("Escolha uma das Opcões: "))

    if opcao == 1:
        JogosInfo.JogodaVelha()
        JogosInfo.comfirmar()
        StartJogoDaVelha()

    elif opcao == 2:
        JogosInfo.JogodaForca()
        JogosInfo.comfirmar()
        StartJogoDaForca()

    elif opcao == 3:
        JogosInfo.JogodaAdivinhacao()
        JogosInfo.comfirmar()
        StartJogoDaAdivinhacao()
    
    elif opcao == 4:
        JogosInfo.JogoPPT()
        JogosInfo.comfirmar()
        StartJogoPPT()

    elif opcao == 5:
        JogosInfo.BlackJack()
        JogosInfo.comfirmar()
        StartBlackJack()

    elif opcao == 6:
        JogosInfo.CorridadeBolinhas()
        JogosInfo.comfirmar()
        startCorridadeBolinha()

    elif opcao == len(listaDejogos):
        os.system('cls')
        print("Não perca as próximas novidades e volte sempre para mais diversão!")
        break

    else:
        print("Ooops, parece que essa opção não existe. Por favor, escolha uma opção válida.")
        
    print("Voltando para o menu principal de jogos. O que você gostaria de fazer a seguir?")
    sleep(3)