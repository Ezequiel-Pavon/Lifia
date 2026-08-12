import unittest

def resta(a, b):
    """
    Calcula la resta de dos números.
    
    Args:
        a (int | float): El minuendo.
        b (int | float): El sustraendo.
        
    Returns:
        int | float: El resultado de la resta.
        
    Raises:
        TypeError: Si los argumentos no son numéricos.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Los argumentos deben ser numéricos. Recibidos: {type(a)}, {type(b)}")
    return a - b

class TestResta(unittest.TestCase):
    """Suite de pruebas para la función resta."""

    def test_numeros_positivos(self):
        """Prueba con enteros positivos."""
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(10, 2), 8)

    def test_con_cero(self):
        """Prueba cuando uno de los operandos es cero."""
        self.assertEqual(resta(5, 0), 5)
        self.assertEqual(resta(0, 5), -5)
        self.assertEqual(resta(0, 0), 0)

    def test_negativos(self):
        """Prueba con números negativos."""
        self.assertEqual(resta(-2, -3), 1)
        self.assertEqual(resta(-5, 3), -8)
        self.assertEqual(resta(5, -3), 8)

    def test_decimales(self):
        """Prueba con números decimales."""
        self.assertAlmostEqual(resta(5.5, 2.3), 3.2, places=1)
        self.assertAlmostEqual(resta(10.0, 0.1), 9.9, places=1)

    def test_grandes_cifras(self):
        """Prueba con números grandes."""
        self.assertEqual(resta(1000000, 1), 999999)

    def test_error_tipo_no_numerico(self):
        """Prueba que lanza TypeError con entradas no numéricas."""
        with self.assertRaises(TypeError):
            resta("5", 3)
        with self.assertRaises(TypeError):
            resta(5, "3")
        with self.assertRaises(TypeError):
            resta("a", "b")

if __name__ == "__main__":
    unittest.main()