valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra < 10:
    desconto = 0
elif valor_compra < 100:
    desconto = 0.05
elif valor_compra < 500:
    desconto = 0.10
else:
    desconto = 0.15

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print("Valor final com desconto: R$", valor_final)
print("Desconto aplicado: {}%".format(desconto * 100))