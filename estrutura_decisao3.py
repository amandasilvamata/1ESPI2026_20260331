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


# abordagem match case
match numero:
    case 2:
        print('Segunda-feira')
    case 3:
        print('Teça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case 1 | 7:
        print('Fim de semana')
    case _:
        print('Número inválido')