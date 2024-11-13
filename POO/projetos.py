class Projetos():
    def __init__(self, Nome, Descricao, Classificacao, Validade):
        self.nome_proj = Nome
        self.descricao = Descricao
        self.classificacao = Classificacao
        self.data_val = Validade

    def adicionar_Lista(self, Lista):
        self.add_lista = Lista

    def excluir_Lista(self, Lista):
        self.exclu_lista = Lista

    def concluir_Proj(self, Projeto):
        self.concluir_proj = Projeto
    def excluir_Proj(self, Projeto):
    self.excluir_proj = Projeto