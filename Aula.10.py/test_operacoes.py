import unittest 
from operacoes import somar, eh_par

class TestMatematica(unittest.TestCase):
    def test_somar(self):
        resultado = somar(10, 5)
        self.assertEqual(resultado,15)
    def test_eh_par (self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(7))

if __name__ == '__main__':
    unittest.main()   