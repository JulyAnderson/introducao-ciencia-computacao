dezena = int(input('Digite um número inteiro:'))
digito = dezena % 100
digito_final = digito // 10
print('O dígito das dezenas é', digito_final)