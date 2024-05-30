class Tarefa:
    __staticvar ={"id":0}

    def __init__(self):
        self.__staticvar["id"] = self.__staticvar["id"] + 1
        self.__id = self.__staticvar["id"]
        self.__desc = ""
        self.__status = '[ ]'

    def getid(self):
        return self.__id
    
    def getdesc(self):
        return self.__desc
    
    def getstatus(self):
        return self.__status
    
    def setdesc(self, desc):
        self.__desc = desc

    def setStatus(self, bool):
        if bool:
            self.__status = '[X]'
        else:
            self.__status = '[ ]'

class ToDo:

    def __init__(self):
        self.task = list()
                
    def add(self):
        tarefa = Tarefa()
        tarefa.setdesc(input("Descrição da tarefa: ").capitalize())
        task = {"id":tarefa.getid() ,"descricao":tarefa.getstatus(), "status":"[ ]"}

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
                # self.task.insert(0, self.task.pop(self.task.index(c))) pop retorna elemento exlcuido. index a posição
                print("Tarefa marcada como concluída\n")
                break

    def edit(self):
        id = int(input("Qual o id da tarefa: "))
        for c in self.task:
            if c["id"] == id:
                desc = input("Descrição da tarefa: ").capitalize()
                c["descricao"] = desc
                print("Tarefa editada\n")
                break



        
def menu():
    print('''
        1 - Listar Tarefas
        2 - Adicionar tarefa
        3 - Marcar tarefas como concluida
        4 - Editar tarefa
        5 - Sair
            ''')

    return int(input("Sua escolha: "))

def main():
    App = ToDo()

    while True:
        op = menu()

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