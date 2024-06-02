def comprar():
    saldo = 700
    
    # Lista de eletrônicos com seus respectivos preços
    eletronicos = {
        'tablet': 200,
        'computador': 300,
        'celular': 100
    }

    while True:
        print(f"Seu saldo atual é: R${saldo:.2f}")
        print("Eletrônicos disponíveis para compra:")
        
        # Exibir a lista de eletrônicos e seus preços
        for item, preco in eletronicos.items():
            print(f"{item.capitalize()}: R${preco:.2f}")
        
        # Solicitar que o usuário escolha um item para comprar
        item_escolhido = input("Qual item deseja comprar? (digite 'sair' para encerrar): ").lower()

        if item_escolhido == 'sair':
            break

        # Verificar se o item está na lista de eletrônicos
        if item_escolhido in eletronicos:
            valor_a_ser_cobrado = eletronicos[item_escolhido]

            if saldo >= valor_a_ser_cobrado:
                saldo -= valor_a_ser_cobrado # Atualiza o saldo após a compra
                print(f"{item_escolhido.capitalize()} comprado com sucesso!")
                print(f"Saldo restante: R${saldo:.2f}")
            else:
                print("Saldo insuficiente para comprar este item.")
        else:
            print("Item não encontrado. Por favor, escolha um item válido.")

        # Pergunta se o usuário deseja fazer outra compra ou não
        continuar = input("Deseja fazer outra compra? (s/n): ").lower()
        if continuar != 's':
            break

    print("Operação finalizada. Obrigado!")

# Chama a função para executar a compra
comprar()