casa = float(input('Qual o valor da propriedade? R$'))
sal = float(input('Qual o seu salário mensal atual? R$'))
anos = int(input('Em quantos anos deseja pagar?'))
parc = casa / (anos * 12)
maxparc = sal * 30 / 100
print('Uma propriedade de R${:.2f}, em {} anos, a prestação será de {}x R${:.2f}'.format(casa, anos,(anos * 12), parc))
if parc <= maxparc:
    print('Emprésimo aprovado!')
else:
    print('Empréstimo negado!')