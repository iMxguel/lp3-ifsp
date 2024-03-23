def verificar_palindromo(texto):
    texto_processado = texto.lower().replace(" ", "")
    
    if texto_processado == texto_processado[::-1]:
        return True
    else:
        return False

texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if verificar_palindromo(texto):
    print(f"A palavra ou frase '{texto}' é um palíndromo.")
else:
    print(f"A palavra ou frase '{texto}' não é um palíndromo.")
