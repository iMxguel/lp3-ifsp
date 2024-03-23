import random

def escolher_palavra():
    palavras = ['python', 'luk', 'latorre', 'ugo', 'claudete', 'ide', 'java']
    return random.choice(palavras)

def mostrar_forca(palavra_secreta, letras_corretas):
    for letra in palavra_secreta:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    tentativas_restantes = 6
    letras_corretas = []
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")
    mostrar_forca(palavra_secreta, letras_corretas)

    while True:
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira apenas uma letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            letras_erradas.append(letra)
            tentativas_restantes -= 1
            print("Letra incorreta! Você tem", tentativas_restantes, "tentativas restantes.")

        mostrar_forca(palavra_secreta, letras_corretas)

        if set(letras_corretas) == set(palavra_secreta):
            print("Parabéns! Você acertou a palavra secreta:", palavra_secreta)
            break

        if tentativas_restantes == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

jogar_forca()
