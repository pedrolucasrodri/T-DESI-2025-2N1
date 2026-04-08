import unittest
from mat_2 import somar

class testeMat(unittest.TestCase):
    def teste_soma(self):
        resultado = somar (2,2)
        self.assertEqual(resultado,4)

if __name__ == "__main__":
    unittest.main()
