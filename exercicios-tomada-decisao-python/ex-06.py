# Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" 
# a senha for "admin123", caso contrário imprima uma mensagem de erro.

user = (input('Olá! Como você gostaria que te chamassemos?'))
login = (input(f'Combinado, {user}. Crie seu login: '))
senha = print (input(f'{user}, agora crie uma senha: '))
if senha != 'admin123':
    print (f'Poxa,{user}, essa senha está dando erro!')