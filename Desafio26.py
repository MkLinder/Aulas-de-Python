frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes.'.format(frase.upper().count('A')))
print('A primiera letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))
