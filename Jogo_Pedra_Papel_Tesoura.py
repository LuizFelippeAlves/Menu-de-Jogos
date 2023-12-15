from random import choice
import os
from time import sleep

def StartJogoPPT():
    opcoes=["pedra","papel","tesoura"]
    maquina=choice(opcoes)


    while True:

        os.system("cls")

        maquina=choice(opcoes)

        print("--=Vamos Jogar Pedra, Papel ou Tesoura!=--")
        print("--- ","Pedra"," --- ","Papel"," --- ", "Tesoura"," ---")
        print("---"*14)
        player=input("Escolha entre uma das opcoes: ").lower().strip()
        print("\nProcessando...")
        sleep(3)
        print("Resultado:",end=" ")

        if maquina==player:
            print("ocorreu um empate!")
        elif player=="pedra":
            if maquina=="papel":
                print(f"Você perdeu! {maquina} cobre {player}")
            else:
                print(f"Parabéns! Voce venceu! {player} quebra {maquina}!")
        elif player=="papel":
            if maquina=="tesoura":
                print(f"Você perdeu! {maquina} corta {player}!")
            else:
                print(f"Parabéns! Voce venceu! {player} cobre {maquina}!")
        elif player=="tesoura":
            if maquina=="pedra":
                print(f"Você perdeu! {maquina} esmaga {player}!")
            else:
                print(f"Parabéns! Voce venceu! {player} corta {maquina}!")
        else:
            print("Jogada inválida, verifique se digitou a opção corretamente!")
        voltar = ""
        while True:
            voltar = input("\nDeseja Jogar outra vez? [S/N] ").upper().strip()[0]
            if voltar in "SN":
                break
            print("Erro! Responda Apenas Com S ou N.")
        if voltar == "N":
            os.system("cls")
            break

