tempo = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = tempo // (3600*24)
tempo_restante = tempo % (3600*24)
horas = tempo_restante // 3600
segundos_restante =  tempo_restante % 3600
minutos = segundos_restante //60
segundos_final = segundos_restante % 60

print( dias, 'dias,', horas, 'horas,', minutos,'minutos e', segundos_final,'segundos.')






#print( dias, horas, minutos, segundos)
