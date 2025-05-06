# Função que verifica se um número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Teste unitário para a função par_ou_impar
import unittest

class TestParOuImpar(unittest.TestCase):
    
    def test_numero_par(self):
        # Testa se o número 4 é corretamente identificado como par
        self.assertEqual(par_ou_impar(4), "Par")

    def test_numero_impar(self):
        # Testa se o número 7 é corretamente identificado como ímpar
        self.assertEqual(par_ou_impar(5), "Ímpar")

    def test_zero(self):
        # Testa se o número 0 é tratado como par
        self.assertEqual(par_ou_impar(0), "Par")

# Executa os testes se o arquivo for rodado diretamente
if __name__ == '__main__':
    unittest.main()
