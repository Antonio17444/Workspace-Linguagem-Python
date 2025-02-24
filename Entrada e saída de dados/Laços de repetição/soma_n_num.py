N = int(input("Digite um número N: "))

soma = 0

for i in range(1, N + 1):
    soma += i

print(f"A soma dos primeiros {N} números é: {soma}")
