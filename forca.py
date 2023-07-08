import random
from unidecode import unidecode
from os import system, name


def lista_palavras(word):
    with open(word, 'r', encoding='utf-8') as arquivo:
        word = arquivo.read().splitlines()
    return word


def limparTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def inGame():
    limparTela()

    vidas = 3
    letra_errada = []

    print("Bem vindo ao jogo da forca!!")
    print("Qual a palavra abaixo: \n")

    listaPalavras = 'palavras.txt'
    palavras = unidecode(random.choice(lista_palavras(listaPalavras)).lower())
    print(palavras)

    palavra_oculta = []
    for letra in palavras:
        palavra_oculta.append("_")

    while vidas > 0:
        print(" ".join(palavra_oculta))
        print(f"Você tem: {vidas} vidas")
        print("Letras erradas: ", " ".join(letra_errada))

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavras:
            i = 0
            for letra in palavras:
                if tentativa == letra:
                    palavra_oculta[i] = letra
                i += 1
        else:
            vidas -= 1
            letra_errada.append(tentativa)

        if "_" not in palavra_oculta:
            print(
                f"\nPARABÉNS, Você Venceu!!!!! - A palavra correta é: {palavras} \n")
            break
    if "_" in palavra_oculta:
        print(
            f"\nQUE PENA :((( Você perdeu! - A palavra correta é: {palavras} \n")


# jogo = jogoForca()
if __name__ == "__main__":
    parada = 0
    while parada == 0:
        inGame()
        parada = int(
            input("\nDeseja jogar novamente ou sair? 0 - Jogar Novamente // 1 - Sair \n"))
        if parada == 0:
            limparTela()
        else:
            limparTela()
            print("\nObrigado pela participação!!!\n")
