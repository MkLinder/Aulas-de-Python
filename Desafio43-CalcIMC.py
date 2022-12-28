altura = float(input('Digite a sua altura (m): '))
peso = float(input('Digite seu peso (Kg): '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')
