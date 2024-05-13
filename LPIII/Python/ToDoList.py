class ToDo:

    def __init__(self):
        self.id = 0
        self.task = list()

    def menu(self):
        print('''
            1 - Listar Tarefas
            2 - Adicionar tarefa
            3 - Marcar tarefas como concluida
            4 - Editar tarefa
            5 - Sair
                ''')

        return int(input("Sua escolha: "))
        
    def add(self):
        self.id = self.id + 1

        desc = input("Descrição da tarefa: ").capitalize()
        task = {"id":self.id ,"descricao":desc, "status":"[ ]"}

        self.task.append(task)

        print("Tarefa resgistrada\n")

    def listar(self):
        print("Lista de tarefas:")
        for c in self.task:
            print(f'{c["id"]}. {c["descricao"]} {c["status"]}')

    def conclude(self):
        id = int(input("Qual o id da tarefa: "))
        for c in self.task:
            if c["id"] == id:
                copia = c
                self.task.remove(c)
                copia["status"] = "[X]"
                self.task.insert(0,copia)
                print("Tarefa marcada como concluída\n")

    def edit(self):
        id = int(input("Qual o id da tarefa: "))
        for c in self.task:
            if c["id"] == id:
                desc = input("Descrição da tarefa: ").capitalize()
                c["descricao"] = desc
                print("Tarefa editada\n")



def main():
    App = ToDo()

    while True:
        op = App.menu()

        if op == 1:
            App.listar()
        elif op == 2:
            App.add()
        elif op == 3:
            App.conclude()
        elif op == 4:
            App.edit()
        elif op == 5:
            break
        else:
            print("Digite uma opção correta")
        

if __name__ == '__main__':
    main()