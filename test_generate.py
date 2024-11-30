import unittest
from functions import generate, create_trie

class test_generate(unittest.TestCase):
    def test_case_1(self):
        input_data = create_trie()
        expected_result = True
        
        self.assertEqual(generate(input_data), expected_result)

    