def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Excesso de peso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def calcular_diferenca_peso_normal(peso, altura):
    imc_normal = 24.9
    peso_normal = imc_normal * (altura * altura)
    
    diferenca = peso_normal - peso
    return diferenca

def main():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)

    classificacao = classificar_imc(imc)

    diferenca_peso_normal = calcular_diferenca_peso_normal(peso, altura)

    print("Seu IMC é:", imc)
    print("Classificação do IMC:", classificacao)
    print("Você precisa", abs(diferenca_peso_normal), "kg", ("a mais" if diferenca_peso_normal < 0 else "a menos"), "para chegar ao peso normal.")

if __name__ == "__main__":
    main()
