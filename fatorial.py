n = int (input('Digite o valor de n:'))

fat = 1
i = 2
while i <= n:
	if n == 0:
		print (1)
	if n > 0:
		fat = fat*i
		i = i + 1
print(fat)
	