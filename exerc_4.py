letra = ('Digite uma letra: ').lower()

match letra:
    case 'a'| 'e' | 'i' | 'o' | 'u':
        print('Essa letra é uma vogal')
    case _:
        print('Essa letra é uma consoante')