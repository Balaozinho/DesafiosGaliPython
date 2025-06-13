pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

pedidos_entregues = []
pedido_valores = []
soma_cancelado = 0

for n in pedidos:
    if n[3] == 'Entregue':
        print(f"Pedido: {n[0]} {n[3]}")
        pedido_valores.append(n[2])
        pedidos_entregues.append(n[0])

for n in pedidos:
    if n[1] == "Vestuário" and n[3] == "Cancelado":
        soma_cancelado += 1

print(f'Cancelados da categoria "Vestuário": {soma_cancelado}')
print(f"Valor Total: {sum(pedido_valores)}")
print(f'Últimos 3 pedidos: {pedidos_entregues[-3:]}')

escolha_categoria = input("Digite a categoria: ")
for n in pedidos:
    if n[1] == escolha_categoria:
        print(f'{n[0]}')
 

