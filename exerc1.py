# caixa A abastece pares
# caixa B abastece impar

blocoPar = []
blocoImpar = []

blocoUsuario = int(input('Qual é o bloco que você mora? '))

if blocoUsuario % 2 == 0 and blocoUsuario <= 4:
    blocoPar.append(blocoUsuario)
elif blocoUsuario % 2 != 0 and blocoUsuario <= 4:
    blocoImpar.append(blocoUsuario)
else:
    print('Digite um bloco válido entre 1 e 4!')

if blocoUsuario in blocoPar:
    print('O seu bloco é abastecido pela caixa A')
elif blocoUsuario in blocoImpar:
    print('O seu bloco é abastecido pela caixa B')
