from gerenciador import GerenciadorDeTarefas

gerenciador = GerenciadorDeTarefas()

program = True

while program:
    opcao = input("Selecione uma opcao:\n"
                  "1 - Adicionar usuario\n"
                  "2 - Excluir usuario\n"
                  "3 - Adicionar tarefa\n"
                  "4 - Excluir tarefa\n"
                  "5 - Designar usuario a uma tarefa\n"
                  "6 - Remover usuario de uma tarefa\n"
                  "7 - Alterar status de tarefa\n"
                  "0 - Sair\n")

    print("=================================================================")

    if opcao == "1":
        print("Adicionar usuario\n")

        nome = input("Nome do usuário:\n")
        email = input("Email do usuário:\n")

        gerenciador.adicionar_usuario(nome, email)
    elif opcao == "2":
        print("Excluir usuario\n")

        email = input("Email do usuário a ser excluído:\n")

        gerenciador.excluir_usuario(email)
    elif opcao == "3":
        print("Adicionar tarefa\n")

        titulo = input("Título da tarefa:\n")
        prioridade = input("Prioridade da tarefa (Baixa/Média/Alta):\n")
        email = input("Email de um usuario responsavel pela tarefa:\n")

        gerenciador.adicionar_tarefa(titulo, prioridade, [email])
    elif opcao == "4":
        print("Excluir tarefa\n")

        titulo = input("Título da tarefa a ser excluída:\n")

        gerenciador.excluir_tarefa(titulo)
    elif opcao == "5":
        print("Designar usuario a uma tarefa\n")

        titulo = input("Titulo da tarefa:\n")
        email = input("Email do usuario a ser designado para a tarefa:\n")

        gerenciador.adicionar_usuario_em_tarefa(titulo, email)
    elif opcao == "6":
        print("Remover usuario de uma tarefa\n")

        titulo = input("Titulo da tarefa:\n")
        email = input("Email do usuario a ser removido da tarefa:\n")

        gerenciador.remover_usuario_de_tarefa(titulo, email)
    elif opcao == "7":
        print("Alterar status de tarefa\n")

        titulo = input("Titulo da tarefa:\n")
        novo_status = input("Novo status da tarefa:\n")

        gerenciador.alterar_status_tarefa(titulo, novo_status)
    else:
        program = False

    print("=================================================================")
