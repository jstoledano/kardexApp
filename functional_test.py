import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        try:
            self.browser.quit()
        except Exception as e:
            print(e)
            pass

    def test_puedo_ver_la_pagina_de_inicio(self) -> None:
        self.browser.get('http://localhost:8000')
        self.assertIn('Kardex App', self.browser.title)
        self.fail('Terminando la prueba!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
