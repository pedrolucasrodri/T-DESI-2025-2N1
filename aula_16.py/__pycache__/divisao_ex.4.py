import unittest

def dividir(a,b):
    return a/b

class TesteMatematica(unittest.TestCase):
    def test_div_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10,0)

    def test_divi_norm(self):
        resultado = dividir(10,2)
        self.assertAlmostEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()
    