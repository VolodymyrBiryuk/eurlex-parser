import unittest

from bs4 import BeautifulSoup

import eurlex


class TestParseAnnexes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('markup_all.html', 'r') as file:
            cls.markup = file.read()

    def test_parse_annexes(self):
        soup = BeautifulSoup(self.markup, 'lxml')
        annexes = eurlex.parse_annexes(soup)

        annex_parts = annexes[0]['content'].split('\n\n')
        self.assertEqual(13, len(annex_parts))

        annex_parts = annexes[1]['content'].split('\n\n')
        self.assertEqual(1, len(annex_parts))

        annex_parts = annexes[2]['content'].split('\n\n')
        self.assertEqual(6, len(annex_parts))

        annex_parts = annexes[3]['content'].split('\n\n')
        self.assertEqual(2, len(annex_parts))

        annex_parts = annexes[4]['content'].split('\n\n')
        self.assertEqual(11, len(annex_parts))

        annex_parts = annexes[5]['content'].split('\n\n')
        self.assertEqual(3, len(annex_parts))


if __name__ == '__main__':
    unittest.main()
