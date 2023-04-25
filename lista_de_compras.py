#Lista de Compras

opcao = ''
lista_compras = []

# Exibe um menu identificado 4 opções para o usuário:
# Inserir = Insere um produto na lista de compras
# Apagar = Apaga um item na lista de compras
# Listar = Mostra a lista de compras
# Sair = Fecha o programa

def exibir_menu():
    while True:
        print("-----------------------------")
        print("|   Selecione uma Opção:    |")
        print("|                           |")
        print("| [I]nserir      [A]pagar   |")
        print("| [L]istar       [S]air     |")
        print("|                           |")
        print("-----------------------------")



        # Input da opção
        opcao = input("Opção: ").lower()

        # Identifica as possíveis opções, se estiver errado o Loop continua até inserir a opção correta. Se estiver
        # certo ele retorna o valor recebido da função exibir_menu()

        possiveis_opcoes = ('i', 'a', 'l', 's')
        if opcao in possiveis_opcoes:
            return(opcao)
        else:
            print("Digite uma opção válida")

mostrar_sua_lista = True

# Confere se a lista está vazia
def lista_vazia():
    if lista_compras == []:
        print("A lista está vazia, adicione itens! \n")
        return True
    else:
        return False

# Confere se a lista está vazia e mostra a lista.
def mostrar_lista():
    if not lista_vazia():
        print("Sua lista: \n")
    
    for indice, item in enumerate(lista_compras):
            print(indice, item.capitalize())


repetir_lista = True

while True:

    opcao = exibir_menu()

    if opcao == 'i':
        while True:

            # Mostra os itens da lista
            if repetir_lista == True:
                mostrar_lista()
            
            # Pede ao usuário para digitar um produto
            produto = input("Digite o produto que deseja inserir: ")
            lista_compras.append(produto)

            # Pergunta ao usuário se ele
            continuar_inserindo = input("Deseja continuar inserindo? [S]im ou [N]ão: ").lower()

            if continuar_inserindo == 'sim' or continuar_inserindo == 's':
                repetir_lista = False
                pass

            elif continuar_inserindo == 'não' or continuar_inserindo == 'n' or continuar_inserindo == 'nao':
                repetir_lista = True
                
                break
            else:
                print("Digite um valor válido.")
                
        print('\n')
        mostrar_lista()

    if opcao == 'a':

        while True:

            # Mostra os itens da lista
            mostrar_lista()

            # Try/Except para evitar que o usuário adicione um índice maior ou menor que a quantidade
            # de valores na lista.

            try:
                # Pede para que o usuário apague o item baseado no item da lista
                index_apagar = int(input("\nDigite o número do produdo que deseja apagar: "))

                # Mostra o item apagado e o apaga
                print(f"\nVocê apagou o item: {lista_compras[index_apagar]}")
                lista_compras.pop(index_apagar)
                
                # Mostra os itens da lista
                mostrar_lista()
                
                item_valido = True

            # Emite uma mensagem de erro caso o usuário coloque um número diferente de um inteiro
            except ValueError:
                print("Digite um dígito inteiro! ")
                item_valido = False

            # Emite um erro caso o índice não esteja na lista
            except IndexError:
                print("Item não existe na lista ")
                item_valido = False

            # Emite um errro caso
            except:
                print("Erro desconhecido ")
            if item_valido == True:
                break

            
    # Caso queira apenas mostrar a lista
    if opcao == 'l':
        mostrar_lista()

    # Função sair
    if opcao == 's':
        exit()