class Usuario():
    def __init__(self, Nome, Email, Senha):
        self.nome = Nome
        self.email = Email
        self.senha = Senha
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)
    
    def listar_projetos(self):
        return self.projetos