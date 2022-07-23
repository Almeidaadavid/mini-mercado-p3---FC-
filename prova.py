import numpy as np
# Biblioteca importada
produtos = ["Milka com oreo", "Nutella", "Laka", "Doce de Leite", "Biscoito Passa-tempo", "Dentaduras Fini",
            "Bis Chocolate Branco", "Amendoim japones", "Sonho de Valsa", "Ouro branco",
            "Baton", "Kinder Ovo", "Tortuguita", "Fandangos", "Pringles", "Ruffles"
            ]

precos = [13.50, 9.00, 5.00, 6.00, 2.30, 4.99, 3.99, 2.00, 1.00, 1.00,
          0.75, 7.40, 1.20, 6.60, 13.00, 7.00]

estoque = [9, 10, 13, 4, 23, 6, 15, 8, 40, 34, 20, 12, 21, 5, 3, 7]

# 1 OK - O programa deve permitir que o usuário faça uma compra com base nos produtos disponíveis na lista produtos e suas respectivas quantidades na lista estoque.
# 2 OK - O programa  deve analisar o produto selecionado registrar a quantidade de itens que o cliente solicitou e ATUALIZAR o valor do estoque para compras futuras.
# 3 OK - O programa deve permitir que o usuário adicione itens até que o mesmo informe , através de um critério de parada de sua escolha, que não deseja mais adicionar itens.
# 4 OK - Após finalizada a coleta dos itens, o programa deve imprimir produto – quantidade – preço unidade e preço total para cada item e pedir que o usuário confirme o pedido.
# 5 OK - Após confirmado o pedido, o programa deve exibir o valor total e perguntar se o pagamento será em dinheiro ou cartão. Caso seja dinheiro, deve aplicar um desconto de 10%. (Seria somar todos os elementos do array de preco_itens e aplicar *0.10)
# 6 OK -  Caso seja em dinheiro, o programa deve receber o valor pago e retornar o troco, informando o valor e a quantidade de notas de 1, 5, 10, 20, 50 ou 100 o caixa deve passar, caso necessário.


# Declaração de variáveis:

itens_pedidos = []
preco_itens = []
qtd_itens = []
valor_compra = []

def inicio():
    #Converter Elementos do Array em minúsculo
    for p in range(len(produtos)):
        produtos[p] = produtos[p].lower()
    produto = input("Digite o produto desejado: ").lower()
    quantidade = int(input("Digite a quantidade desejada: "))
    #Inicializa a função addItem
    addItem(produto,quantidade)

def addItem(produto, quantidade):
    continuar = "s"
    while continuar != "n":
        item_existente = produtos.count(produto)
        if item_existente != 0:
            index = produtos.index(produto)
            preco = precos[index]
            qtd_estoque = estoque[index]
            if qtd_estoque >= quantidade and quantidade > 0:
                itens_pedidos.append(produto)
                qtd_itens.append(quantidade)
                preco_itens.append(preco)
                estoque[index] -= quantidade
            else:
                print("Quantidade não disponível no estoque.")
                print("A quantidade disponível é:",estoque[index])
                continuar = input("Deseja adicionar outro item? s - sim / n - não: ").lower()
                if continuar == "s":
                    inicio()
                    if quantidade > qtd_estoque or quantidade < 0:
                        print("Valor incorreto, reiniciando o sitema de compra. ") # Prever um tratamento para que ao cair nesse local, não retornar outro trecho de código
                        inicio()
                    else:
                        itens_pedidos.append(produto)
                        qtd_itens.append(quantidade)
                        preco_itens.append(preco)
                        estoque[index] = estoque[index] - quantidade
                        valor_compra = (np.multiply(preco_itens, qtd_itens))
                else:
                    print("Encerrando, obrigado.")
                    break
                
            print(itens_pedidos)  # Ta retornando os itens que insiro
            print(qtd_itens)  # Quantidade
            print(preco_itens)  # Valor de cada item.
            print("Quantidade restante no estoque:", estoque[index])
            
            continuar = input("Deseja adicionar outro item? s - sim/ n - não: ").lower()
            print("")
            if continuar == "n":
                carrinho()
            else:
                produto = input("Digite o produto desejado: ").lower()
                quantidade = int(input("Digite a quantidade desejada: "))
        else:
            print("Item não existente no estoque, reiniciando.")
            continuar = input("Deseja reiniciar ? s - sim / n - não: ").lower()
            if continuar == "s":
                inicio()
            else:
                print("Erro")
                exit()
    else:
        print("Saindo") 
        

