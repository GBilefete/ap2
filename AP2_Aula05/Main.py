from Pilha import Pilha

pilha = Pilha()
opcao = "" 

while(opcao != "0"):
    print("\n----------------------")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Retorna o topo da pilha")
    print("4 - Imprimir")
    print("0 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        dado = input("Informe um valor: ")
        pilha.push(dado)

    if opcao == "2":
        pilha.pop()

    if opcao == "3":
        print(pilha.peek())

    if opcao == "4":
        print(pilha)