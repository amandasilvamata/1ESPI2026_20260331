# estrutrura de decisão
# if, then(:), els:
# igualdades (==) e desigualdades(>, <, >=, <=, !=)
# operadores  logicos - juntam duas ou comparações no mesmo if
# and (malvado), or (bonzinho), not (do contra)
# elif
# nada mais é que a junção do else+if
titulo = 'Dia da semana'
print(f'{titulo:^30}')
numero = int(input('Escolha um numero de 1 até 7: '))

if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-feira')
elif numero == 3:
    print('Teça-feira')
elif numero == 4:
    print('Quarta-feira')
elif numero == 5:
    print('Quinta-feira')
elif numero == 6:
    print('Sexta-feira')
elif numero == 7:
    print('Sábado')
else:
    print('Número inválido')