#Atividade POO Atividade 02 - Capítulo 02 do livro Código do Diagrama UML
#Docente: Filipe Dwan
#Discentes: Lucas Gabriel Rocha Constancio, Yan dos Santos Teixeira 

class Tarefa():
    def __init__(self, Titulo, Data = None, Descricao = None, Status = 'A fazer', Prioridade = 'Baixa'):
        self.titulo = Titulo
        self.data = Data
        self.prioridade = Prioridade
        self.descricao = Descricao
        self.status = Status

    def busca(self, termo_buscado:str):
        if termo_buscado.lower() in self.titulo.lower():
            return True
        return False

    def Info(self):
        print(f"Título: {self.titulo}")
        print(f"Data: {self.data}")
        print(f"Descrição: {self.descricao}")
        print(f"Status: {self.status}")
        print(f"Prioridade:{self.prioridade}")

