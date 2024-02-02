# Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e 
# classifique-o como equilátero, isósceles ou escaleno. 
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

prim = int(input('Informe a primeira medida do triângulo: '))
segu = int(input('Informe a segunda medida do triângulo: '))
terc = int(input('Informe a terceira medida do triângulo: '))
if prim == segu == terc:
    print ('Este triângulo é equilátero')
elif prim == segu != terc:
    print ('Este triângulo é isósceles')
elif prim != segu == terc:
    print ('Este triângulo é isósceles')
elif prim != segu != terc:
    print ('Este triângulo é escaleno')

