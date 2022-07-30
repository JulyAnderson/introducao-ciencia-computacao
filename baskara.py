from math import sqrt

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de b: '))

delta = b*b - 4*a*c

if delta < 0 :
	print ('esta equação não possui raízes reais')

elif delta == 0:
	raiz = (-b + sqrt(delta))/2*a
	print ('a raiz dupla desta equação é {}'.format(raiz))
else:
	raiz1 = (-b + sqrt(delta))/2*a
	raiz2 = (-b - sqrt(delta))/2*a
	if raiz1 < raiz2:
		print ('as raízes da equação são {} e {}'.format(raiz1, raiz2))
	else:
		print ('as raízes da equação são {} e {}'.format(raiz2, raiz1))