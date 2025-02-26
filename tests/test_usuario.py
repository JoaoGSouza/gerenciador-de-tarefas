import unittest
from usuario import Usuario


class TestUsuario(unittest.TestCase):
    def test_criacao_usuario(self):
        usuario = Usuario("Alice", "alice@email.com")
        self.assertEqual(usuario.nome, "Alice")
        self.assertEqual(usuario.email, "alice@email.com")


if __name__ == "__main__":
    unittest.main()
