import unittest
from tarefa import Tarefa


class TestTarefa(unittest.TestCase):
    def test_criacao_tarefa(self):
        tarefa = Tarefa("Fazer relatório", "Alta")
        self.assertEqual(tarefa.titulo, "Fazer relatório")
        self.assertEqual(tarefa.status, "A fazer")
        self.assertEqual(tarefa.prioridade, "Alta")
        self.assertEqual(tarefa.observadores, [])

    def test_adicionar_remover_observador(self):
        tarefa = Tarefa("Comprar mantimentos", "Média")
        tarefa.adicionar_observador("joao@email.com")
        self.assertIn("joao@email.com", tarefa.observadores)

        tarefa.remover_observador("joao@email.com")
        self.assertNotIn("joao@email.com", tarefa.observadores)


if __name__ == "__main__":
    unittest.main()
