import unittest

from bs4 import BeautifulSoup

import eurlex


class TestParseTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('markup_celex_de.html', 'r') as file:
            cls.celex_markup_de = file.read()

    def test_parse_title(self):
        input = self.celex_markup_de.replace('\xa0', ' ').replace('&nbsp;', ' ')
        soup = BeautifulSoup(input, 'lxml')
        eurlex.language = 'DE'
        expected = 'VERORDNUNG (EU) Nr. 10/2011 DER KOMMISSION - vom 14. Januar 2011 - über Materialien und Gegenstände aus Kunststoff, die dazu bestimmt sind, mit Lebensmitteln in Berührung zu kommen'
        actual = eurlex.parse_title(soup)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
