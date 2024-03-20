import re

def verificar_codigo(codigo):
    padrao = r'^BR\d{4}X$'

    if re.match(padrao, codigo):
        numero = int(codigo[2:6])  
        if 1 <= numero <= 9999:
            return True
    return False

def main():

    codigo = input("Digite o identificador (no formato BRXXXXX): ")

    if verificar_codigo(codigo):
        print("O identificador", codigo, "é válido.")
    else:
        print("O identificador", codigo, "é inválido.")

if __name__ == "__main__":
    main()
