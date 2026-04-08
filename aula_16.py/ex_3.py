import unittest

class TesteCicloDeVida(unittest.TestCase):

    def setUp(self):
        print("\n---Preparando o ambiente---")

    def tearDown(self):
        print("---Limpando---\n")
    
    def test_primeiro_teste(self):
        print("Executando o teste 1...")
        pass

    def test_segundo_teste(self):
        print("Executando o teste 2...")
        pass

    def test_terceiro_teste(self):
        print("Executando o teste 3...")
        pass

if __name__ == '__main__':
    unittest.main()
    