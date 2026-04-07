numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))

if numero1 == numero2 and numero2 == numero3:
    print('É equilátero')
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print('É isósceles')
else:
    print('É escaleno')