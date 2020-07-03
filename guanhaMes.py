#Faça um progrma que pergunte quanto você ganha por hora e o numero de horas que ele trabalha por mês. Calcule e mostre o total em mês

salHora = int(input('\n Digite o seu salario por hora: '))
traHora = int(input('\n Quantas horas você trabalha por hora: '))

hora = salHora * traHora

print('\n Salario mensal: {}'.format(hora))