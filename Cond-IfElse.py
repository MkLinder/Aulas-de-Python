n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1+n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')

# Podemos fazer também condições simplificadas:
# print('Parabpens!' if m >=6 else 'Estude mais!')