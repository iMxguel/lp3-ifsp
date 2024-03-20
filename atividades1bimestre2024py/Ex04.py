import re

def verificar_codigo(codigo):
    padrao = r'^BR\d{4}X$'

    if re.match(padrao, codigo):
        numero = int(codigo[2:6])  
        if 1 <= numero <= 9999:
            return True
    return False

codigos = ['BR0001X', 'BR1236X', 'BR9999X', 'br0001X', 'BR126X', 'BR99999X', 'BR9999Y']

for codigo in codigos:
    if verificar_codigo(codigo):
        print(codigo, "é válido")
    else:
        print(codigo, "é inválido")
