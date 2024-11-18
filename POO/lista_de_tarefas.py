#Atividade POO Atividade 02 - Capítulo 02 do livro Código do Diagrama UML
#Docente: Filipe Dwan
#Discentes: Lucas Gabriel Rocha Constancio, Yan dos Santos Teixeira 

#defindo a classe lista de taferas 
class Lista_Tarefas:
    def __init__(self, nome, data, prioridade = 'Baixa'):
        self.nome = nome
        self.data = data
        self.prioridade = prioridade
        self.tarefas = []

    def adicionar_lista(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

    def listar_tarefas(self):
        return self.tarefas