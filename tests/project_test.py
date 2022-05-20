import unittest
from parameterized import parameterized

from project.helper_functions.pdf_to_csv import pdf_processor

class TestHelpers(unittest):

    @parameterized.expand([
       ("cheese", 'failed', TypeError),
       ("/pdf_files", "/csv_files", '')
   ])
    def test_pdf_processor(self, func, input1, input2, expected_output):
        self.assertEqual(pdf_processor(input1, input2), expected_output)


if __name__ == '__main__':
    unittest.main()