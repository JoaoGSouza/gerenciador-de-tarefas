import json
from usuario import Usuario
from tarefa import Tarefa
from config import ARQUIVO_JSON


class GerenciadorDeTarefas:
    def __init__(self):
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON."""
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"usuarios": [], "tarefas": []}

    def salvar_dados(self):
        """Salva os dados no arquivo JSON."""
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as file:
            json.dump(self.dados, file, indent=4, ensure_ascii=False)

    def adicionar_usuario(self, nome, email):
        """Adiciona um usuário ao sistema."""
        if any(u["email"] == email for u in self.dados["usuarios"]):
            print(f"Usuário com e-mail {email} já cadastrado!")
            return

        usuario = Usuario(nome, email)
        self.dados["usuarios"].append(usuario.__dict__)
        self.salvar_dados()
        print(f"Usuário {nome} adicionado com sucesso!")

    def excluir_usuario(self, email):
        """Exclui um usuário do sistema e o remove de todas as tarefas."""
        novos_usuarios = [u for u in self.dados["usuarios"] if u["email"] != email]

        if len(novos_usuarios) == len(self.dados["usuarios"]):
            print(f"Nenhum usuário encontrado com o e-mail {email}.")
            return

        self.dados["usuarios"] = novos_usuarios

        # Remover o usuário das tarefas onde ele era observador
        for tarefa in self.dados["tarefas"]:
            if email in tarefa["observadores"]:
                tarefa["observadores"].remove(email)

        self.salvar_dados()
        print(f"Usuário com e-mail {email} excluído com sucesso!")

    def adicionar_tarefa(self, titulo, prioridade, emails_observadores):
        """Adiciona uma tarefa e vincula observadores."""
        if any(t["titulo"] == titulo for t in self.dados["tarefas"]):
            print(f"Já existe uma tarefa com o título '{titulo}'.")
            return

        tarefa = Tarefa(titulo, prioridade)
        for email in emails_observadores:
            if any(u["email"] == email for u in self.dados["usuarios"]):
                tarefa.adicionar_observador(email)

        self.dados["tarefas"].append(tarefa.__dict__)
        self.salvar_dados()
        print(f"Tarefa '{titulo}' adicionada com sucesso!")

    def excluir_tarefa(self, titulo):
        """Exclui uma tarefa do sistema."""
        novas_tarefas = [t for t in self.dados["tarefas"] if t["titulo"] != titulo]

        if len(novas_tarefas) == len(self.dados["tarefas"]):
            print(f"Nenhuma tarefa encontrada com o título '{titulo}'.")
            return

        self.dados["tarefas"] = novas_tarefas
        self.salvar_dados()
        print(f"Tarefa '{titulo}' excluída com sucesso!")

    def remover_usuario_de_tarefa(self, titulo_tarefa, email_usuario):
        """Remove um usuário específico de uma tarefa utilizando o método da classe Tarefa."""
        for tarefa_data in self.dados["tarefas"]:
            if tarefa_data["titulo"] == titulo_tarefa:
                tarefa = Tarefa(
                    titulo=tarefa_data["titulo"],
                    prioridade=tarefa_data["prioridade"],
                    observadores=tarefa_data["observadores"]
                )
                tarefa.remover_observador(email_usuario)
                tarefa_data["observadores"] = tarefa.observadores  # Atualiza os dados no gerenciador
                self.salvar_dados()
                print(f"Usuário {email_usuario} removido da tarefa '{titulo_tarefa}'.")
                return

        print(f"Tarefa '{titulo_tarefa}' não encontrada.")

    def adicionar_usuario_em_tarefa(self, titulo_tarefa, email_usuario):
        """Adiciona um usuário específico a uma tarefa existente."""
        for tarefa_data in self.dados["tarefas"]:
            if tarefa_data["titulo"] == titulo_tarefa:
                tarefa = Tarefa(
                    titulo=tarefa_data["titulo"],
                    prioridade=tarefa_data["prioridade"],
                    observadores=tarefa_data["observadores"]
                )
                if any(u["email"] == email_usuario for u in self.dados["usuarios"]):
                    tarefa.adicionar_observador(email_usuario)
                    tarefa_data["observadores"] = tarefa.observadores  # Atualiza os dados no gerenciador
                    self.salvar_dados()
                    print(f"Usuário {email_usuario} adicionado à tarefa '{titulo_tarefa}'.")
                    return
                else:
                    print(f"O e-mail '{email_usuario}' não pertence a nenhum usuário cadastrado.")
                    return

        print(f"Tarefa '{titulo_tarefa}' não encontrada.")

    def alterar_status_tarefa(self, titulo, novo_status):
        """Altera o status de uma tarefa e notifica os observadores."""
        for tarefa_data in self.dados["tarefas"]:
            if tarefa_data["titulo"] == titulo:
                tarefa = Tarefa(
                    titulo=tarefa_data["titulo"],
                    prioridade=tarefa_data["prioridade"],
                    observadores=tarefa_data["observadores"]
                )
                tarefa.status = novo_status
                tarefa_data["status"] = novo_status  # Atualiza os dados no gerenciador
                self.salvar_dados()
                mensagem = f"A tarefa '{titulo}' foi atualizada! Status: {novo_status}"

                # Notificar observadores
                for email in tarefa.observadores:
                    print(f"Notificação enviada para {email}: {mensagem}")

                return

        print(f"Tarefa '{titulo}' não encontrada.")
