import unittest
from division import dividir

class TestRestar(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        self.assertEqual(dividir(0, 2), 0)
        self.assertEqual(dividir(2, 0), "Error dividiendo entre 0")

if __name__ == "__main__":
    unittest.main()