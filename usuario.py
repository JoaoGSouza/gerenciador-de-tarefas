from observer import Observer


class Usuario(Observer):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def atualizar(self, mensagem: str):
        """Simula o envio de uma notificação para o usuário."""
        print(f"Notificação para {self.nome} ({self.email}): {mensagem}")
