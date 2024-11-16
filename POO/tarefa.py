class Tarefa():
    def __init__(self, Titulo, Data = None, Descricao = None, Status = 'A fazer', Prioridade = 'Baixa'):
        self.titulo = Titulo
        self.data = Data
        self.prioridade = Prioridade
        self.descricao = Descricao
        self.status = Status

    def __str__(self):
        print("Insira o nome e a Descrição: ")
        return f"Titulo: {self.titulo} \nDescrição: {self.descricao}"
        

    def busca(self, termo_buscado:str):
        if termo_buscado.lower() in self.titulo.lower():
            return True
        return False

    def Info(self):
        print(self.titulo, self.data)


if __name__ == '__main__':
    t1 = str(input('Digite o Titulo da tarefa: '))
    t2 = str(input('Digite o Titulo da tarefa: '))
    

    #t1.titulo = 'Tarefa POO'
    #t1.Alterar_Titulo('Tarefa POO')

    print(f"Tarefa 1: {t1}\n Tarefa 2: {t2}\n")

    print("==== Tarefa cadastrada! ====")
    