def carrinho():
    
    for i in range(len(itens_pedidos)):
        print("Você possui no seu carrinho {1} iten(s) {0} que custa(m) R${2} cada ".format(itens_pedidos[i],qtd_itens[i],preco_itens[i]))
        
    confirmar_compra = input("Deseja confirmar a sua compra? s - sim / n - não: ").lower()
    print("")
    
    if confirmar_compra == "s":
        caixa()
    else:
        inicio()
        

def caixa():
    for i in range(len(itens_pedidos)):
        a = itens_pedidos[i]
        valor_compra.append(np.multiply(preco_itens[i], qtd_itens[i]))
        print("O valor total do item {0} é R$".format(a),valor_compra[i])
    print("")
    
    # retorna a soma de todos os elementos no caixa.
    global valor_total
    valor_total = sum(valor_compra)
    print("O valor total da sua compra é R$", valor_total)
    print("")
    metodo_pagamento()
    
    
def metodo_pagamento():
    metodo_pagamento = input("Qual é o método de pagamento? a - A vista / cc - Cartão de crédito: ")
    
    if metodo_pagamento == "a":
        valor_desconto = valor_total*0.10
        valor_a_vista = valor_total - valor_desconto
        print("Valor com desconto R$",round(valor_a_vista,2))
        print("")
        valor_pagamento = float(input("Digite o valor que irá pagar: R$"))
        print("")
        if valor_pagamento >= valor_a_vista:
            valor_troco = valor_pagamento - valor_a_vista
            print("O valor do seu troco é R$",round(valor_troco,2))
            troco(valor_troco)
            print("Obrigado, volte sempre!!!!")
            exit()
        else:
            print("Valor menor do que o valor total.")
            metodo_pagamento()
            
    else:
        print("Valor sem desconto: R$",round(valor_total,2))
        print("Obrigado, volte sempre!!!!")
        exit()
    

def troco(valor_troco):
    cedulas_troco = valor_troco
    #100
    cedulas_cem = cedulas_troco // 100
    cedulas_troco -= cedulas_cem * 100
    #50
    cedulas_cinquenta = cedulas_troco // 50
    cedulas_troco -= cedulas_cinquenta * 50
    #20
    cedulas_vinte = cedulas_troco // 20
    cedulas_troco -= cedulas_vinte * 20
    #10
    cedulas_dez = cedulas_troco // 10
    cedulas_troco -= cedulas_dez * 10
    #5
    cedulas_cinco = cedulas_troco // 5
    cedulas_troco -= cedulas_cinco * 5
    #2
    cedulas_dois = cedulas_troco // 2
    cedulas_troco -= cedulas_dois * 2
    #1
    cedulas_um = cedulas_troco // 1
    cedulas_troco -= cedulas_um * 1
    #0.50
    moeda_cinquenta = cedulas_troco // 0.5
    cedulas_troco -= moeda_cinquenta * 0.5
    #0.25
    moeda_vinte_e_cinco = cedulas_troco // 0.25
    cedulas_troco -= moeda_vinte_e_cinco * 0.25
    #0.10
    moeda_dez = cedulas_troco // 0.10
    cedulas_troco -= moeda_dez * 0.10
    #0.05
    moeda_cinco = cedulas_troco // 0.05
    cedulas_troco -= moeda_cinco * 0.05
    #0.01
    moeda_um = cedulas_troco // 0.01
    cedulas_troco -= moeda_um * 0.01
    
    if cedulas_cem > 0:
        print("{} nota(s) de cem".format(cedulas_cem))
    if cedulas_cinquenta > 0:
        print("{} nota(s) de cinquenta".format(cedulas_cinquenta))
    if cedulas_vinte > 0:
        print("{} nota(s) de vinte".format(cedulas_vinte))
    if cedulas_dez > 0:
        print("{} nota(s) de dez".format(cedulas_dez))
    if cedulas_cinco >0:
        print("{} nota(s) de cinco".format(cedulas_cinco))
    if cedulas_dois >0:
        print("{} nota(s) de dois".format(cedulas_dois))
    if cedulas_um > 0:
        print("{} nota(s) de um".format(cedulas_um))
    if moeda_cinquenta > 0:
        print("{} moeda(s) de cinquenta".format(moeda_cinquenta))
    if moeda_vinte_e_cinco > 0:
        print("{} moeda(s) de vinte e cinco".format(moeda_vinte_e_cinco))
    if moeda_dez > 0:
        print("{} moeda(s) de dez".format(moeda_dez))
    if moeda_cinco > 0:
        print("{} moeda(s) de cinco".format(moeda_cinco))
    if moeda_um > 0:
        print("{} moeda(s) de um".format(moeda_um))

inicio()