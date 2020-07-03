# Faça um programa que peça dois números int e um float. Calcule e mostre
# a. o produto do dobro do primeiro com  metade do segundo
# b. a soma do triplo do primeiro com o terceiro
# c. o terceiro elevado ao cubo

numb1 = int(input('\n Digite um numaro inteiro: '))
numb2 = int(input('\n Digite um numaro inteiro: '))
numb3 = float(input('\n Digite um numaro inteiro: '))

produto = ((numb1*2)*(numb2/2))
soma = ((numb1*3)+numb3)
elevado = pow(numb3,3)

print('\n a. o produto do dobro do primeiro com  metade do segundo {} \n b. a soma do triplo do primeiro com o terceiro {} \n c. o terceiro elevado ao cubo {}'.format(produto,soma,elevado))