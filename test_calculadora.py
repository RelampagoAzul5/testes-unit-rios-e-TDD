import unittest
from calculadora import soma, subtrai
class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5),10)
    
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10,10,20),
            (5,5,10),
            (1.5,1.5,3.0),
            (-5,5,0),
            (100,100,200),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)
    def test_soma_x_nao_e_int_ou_float_deve_retornar_assetionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)
    def test_soma_y_nao_e_int_ou_float_deve_retornar_assetionerror(self):
        with self.assertRaises(AssertionError):
            soma(11, '0')

    def test_subtrai_5_de_8_deve_retornar_3(self):
        self.assertEqual(subtrai(8,5),3)
    def test_subtrai_20_de_4_negativo_deve_retornar_24_negativo(self):
        self.assertEqual(subtrai(-4,20),-24)

    def test_subtrai_varias_entradas(self):
        x_y_saidas =(
            (20,10,10),
            (4,2,2),
            (10,4,6),
            (7,2,5),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x,y,saida= x_y_saida
                self.assertEqual(subtrai(x,y),saida)

    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assetionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('11', 0)
    def test_subtrai_y_nao_e_int_ou_float_deve_retornar_assetionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(11, '0')



unittest.main(verbosity=2)
