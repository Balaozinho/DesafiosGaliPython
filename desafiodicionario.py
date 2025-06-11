loja_games  = {
    "Minecraft" : {"Preço" : 59.90, "Estoque": 5},
    "Fifa23" : {"Preço" : 199.90, "Estoque": 3},
    "God of war" : {"Preço" : 149.90, "Estoque": 4},
}

#mostre todos os jogos disponiveis 
for jogo,info in loja_games.items():
    print(f'{jogo} - R$ {info['Preço']} - {info['Estoque']} unidades em estoque')

print('-'*60)


#Carrinho de Compras (dicionário)
carrinho = {}

while True:
    escolha_jogo = input("Qual jogo você deseja? (ou 'sair' para fechar): ").strip().capitalize()
    if escolha_jogo.strip().lower() == 'sair':
        break

    if escolha_jogo in loja_games:
        print("TEMOS EM NOSSO CONTROLE!")
        jogo = loja_games[escolha_jogo] #retorna o dicionário que possui como valor as infos do jogo escolhido
        qtdade_solicitada = int(input("Quantos unidades você deseja comprar?"))
        if qtdade_solicitada <= jogo['Estoque']:
            loja_games[escolha_jogo]['Estoque'] -= qtdade_solicitada
            if escolha_jogo in carrinho:
                carrinho[escolha_jogo] += qtdade_solicitada
            else:
                carrinho[escolha_jogo] = qtdade_solicitada
            print(f'Carrinho: {qtdade_solicitada} unidades adicionadas do jogo {escolha_jogo}')
        else:
            print(f"Não temos essa quantidade disponível em estoque, apenas {loja_games[escolha_jogo]['Estoque']} unidades")
    else:
        print("Jogo não encontrado. Tente novamente ou digite 'sair")

#RESUMO DA COMPRA
total = 0
print('RESUMO DA COMPRA'.center(40,'-'))
for jogo, qtd in carrinho.items():
    preco = loja_games[jogo]['Preço']
    total += preco * qtd
    print(f'{jogo}  x{qtd} unidades'.center(40))
print('-'*40)
print(f'Total: R$ {total}'.center(40))