class Tarefa:
    def __init__(self, titulo, prioridade, observadores=None):
        self.titulo = titulo
        self.status = "A fazer"
        self.prioridade = prioridade
        self.observadores = observadores if observadores else []

    def adicionar_observador(self, observador_email):
        """Adiciona um observador à tarefa."""
        if observador_email not in self.observadores:
            self.observadores.append(observador_email)

    def remover_observador(self, observador_email):
        """Remove um observador da tarefa."""
        if observador_email in self.observadores:
            self.observadores.remove(observador_email)
