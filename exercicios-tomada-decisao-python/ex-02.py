# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "BomDia!","BoaTarde!"ou"BoaNoite!"ou "ValorInválido!", conforme o caso.

valores_permitidos = ['M', 'V', 'N']

turno = input("Em que turno você estuda? Responda com:\nM para matutino\n" +
              "V para vespertino\nN para noturno.\n")

if turno not in valores_permitidos:
    print("Valor inválido!")

elif turno == 'M':
    print("Bom dia!")

elif turno == 'V':
    print("Boa tarde!")

else:
    print("Boa noite!")