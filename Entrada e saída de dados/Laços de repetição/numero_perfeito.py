num = int(input("Digite um número para verificar se é perfeito: "))

soma_divisores = sum(i for i in range(1, num) if num % i == 0)

if soma_divisores == num:
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} não é um número perfeito.")
