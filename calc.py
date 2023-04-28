num = int(input('Digite um número inteiro: '))
bas = int(input('''
Escolha uma das bases para conversão:
[ 1 ] Converter para binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal
Sua opção: '''))
if bas == 1:
    print(f'{num} para binário é igual a {bin(num)[2:]}')
elif bas == 2:
    print(f'{num} para octal é igual a {oct(num)[2:]}')
elif bas == 3:
    print(f'{num} para hexadecimal é igual a {hex(num)[2:]}')
else:
    print(f'{bas} não equivale a nehuma base!')
