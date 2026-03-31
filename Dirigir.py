titulo = 'Maioridade'
print(f'{titulo: ^30}')
idade = int(input('Que idade você tem? '))
cnh = input('Você tem CNH?')

# Operadores RELACIONANIS
# São os que vão combinar as comparações
# AND é o operador malvado, só deixa prosseguir se tudo for sim
# OR é o operador bonzinho, qualquer um que for sim ele deixa prosseguir
# NOT é o operador do contra, ele faz tudo ao contrário


if idade >= 18 and cnh == 'sim': #sim, then, 1
    print('Você pode dirigir')
else: #não, else, 0
    print('Você não pode dirigir')
print('TRÂNSITO DE SÃO PAULO AGRADECE')