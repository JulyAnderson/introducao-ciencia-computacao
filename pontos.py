from math import sqrt

x1 = int(input('Digite uma coordenada: '))
y1 = int(input('Digite uma coordenada: '))
x2 = int(input('Digite uma coordenada: '))
y2 = int(input('Digite uma coordenada: '))

d = sqrt( (x1 - x2)*(x1 - x2) + (y1 -y2)*(y1 -y2))
			
if d >= 10:
	print ('longe')
else:
	print ('perto')