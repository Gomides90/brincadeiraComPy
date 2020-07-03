# Faça que peça a temperatura em graus Farenheit, e transforme em Celsius C = (5*(F-32)/9)

f = float(input('\n Digite a temperatura em Farenheit'))
c = (5*(f-32)/9)

print('\n A transformação de temperatura de Farenheit para Celsius é: {}'.format(c))