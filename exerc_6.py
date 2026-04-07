numero1 = (int(input('Digite um numero das horas: ')))
numero2 = (int(input('Digite um numero dos minutos: ')))

if numero1 > 23 or numero2 > 59:
    print('Hora invalida ou minutos invalidos')
else:
    print(f'as horas são {numero1}:{numero2}')
