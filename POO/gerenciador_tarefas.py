from usuario import Usuario
from tarefa import Tarefa

while True:
    print("======/ Menu \======")
    print("1. Adicionar tarefa")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        titulo_tar = input("Digite o titulo da tarefa: ")
        tarefa = Tarefa(titulo_tar)
        print(f"Titulo: {titulo_tar}")
    else:
        print("Opcao invalida!")
