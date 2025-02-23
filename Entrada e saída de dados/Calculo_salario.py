salario_base = float(input("Digite o salário base do funcionário: "))
percentual_aumento = float(input("Digite o percentual de aumento (%): "))

novo_salario = salario_base + (salario_base * percentual_aumento / 100)

print(f"O novo salário do funcionário será: R$ {novo_salario:.2f}")
