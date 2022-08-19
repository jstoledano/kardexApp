from datetime import date, timedelta

from django.test import TestCase

from kardex.models import Materia, Clase, Tarea

INICIO: int = 15


class ModelosTest(TestCase):
    def setUp(self):
        self.materia = Materia(
            clave='1156',
            nombre='Teoría del Conocimiento',
            tipo='1',
            semestre=1,
            puntos=8
        )
        self.materia.save()
        self.clase = Clase(
            materia=self.materia,
            periodo='2020-1',
            grupo='8169',
            asesor='Erika Angelina Nuevo'
        )
        self.clase.save()
        self.tarea1 = Tarea(
            clase=self.clase,
            unidad=1,
            actividad='1',
            f_entrega=date(2020, 1, 16),
            desc='Descripción de la tarea'
        )
        self.tarea1.save()
        self.tareaC1 = Tarea(
            clase=self.clase,
            unidad=1,
            actividad='C1',
            f_entrega=date(2020, 1, 18),
            desc='Descripción de la tarea'
        )
        self.tareaC1.save()

    def test_materia_string(self):
        self.assertEqual(str(self.materia), '1156 Teoría del Conocimiento')

    def test_materia_tipo_display(self):
        self.assertEqual(self.materia.get_tipo_display(), 'Obligatoria')

    def test_clase_string(self):
        self.assertEqual(str(self.clase), '1156 - 8169 - Teoría del Conocimiento (2020-1)')

    def test_tarea1_string(self):
        self.assertEqual(str(self.tarea1), '1156:01:01')

    def test_tarea_f_inicio(self):
        self.assertEqual(self.tarea1.f_inicio, date(2020, 1, 1))

    def test_tarea_inicio(self):
        self.assertEqual(self.tarea1.f_inicio, self.tarea1.f_entrega - timedelta(days=INICIO))

    def test_tareaC1_string(self):
        self.assertEqual(str(self.tareaC1), '1156:01:C1')

    def tearDown(self):
        pass


class HomePageTest(TestCase):

    def test_la_pagina_inicial_esta_funcionado(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_la_pagina_inicial_tiene_el_titulo_correcto(self):
        response = self.client.get('/')
        self.assertContains(response, 'Kardex App')

    def test_la_portada_usa_la_plantilla_correcta(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'kardex/index.html')

    def test_one_entry(self):
        self.materia = Materia(
            clave='1264',
            nombre='Costos y Presupuestos',
            tipo='1',
            semestre=6,
            puntos=8
        )
        self.materia.save()
        response = self.client.get('/')
        self.assertContains(response, '1264')
        self.assertContains(response, 'Costos y Presupuestos')

    def test_two_entries(self):
        self.materia = Materia(
            clave='1264',
            nombre='Costos y Presupuestos',
            tipo='1',
            semestre=6,
            puntos=8
        )
        self.materia.save()
        self.materia = Materia(
            clave='1265',
            nombre='Economía',
            tipo='1',
            semestre=6,
            puntos=8
        )
        self.materia.save()
        response = self.client.get('/')
        self.assertContains(response, '1264')
        self.assertContains(response, 'Costos y Presupuestos')
        self.assertContains(response, '1265')
        self.assertContains(response, 'Economía')
