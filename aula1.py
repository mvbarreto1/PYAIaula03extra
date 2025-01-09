tarefas = []

def adicionar_tarefas(tarefa):
    tarefas.append(tarefa)

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        print(f"{tarefa} REMOVIDA com sucesso!")
        tarefas.remove(tarefa)
    else:
        print("Tarefa não encontrada!")

def exibir_tarefas():
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

while True:
    opcao = input("1. Adicionar | 2. Remover | 3. Exibir | 4. Sair: \n")

    if opcao == "1":
        tarefa = input("Digite o nome da Tarefa que deseja Adicionar: \n")

        adicionar_tarefas(tarefa)

    elif opcao == "2":
        tarefa = input("Digite o nome da Tarefa que deseja Remover: \n")

        remover_tarefa(tarefa)

    elif opcao == "3":
        exibir_tarefas()

    elif opcao == "4":
        break

    else:
        print("Opção invalida, tente novamente!")