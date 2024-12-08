import unittest
from functions import generate, create_trie, print_trie

class test_generate(unittest.TestCase):
    def test_case_1(self):
        degree = 2
        roots, comp = create_trie(degree)
        melody = generate(["C4", "C5"], 50, roots, degree)
        ok = True
        #print_trie(roots, degree)
        with open('test.txt', 'w') as f:
            for i in comp:
                for j in i:
                    f.write(''.join(j))
                f.write("\n")
        for i in range(len(melody)-degree):
            if melody[i: i + degree + 1] not in comp:
                print(melody[i: i + degree + 1])
                ok = False
        self.assertTrue(ok)

        

    