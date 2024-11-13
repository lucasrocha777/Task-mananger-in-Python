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
        print(self.titulo, self.data)


if __name__ == '__main__':
    t1 = str(input('Digite o Titulo da tarefa: '))
    t2 = str(input('Digite o Titulo da tarefa: '))

    t1 = Tarefa.Titulo
    #Tarefa = t1, t2 

    #t1.titulo = 'Tarefa POO'
    #t1.Alterar_Titulo('Tarefa POO')

    print(f"Tarefa 1: {Tarefa.Titulo}\n Tarefa 2:\n")

    print("==== Tarefa cadastrada! ====")
    