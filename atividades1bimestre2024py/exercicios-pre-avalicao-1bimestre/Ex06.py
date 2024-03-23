def converter_nota(pontuacao):
    if pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'

pontuacao = float(input("Digite a pontuação (0 a 100): "))

if 0 <= pontuacao <= 100:
    nota = converter_nota(pontuacao)
    print(f"A nota correspondente à pontuação {pontuacao} é {nota}.")
else:
    print("Pontuação inválida. Por favor, insira uma pontuação entre 0 e 100.")
