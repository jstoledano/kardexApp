from django.test import TestCase


class PruebaPortada(TestCase):

    def test_la_pagina_inicial_esta_funcionado(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_la_pagina_inicial_tiene_el_titulo_correcto(self):
        response = self.client.get('/')
        self.assertContains(response, 'Kardex App')

    def test_la_portada_usa_la_plantilla_correcta(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'kardex/index.html')
