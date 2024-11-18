#Atividade POO Atividade 02 - Capítulo 02 do livro Código do Diagrama UML
#Docente: Filipe Dwan
#Discentes: Lucas Gabriel Rocha Constancio, Yan dos Santos Teixeira 

class Projetos():
    def __init__(self, nome, descricao, classificacao, validade):
        self.nome = nome
        self.descricao = descricao
        self.classificacao = classificacao
        self.data_val = validade
        self.listas_tarefas = []

    
    def adicionar_lista(self, lista_tarefas):
        self.listas_tarefas.append(lista_tarefas)

    def remover_lista_tarefa(self, lista_tarefas):
        self.listas_tarefas(lista_tarefas)

    def listar_listas(self):
        return self.listas_tarefas
    
