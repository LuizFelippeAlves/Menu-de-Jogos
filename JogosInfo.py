from time import sleep
import os

def JogodaVelha():
    os.system("cls")

    print("Processando....")

    sleep(2)

    print("""Jogo da Velha

Como jogar:

Escolha quem será o primeiro a jogar.
    1 - O jogador da vez deve selecionar a linha e a coluna onde deseja jogar.
    2 - Os jogadores se alternam até que um jogador consiga colocar três símbolos iguais em uma linha, coluna ou diagonal.
    3 - Se todas as posições da grade forem preenchidas e nenhum jogador conseguir fazer uma linha, coluna ou diagonal com três símbolos iguais, o jogo termina em empate.

Dicas:
    0 - Observe as jogadas do oponente e tente bloquear suas jogadas.
    0 - Procure suas próprias oportunidades de fazer uma linha, coluna ou diagonal com seus símbolos.

Divirta-se jogando o Jogo da Velha!
""")

def JogodaForca():
    os.system("cls")

    print("Processando....")

    sleep(2)

    print("""Jogo da Forca

Como jogar:

    1 - O jogo seleciona uma palavra aleatória para o jogador adivinhar.
    2 - O jogador deve adivinhar as letras da palavra, uma por vez.
    3 - Se o jogador acertar a letra, ela é revelada na palavra. Se não, perde uma das tentativas.
    4 - O jogador continua a adivinhar letras até que a palavra seja completada ou as tentativas acabem.

Dicas:
    0 - Tente adivinhar as letras mais comuns primeiro, como as vogais.
    0 - Use seu conhecimento de palavras e do contexto para tentar adivinhar a palavra completa.
    0 - Tome cuidado para não errar muitas letras e acabar com as tentativas.

Divirta-se jogando o Jogo da Forca!
""")

def JogodaAdivinhacao():
    os.system("cls")

    print("Processando....")

    sleep(2)

    print("""Jogo de Adivinhar um Número

Como jogar:

    1 - O jogo escolhe um número aleatório entre 1 e 100.
    2 - O jogador deve tentar adivinhar qual é o número selecionado, digitando um palpite.
    3 - Se o palpite do jogador for maior que o número selecionado, o jogo informa que o número é menor. Se for menor, o jogo informa que o número é maior.
    4 - O jogador continua a adivinhar até acertar o número selecionado.

Dicas:
    0 - Tente fazer uma estimativa do número selecionado com base nas dicas fornecidas pelo jogo.
    0 - Comece com um palpite no meio do intervalo (50), para poder reduzir pela metade o número de possibilidades a cada palpite.
    0 - Use o processo de eliminação para eliminar possibilidades de números.

Divirta-se jogando o Jogo de Adivinhar um Número!
""")

def JogoPPT():
    os.system("cls")

    print("Processando....")

    sleep(2)

    print("""Jogo Pedra, Papel e Tesoura

Como jogar:

    1 - Os jogadores escolhem uma das opções: pedra, papel ou tesoura.
    2 - A escolha de cada jogador é comparada, e o jogador com a opção vencedora ganha a rodada.
    3 - Pedra ganha de tesoura, tesoura ganha de papel e papel ganha de pedra.
    4 - O jogo continua até que um jogador alcance um número de vitórias pré-determinado.

Dicas:
    0 - Tente adivinhar a opção do oponente e escolha a opção que a vence.
    0 - Use táticas psicológicas para tentar fazer o oponente escolher uma opção que você vence.
    0 - Lembre-se que o jogo é baseado na sorte, então não se frustre caso perca algumas rodadas.

Divirta-se jogando o Jogo Pedra, Papel e Tesoura!
""")

def BlackJack():
    os.system("cls")

    print("Processando....")

    sleep(2)

    print("""Jogo de Cartas Blackjack

Como jogar:

    1 - O objetivo do jogo é ter uma mão que some 21 pontos ou o mais próximo possível sem passar desse valor.
    2 - O jogo começa com o dealer distribuindo duas cartas para cada jogador, incluindo ele mesmo. Uma das cartas do dealer fica virada para baixo.
    3 - Os jogadores podem escolher "hit" para receber outra carta ou "stand" para manter a mão atual.
    4 - Se o jogador passar de 21 pontos, ele perde automaticamente. Se o jogador ficar abaixo de 21, o dealer revela sua carta virada para baixo e continua a jogar até que sua mão some 17 pontos ou mais.
    5 - Se a mão do jogador for maior que a do dealer e não ultrapassar 21, o jogador ganha. Se a mão do jogador for menor que a do dealer ou ultrapassar 21, o jogador perde.

Dicas:
    0 - Lembre-se que o Ás pode valer 1 ou 11 pontos, dependendo da sua mão.
    0 - Considere a carta do dealer virada para baixo ao tomar suas decisões.
    0 - Aprenda a estratégia básica do blackjack para aumentar suas chances de ganhar.

Divirta-se jogando o Jogo de Cartas Blackjack!""")

def CorridadeBolinhas():
    os.system("cls")

    print("Processando....")

    sleep(2)

    print("""Corrida de Bolinhas

Como jogar:

    1 - Cada jogador escolhe uma das 4 bolinhas coloridas.
    2 - Após isso, a corrida irá se iniciar. Torça para que sua bolinha chegue primeiro e divirta-se!
    3 - Os corredores são Vermelho, Azul, Cyano e Verde.
""")
    
def comfirmar():
    input("Para prosseguir, aperte Enter...")
