def contador_vogais_consoantes(frase):
    vogais = 0
    consoantes = 0
    vogais_lista = ['a', 'e', 'i', 'o', 'u']

    for letra in frase:
        if letra.lower() in vogais_lista:
            vogais += 1
        elif letra.isalpha():
            consoantes += 1
    
    return vogais, consoantes

frase = input("Digite uma frase: ")

num_vogais, num_consoantes = contador_vogais_consoantes(frase)

print(f"Na frase '{frase}' nós temos {num_vogais} vogais e {num_consoantes} consoantes.")
