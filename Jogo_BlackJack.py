from DefsJogos import CriarBaralho,ComprarCarta,MostrarMao,VerificarJogo,CalcularPontos,sleep,ResultadoJogo
import os

def StartBlackJack():
    naips = ["Paus","Ouros","Espadas","Copas"]
    baralho = CriarBaralho(naips)
    
    maoJogador = []
    maoMesa = []
    cartaEmJogo = list(set(maoJogador + maoMesa))

    maoJogador.append(ComprarCarta(baralho,cartaEmJogo))
    maoJogador.append(ComprarCarta(baralho,cartaEmJogo))
    maoMesa.append(ComprarCarta(baralho,cartaEmJogo))
    cartaOculta = ComprarCarta(baralho,cartaEmJogo)
    maoMesa.append("Carta Virada")

    while True:
        os.system("cls")

        estadoJogo = VerificarJogo(CalcularPontos(maoJogador))

        MostrarMao(maoMesa,maoJogador)
        sleep(2)

        if "Carta Virada" in maoMesa:
            decisao = "inicio"
        else:
            decisao = "finalizar"

        if estadoJogo == "Em Jogo" and decisao != "finalizar":
            while True:
                decisao = input("Deseja Comprar uma carta ou Finalizar jogada?\nEscolha: ").lower().strip()
                if decisao in ["comprar","finalizar"]:
                    break
                print("Erro! Responda Apenas Com Comprar ou Finalizar")
                sleep(2)
            if decisao == "comprar":
                maoJogador.append(ComprarCarta(baralho,cartaEmJogo))
            elif decisao == "finalizar":
                print("finalizando Jogada...")
                print("Vez da mesa jogar")
                sleep(2)

        acaomesa = "espera"
        if estadoJogo != "Em Jogo" or decisao == "finalizar":
            if "Carta Virada" in maoMesa:
                maoMesa.remove("Carta Virada")
                maoMesa.append(cartaOculta)
                print("Virando a carta Oculta da mesa!")
                sleep(2)
            else:
                if CalcularPontos(maoMesa) < 17:
                    maoMesa.append(ComprarCarta(baralho,cartaEmJogo))
                    acaomesa = "A Mesa comprou uma carta"
                    continue
                elif CalcularPontos(maoMesa) == 21:
                    acaomesa = "A Mesa fez 21!"
                elif CalcularPontos(maoMesa) > 21:
                    acaomesa = "A Mesa Estorou o valor limite"
                else:
                    acaomesa = "A Mesa encerrou suas acoes"
                print(acaomesa)
                sleep(2)

        if acaomesa != "espera" and acaomesa != "A Mesa comprou uma carta":
            ptmesa = CalcularPontos(maoMesa)        
            ptjogador = CalcularPontos(maoJogador)
            ResultadoJogo(ptmesa,ptjogador,maoJogador,maoMesa)
            sleep(3)
            voltar = ""
            while True:
                    voltar = input("\nDeseja Jogar outra vez? [S/N] ").upper().strip()[0]
                    if voltar in "SN":
                        break
                    print("Erro! Responda Apenas Com S ou N.")
            if voltar == "N":
                os.system("cls")
                break
            elif voltar == "S":
                maoJogador = []
                maoMesa = []
                cartaEmJogo = list(set(maoJogador + maoMesa))

                maoJogador.append(ComprarCarta(baralho,cartaEmJogo))
                maoJogador.append(ComprarCarta(baralho,cartaEmJogo))
                maoMesa.append(ComprarCarta(baralho,cartaEmJogo))
                cartaOculta = ComprarCarta(baralho,cartaEmJogo)
                maoMesa.append("Carta Virada")