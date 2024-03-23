import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    
    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Seu palpite está baixo. Tente novamente!")
        elif palpite > numero_secreto:
            print("Seu palpite está alto. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
            break

jogo_de_adivinhacao()
