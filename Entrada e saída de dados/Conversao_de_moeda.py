valor_reais = float(input("Digite o valor em reais (R$): "))
taxa_cambio = float(input("Digite a taxa de câmbio (1 dólar equivale a quantos reais?): "))

valor_dolares = valor_reais / taxa_cambio

print(f"O valor em dólares é: ${valor_dolares:.2f}")
