#Atividade POO Atividade 02 - Capítulo 02 do livro Código do Diagrama UML
#Docente: Filipe Dwan
#Discentes: Lucas Gabriel Rocha Constancio, Yan dos Santos Teixeira 

import time

# gerenciador_tarefas.py
from usuario import Usuario
from projetos import Projetos
from lista_de_tarefas import Lista_Tarefas
from tarefa import Tarefa



def main():
    usuario = None

    while True:
        print("\nMenu:")
        print("1. Criar usuário")
        print("2. Adicionar projeto")
        print("3. Adicionar lista de tarefas ao projeto")
        print("4. Adicionar tarefa à lista")
        print("5. Listar projetos")
        print("6. Listar listas de tarefas de um projeto")
        print("7. Listar tarefas de uma lista")
        print("8. Remover tarefa")
        print("9. Remover projeto")
        print("10. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_usuario = input("Digite o nome do usuário: ")
            email_usuario = input("Digite o email do usuário: ")
            senha_usuario = input("Digite a senha do usuário: ")
            usuario = Usuario(nome_usuario, email_usuario, senha_usuario)
            print(f"Usuário '{usuario.nome}' criado com sucesso!")
            time.sleep(2)


        elif opcao == '2':
            if usuario is None:
                print("Você precisa criar um usuário primeiro.")
                continue
            nome_projeto = input("Digite o nome do projeto: ")
            descricao_projeto = input("Digite a descrição do projeto: ")
            classificacao_projeto = input("Digite a classificação do projeto: ")
            validade_projeto = input("Digite a validade do projeto: ")
            projeto = Projetos(nome_projeto, descricao_projeto, classificacao_projeto, validade_projeto)
            usuario.adicionar_projeto(projeto)
            print(f"Projeto '{projeto.nome}' adicionado ao usuário '{usuario.nome}'.")
            time.sleep(2)


        elif opcao == '3':
            if usuario is None or not usuario.projetos:
                print("Você precisa ter um usuário e pelo menos um projeto.")
                time.sleep(2)
                continue
            for i, proj in enumerate(usuario.projetos):
                print(f"{i + 1}. {proj.nome}")
            indice = int(input("Escolha o projeto para adicionar a lista: ")) - 1
            nome_lista = input("Digite o nome da lista de tarefas: ")
            data_lista = input("Digite a data da lista: ")
            lista_tarefas = Lista_Tarefas(nome_lista, data_lista)
            usuario.projetos[indice].adicionar_lista(lista_tarefas)
            print(f"Lista '{lista_tarefas.nome}' adicionada ao projeto '{usuario.projetos[indice].nome}'.")
            time.sleep(2)


        elif opcao == '4':
            if usuario is None or not usuario.projetos:
                print("Você precisa ter um usuário e pelo menos um projeto.")
                time.sleep(2)
                continue
            for i, proj in enumerate(usuario.projetos):
                print(f"{i + 1}. {proj.nome}")
            indice_projeto = int(input("Escolha o projeto: ")) - 1
            for j, lista in enumerate(usuario.projetos[indice_projeto].listas_tarefas):
                print(f"{j + 1}. {lista.nome}")
            indice_lista = int(input("Escolha a lista de tarefas: ")) - 1
            titulo_tarefa = input("Digite o título da tarefa: ")
            data_tarefa = input("Digite a data da tarefa: ")
            descricao_tarefa = input("Digite a descrição da tarefa: ")
            prioridade_tarefa = input("Digite a prioridade da tarefa (Baixa, Média, Alta): ")
            tarefa = Tarefa(titulo_tarefa, data_tarefa, descricao_tarefa, prioridade=prioridade_tarefa)
            usuario.projetos[indice_projeto].listas_tarefas[indice_lista].adicionar_lista(tarefa)
            print(f"Tarefa '{tarefa.titulo}' adicionada à lista '{usuario.projetos[indice_projeto].listas_tarefas[indice_lista].nome}'.")
            time.sleep(2)

        elif opcao == '5':
            if usuario is None or not usuario.projetos:
                print("Você não tem projetos.")
                time.sleep(2)
                continue
            for proj in usuario.listar_projetos():
                print(proj.nome)
                time.sleep(2)

        elif opcao == '6':
            if usuario is None or not usuario.projetos:
                print("Você não tem projetos.")
                time.sleep(2)
                continue
            for i, proj in enumerate(usuario.projetos):
                print(f"{i + 1}. {proj.nome}")
            indice = int(input("Escolha o projeto: ")) - 1
            for lista in usuario.projetos[indice].listar_listas():
                print(lista.nome)
                time.sleep(2)

        elif opcao == '7':
            if usuario is None or not usuario.projetos:
                print("Você não tem projetos.")
                time.sleep(2)
                continue
            for i, proj in enumerate(usuario.projetos):
                print(f"{i + 1}. {proj.nome}")
            indice_projeto = int(input("Escolha o projeto: ")) - 1
            for j, lista in enumerate(usuario.projetos[indice_projeto].listas_tarefas):
                print(f"{j + 1}. {lista.nome}")
            indice_lista = int(input("Escolha a lista de tarefas: ")) - 1
            for tarefa in usuario.projetos[indice_projeto].listas_tarefas[indice_lista].listar_tarefas():
                print(tarefa.titulo)
                time.sleep(2)

        elif opcao == '8':
            if usuario is None or not usuario.projetos:
                print("Você não tem projetos.")
                time.sleep(2)
                continue
            for i, proj in enumerate(usuario.projetos):
                print(f"{i + 1}. {proj.nome}")
            indice_projeto = int(input("Escolha o projeto: ")) - 1
            for j, lista in enumerate(usuario.projetos[indice_projeto].listas_tarefas):
                print(f"{j + 1}. {lista.nome}")
            indice_lista = int(input("Escolha a lista de tarefas: ")) - 1
            for k, tarefa in enumerate(usuario.projetos[indice_projeto].listas_tarefas[indice_lista].listar_tarefas()):
                print(f"{k + 1}. {tarefa.titulo}")
            indice_tarefa = int(input("Escolha a tarefa para remover: ")) - 1
            usuario.projetos[indice_projeto].listas_tarefas[indice_lista].remover_tarefa(usuario.projetos[indice_projeto].listas_tarefas[indice_lista].tarefas[indice_tarefa])
            print("Tarefa removida com sucesso.")
            time.sleep(2)

        elif opcao == '9':
            if usuario is None or not usuario.projetos:
                print("Você não tem projetos.")
                time.sleep(2)
                continue
            for i, proj in enumerate(usuario.projetos):
                print(f"{i + 1}. {proj.nome}")
            indice = int(input("Escolha o projeto para remover: ")) - 1
            usuario.remover_projeto(usuario.projetos[indice])
            print("Projeto removido com sucesso.")
            time.sleep(2)

        elif opcao == '10':
            print("Saindo...")
            time.sleep(2)
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()