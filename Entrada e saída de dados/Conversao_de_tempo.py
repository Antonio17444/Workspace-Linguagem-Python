tempo_total = int(input("Digite o tempo em segundos: "))

horas = tempo_total // 3600
resto = tempo_total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
