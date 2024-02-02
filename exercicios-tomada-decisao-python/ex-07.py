# Desenvolver um programa que solicite a idade do usuário e 
# identifique se ele é uma criança, um adolescente, adulto ou idoso

idade = int(input('Olá! Informe a sua idade: '))
if idade <= 11:
    print('Você é uma criança. Aproveite essa fase')
elif idade <= 17:
    print('Você está na fase da adolescência. Fica tranquilo, que passa')
elif idade >= 60:
    print('Você é uma pessoa idosa')
else:
    print('Você é adulto. Os boletos já chegaram!')