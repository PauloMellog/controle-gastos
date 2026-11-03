## Calculadora para controle de gastos 

## Registrar gastos (descrição, valor, categoria)

registro = [
    {"valor": 70, "contexto": "Farmácia", "categoria": "Saúde"},
    {"valor": 56.50, "contexto": "Mercado", "categoria": "Alimentação"},
    {"valor": 115.20, "contexto": "Shopping", "categoria": "Lazer"}
]
print("=== Gastos ===")
for gasto in registro:
    print(f"R$ {gasto['valor']:.2f}")
