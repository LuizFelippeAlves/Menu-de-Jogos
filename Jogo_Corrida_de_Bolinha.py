from time import sleep
from DefsJogos import avancarBolas
import os

def startCorridadeBolinha():
    RED   = "\033[1;31mO\033[m"  
    BLUE  = "\033[1;34mO\033[m"
    CYAN  = "\033[1;36mO\033[m"
    GREEN = "\033[0;32mO\033[m"

    corrida = [
                [f"{RED}----","-----","-----","-----","-----","-----","-----","#"],
                [f"{BLUE}----","-----","-----","-----","-----","-----","-----","#"],
                [f"{CYAN}----","-----","-----","-----","-----","-----","-----","#"],
                [f"{GREEN}----","-----","-----","-----","-----","-----","-----","#"]]
        
    bolas = [RED,BLUE,CYAN,GREEN]

    partida = "iniciar"
    while True:
        os.system("cls")
        
        print(f"{' Corrida das bolinhas ':=^36}")
        for linha in corrida:
            for espaco in linha:
                print(espaco,end="")
            print()
        print("="*36)

        if partida == "iniciar":
            print("Atenção, Todas as bolinhas em suas marcas!")        
            sleep(1)
            print("Em",end="...")
            for l in range(5,0,-1):
                print(f"{l}",end="...")
            print("BANG!!!")
            sleep(1.5)
            partida= "Emjogo"
        
        sleep(0.4)

        if partida != "Emjogo":
            print("\n",f"{f'{partida}':-^36}","\n")
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
                corrida = [
                    [f"{RED}----","-----","-----","-----","-----","-----","-----","#"],
                    [f"{BLUE}----","-----","-----","-----","-----","-----","-----","#"],
                    [f"{CYAN}----","-----","-----","-----","-----","-----","-----","#"],
                    [f"{GREEN}----","-----","-----","-----","-----","-----","-----","#"]]
                partida = "iniciar"

        corrida, partida = avancarBolas(bolas,corrida)
