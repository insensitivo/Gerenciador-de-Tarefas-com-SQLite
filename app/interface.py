from app.tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    remover_tarefa
)


def menu():
    while True:
        print("=== GERENCIADOR DE TAREFAS ===")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()

        elif opcao == "2":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            adicionar_tarefa(titulo, descricao)

        elif opcao == "3":
            try:
                id_tarefa = int(input("Digite o ID da tarefa: "))
                concluir_tarefa(id_tarefa)
            except ValueError:
                print("Digite um número válido.\n")

        elif opcao == "4":
            try:
                id_tarefa = int(input("Digite o ID da tarefa: "))
                remover_tarefa(id_tarefa)
            except ValueError:
                print("Digite um número válido.\n")

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.\n")