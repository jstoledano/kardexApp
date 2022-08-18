from django.test import TestCase


class PruebaDeHumo(TestCase):

    def test_suma_incorrecta(self):
        self.assertEqual(1 + 1, 3)
