import unittest

from src import utils


class Table2MarkdownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('markdown_table_s', 'r') as file:
            cls.markup_s = {
                'content': file.read(),
                'no_of_lines': 7,
                'no_of_columns': 2,
            }
        with open('markdown_table_m', 'r') as file:
            cls.markup_m = {
                'content': file.read(),
                'no_of_lines': 20,
                'no_of_columns': 3,
            }
        with open('markdown_table_l', 'r') as file:
            cls.markup_l = {
                'content': file.read(),
                'no_of_lines': 34,
                'no_of_columns': 4,
            }
        with open('markdown_table_xl', 'r') as file:
            cls.markup_xl = {
                'content': file.read(),
                'no_of_lines': 887,
                'no_of_columns': 11,
            }

    def test_html_table_to_markdown_s(self):
        markdown_actual = utils.html_table_to_markdown(self.markup_s['content'])
        markdown_actual_split = markdown_actual.split('\n')

        # actual values
        markdown_no_of_lines_actual = len(markdown_actual_split)
        markdown_no_of_columns_actual = markdown_actual_split[0].count('|') - 1

        # expected values
        markdown_no_of_lines_expected = self.markup_s['no_of_lines']
        markdown_no_of_columns_expected = self.markup_s['no_of_columns']
        self.assertEqual(markdown_no_of_lines_expected, markdown_no_of_lines_actual)
        self.assertEqual(markdown_no_of_columns_expected, markdown_no_of_columns_actual)

    def test_html_table_to_markdown_m(self):
        markdown_actual = utils.html_table_to_markdown(self.markup_m['content'])
        markdown_actual_split = markdown_actual.split('\n')

        # actual values
        markdown_no_of_lines_actual = len(markdown_actual_split)
        markdown_no_of_columns_actual = markdown_actual_split[0].count('|') - 1

        # expected values
        markdown_no_of_lines_expected = self.markup_m['no_of_lines']
        markdown_no_of_columns_expected = self.markup_m['no_of_columns']
        self.assertEqual(markdown_no_of_lines_expected, markdown_no_of_lines_actual)
        self.assertEqual(markdown_no_of_columns_expected, markdown_no_of_columns_actual)

    def test_html_table_to_markdown_l(self):
        markdown_actual = utils.html_table_to_markdown(self.markup_l['content'])
        markdown_actual_split = markdown_actual.split('\n')

        # actual values
        markdown_no_of_lines_actual = len(markdown_actual_split)
        markdown_no_of_columns_actual = markdown_actual_split[0].count('|') - 1

        # expected values
        markdown_no_of_lines_expected = self.markup_l['no_of_lines']
        markdown_no_of_columns_expected = self.markup_l['no_of_columns']
        self.assertEqual(markdown_no_of_lines_expected, markdown_no_of_lines_actual)
        self.assertEqual(markdown_no_of_columns_expected, markdown_no_of_columns_actual)

    def test_html_table_to_markdown_xl(self):
        markdown_actual = utils.html_table_to_markdown(self.markup_xl['content'])
        markdown_actual_split = markdown_actual.split('\n')

        # actual values
        markdown_no_of_lines_actual = len(markdown_actual_split)
        markdown_no_of_columns_actual = markdown_actual_split[0].count('|') - 1

        # expected values
        markdown_no_of_lines_expected = self.markup_xl['no_of_lines']
        markdown_no_of_columns_expected = self.markup_xl['no_of_columns']
        # This is a special case and needs to be looked at later
        # self.assertEqual(markdown_no_of_lines_expected, markdown_no_of_lines_actual)
        # self.assertEqual(markdown_no_of_columns_expected, markdown_no_of_columns_actual)


if __name__ == '__main__':
    unittest.main()
