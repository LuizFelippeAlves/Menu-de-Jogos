from random import choice
from time import sleep
import os
from DefsJogos import ListadePalavras


def StartJogoDaForca():
    
    dica, Palavras = ListadePalavras()

    PalavrasEscolhida = choice(Palavras)

    LetrasAcertadas = []
    LetrasErradas = []
    Tentativas = 8


    while True:
        os.system("cls")

        print("===== Jogo Da Froca =====")
        print(f"{f'Dica: {dica}': ^25}")
        print("-"*25)
        PalavraEscondida = "".join([letra if letra in LetrasAcertadas else " _" for letra in PalavrasEscolhida])
        print(f"{PalavraEscondida: ^25}")
        print("="*25)
        print("Letra Erradas: ",LetrasErradas)
        print("="*25)
        print(f"Tentativas: {Tentativas}")
        print("="*25)
        
        if "_" not in PalavraEscondida:
            print("\nVocê ganhou!")
            while True:
                voltar = input("\nDeseja Jogar outra vez? [S/N] ").upper().strip()[0]
                if voltar in "SN":
                    break
                print("Erro! Responda Apenas Com S ou N.")
            if voltar == "N":
                os.system("cls")
                break
            else:
                dica, Palavras = ListadePalavras()
                PalavrasEscolhida = choice(Palavras)
                LetrasAcertadas = []
                LetrasErradas = []
                Tentativas = 8

        elif Tentativas == 0:
            print("\nVocê Perdeu! A Palavra era", PalavrasEscolhida)
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
                dica, Palavras = ListadePalavras()
                PalavrasEscolhida = choice(Palavras)
                LetrasAcertadas = []
                LetrasErradas = []
                Tentativas = 8

        else:   
            Letra = input("Digite uma Letra: ").strip()
            
            if len(Letra) == 1:
                if Letra in LetrasAcertadas or Letra in LetrasErradas:
                    print("\nVocê já escolheu essa letra!")
                elif Letra in PalavrasEscolhida:
                    LetrasAcertadas.append(Letra)
                    print(f"\nVoce acertou a letra {Letra}")
                else:
                    LetrasErradas.append(Letra)
                    Tentativas -= 1
                    print("\nVocê errou! -1 Tentativa.")
            else:
                print("\nERRO! Digite apenas uma Letra")

        sleep(2)
