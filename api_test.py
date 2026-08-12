import unittest
from fastapi.testclient import TestClient
from ejemplo_api import app

class TestAPI(unittest.TestCase):
    """Suite de pruebas para la API FastAPI."""

    def setUp(self):
        """Configura el cliente de prueba antes de cada método."""
        self.client = TestClient(app)

    def _assert_success(self, response, expected_status=200):
        """Verifica respuesta exitosa y estructura JSON."""
        self.assertEqual(response.status_code, expected_status, 
                        f"Status code incorrecto: {response.status_code}")
        self.assertIsInstance(response.json(), dict, "La respuesta no es un diccionario JSON")

    def _assert_error(self, response, expected_status=422):
        """Verifica respuesta de error y estructura."""
        self.assertEqual(response.status_code, expected_status, 
                        f"Status code incorrecto para error: {response.status_code}")
        self.assertIn("detail", response.json(), "La respuesta de error no contiene 'detail'")

    def test_root(self):
        """Prueba el endpoint raíz '/'."""
        response = self.client.get("/")
        self._assert_success(response)
        
        data = response.json()
        self.assertEqual(data.get("mensaje"), "Hola mundo", 
                        "El mensaje de bienvenida no coincide")

    def test_suma_exitosa(self):
        """Prueba suma correcta con enteros positivos."""
        response = self.client.get("/suma?a=2&b=3")
        self._assert_success(response)
        
        data = response.json()
        self.assertIn("resultado", data, "Falta el campo 'resultado'")
        self.assertEqual(data["resultado"], 5, "El resultado de la suma es incorrecto")

    def test_suma_decimales(self):
        """Prueba suma con valores decimales."""
        response = self.client.get("/suma?a=2.5&b=3.5")
        self._assert_success(response)
        
        data = response.json()
        self.assertAlmostEqual(data["resultado"], 6.0, places=1)

    def test_suma_negativos(self):
        """Prueba suma con números negativos."""
        response = self.client.get("/suma?a=-5&b=-3")
        self._assert_success(response)
        
        data = response.json()
        self.assertEqual(data["resultado"], -8, "La suma de negativos es incorrecta")

    def test_suma_cero(self):
        """Prueba suma con un valor cero."""
        response = self.client.get("/suma?a=0&b=10")
        self._assert_success(response)
        
        data = response.json()
        self.assertEqual(data["resultado"], 10, "La suma con cero es incorrecta")

    def test_suma_parametro_falta(self):
        """Prueba suma sin parámetros obligatorios."""
        response = self.client.get("/suma")
        self._assert_error(response)

    def test_suma_parametro_falta_uno(self):
        """Prueba suma con solo un parámetro."""
        response = self.client.get("/suma?a=5")
        self._assert_error(response)

    def test_suma_valor_no_numerico(self):
        """Prueba suma con valores no numéricos."""
        response = self.client.get("/suma?a=2&b=hola")
        self._assert_error(response)

    def test_suma_valor_no_numerico_a(self):
        """Prueba suma con el primer parámetro no numérico."""
        response = self.client.get("/suma?a=hola&b=3")
        self._assert_error(response)

    def test_suma_valor_vacio(self):
        """Prueba suma con parámetros vacíos."""
        response = self.client.get("/suma?a=&b=")
        self._assert_error(response)

if __name__ == "__main__":
    unittest.main()  