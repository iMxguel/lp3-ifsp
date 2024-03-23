def contar_palavras(frase):
    palavras = frase.split()
    contagem = {}

    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem

texto = input("Digite uma frase para contar as palavras: ")

resultado = contar_palavras(texto)

print("Contagem de palavras:")
for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")
