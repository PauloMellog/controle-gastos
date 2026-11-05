## Calculadora para controle de gastos 

#################################################
## Registrar gastos (descrição, valor, categoria)
#################################################

registro = [
    {"valor": 70, "contexto": "Farmácia", "categoria": "Saúde"},
    {"valor": 56.50, "contexto": "Mercado", "categoria": "Alimentação"},
    {"valor": 115.20, "contexto": "Shopping", "categoria": "Lazer"}
]
print("=== Gastos ===")
for gasto in registro:
    print(f"{gasto['contexto']}: {gasto['categoria']}, R$ {gasto['valor']:.2f}")

##############################################
## Mostra o gasto total do mês e por categoria
##############################################

print("\n=== Soma total no mês ===")

soma = 0
for gasto in registro:
    soma = soma + gasto["valor"]

print(f"A soma do mês é igual a R${soma:.2f}")

gastos_categoria = {}

for gasto in registro:
    categoria = gasto["categoria"]
    if categoria in gastos_categoria:
        gastos_categoria[categoria] = gastos_categoria[categoria] + gasto["valor"]
    else:
        gastos_categoria[categoria] = gasto["valor"]

print("\n=== Soma por categoria ===")
for categoria, total in gastos_categoria.items():
    print(f"{categoria}: R$ {total:.2f}")
