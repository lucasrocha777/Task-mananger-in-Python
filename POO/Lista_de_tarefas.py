#defindo a classe lista de taferas 
class Lista_Tarefas:
    def __init__(self, Nome, Data, Prioridade):
        self.nome = Nome
        self.data = Data
        self.prioridade = Prioridade
        self.tarefas = []

#/////////////////////////Métodos\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

#Menu da Lista de Tarefas
    def menu(self):
        print("======= 𝑳𝒊𝒔𝒕𝒂 𝒅𝒆 𝑻𝒂𝒓𝒆𝒇𝒂𝒔 =======")
        print("________________________________")
        print("║ 1. Procurar Tarefa           ║")
        print("║ 2. Concluir Tarefa           ║")
        print("║ 3. Editar Tarefa             ║")
        print("║ 4. Excluir Tarefa            ║")
        print("║ 5. Data de entrega           ║")
        print("║ 6. Sair                      ║")
        print("────────────────────────────────")

#Definindo para escolher as opções
    def exibir_opcoes(self):
        while True:
            try:
                escolha = (int(input("Qual opção você quer mexer: ")))
                
                if escolha == 1:
                    nome_tarefa = input("Digite o nome da tarefa que procura: ")
                    print(self.procurar_tarefas(nome_tarefa))
                elif escolha == 2:
                    concluir_tarefas()
                elif escolha == 3:
                    print("Editar Tarefa")
                    editar_tarefas()
                elif escolha == 4:
                    excluir_tarefa()
                    print("Saindo do programa")
                elif escolha == 5:
                    data_de_entrega()
                elif escolha == 6:
                    exit()
                    print("Saindo do programa")
                else:
                    print("Opção invalida!")
            except ValueError:
                print(" Digite novamente!")

#Procurando tarefas adiciona na lista.
    def adicionar_tarefa(self, tarefa):
       self.tarefas.append(tarefa)
       print(f"Tarefa '{tarefa}' adicionada com sucesso!")

#Procurar as taferas se está adcionada na lista ou não
    def procurar_tarefas (self, nome_tarefa):
        for tarefa in self.tarefas:
            if tarefa.nome.lower() == nome_tarefa.lower():
                return f" A tarefa '{nome_tarefa}' foi encontrada." #True
            else:
                return f"A tarefa'{nome_tarefa}' não existe na lista." #False

#Criando uma instância da classe
#minha_lista = Lista_Tarefas("Trabalho", "2024-11-20", "Alta")

#resultado = minha_lista.procurar_tarefas(nome_da_tarefa)
#print(resultado)

#Concluindo tarefas
    def concluir_taferas(self, Tarefa):
        self.tarefas.remove(Tarefa)
        print("tarefa entregue")

#Editando as tarefas
    def editar_tarefas(self, Tarefas):
        print("")
        self.editar_tarefas = Tarefas

#Excluindo Tarefas
    #def excluindo_tarefas(self, Tarefa):
        #self.excluindo_tarefas = self.tarefas.remove(Tarefa)
#Data de entrega
# O usúario conseguira vê as datas de entregas das atividades
    #def data_de_entrega(self, Tarefa, Data):
        #self.data_de_entrega = Data
        
#atividade1 = Lista_Tarefas('ativade de POO','13/11/2024', 'Alta') print( atividade1.nome, atividade1.data, atividade1.prioridade)


