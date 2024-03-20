def calcular_volume(comprimento, altura, largura):
    volume = (comprimento * altura * largura) / 1000
    return volume

def calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia

def calcular_quantidade_filtragem(volume):
    filtragem_minima = 2 * volume
    filtragem_maxima = 3 * volume
    return filtragem_minima, filtragem_maxima

def main():
    comprimento = float(input("Digite o comprimento do aquário (em cm): "))
    altura = float(input("Digite a altura do aquário (em cm): "))
    largura = float(input("Digite a largura do aquário (em cm): "))
    temperatura_desejada = float(input("Digite a temperatura desejada dentro do aquário (em °C): "))
    temperatura_ambiente = float(input("Digite a temperatura ambiente (em °C): "))

    volume = calcular_volume(comprimento, altura, largura)

    potencia = calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)

    filtragem_minima, filtragem_maxima = calcular_quantidade_filtragem(volume)

    print("Volume do aquário:", volume, "litros")
    print("Potência do termostato necessária:", potencia, "Watts")
    print("Quantidade mínima de filtragem por hora:", filtragem_minima, "litros")
    print("Quantidade máxima de filtragem por hora:", filtragem_maxima, "litros")

if __name__ == "__main__":
    main()
