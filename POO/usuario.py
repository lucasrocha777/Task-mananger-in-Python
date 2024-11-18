class Usuario():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)
    
    def listar_projetos(self):
        return self.projetos
    
    def remover_projeto(self, projeto):
        if projeto in self.projetos:
            self.projetos.remove(projeto)
    