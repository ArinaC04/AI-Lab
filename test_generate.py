import unittest
from functions import generate, create_trie

class test_generate(unittest.TestCase):
    def test_case_1(self):
        degree = 4
        roots, comp = create_trie(degree)
        melody = generate(["C4", "C5"], 50, roots, degree)
        for i in range(len(melody)-degree):
            self.assertTrue(melody[i: i + degree] in comp)

        

    